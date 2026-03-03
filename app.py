from flask import Flask, render_template, session, request, redirect, url_for

from game import engine
from game.data import common

app = Flask(__name__)
import os
app.secret_key = os.environ.get("SECRET_KEY", "stcc-dev-secret-change-in-production")


# ── Helpers ───────────────────────────────────────────────────────────────────

def _game() -> dict:
    return session["game"]


def _save(state: dict):
    session["game"] = state
    session.modified = True


# ── Index / captain select ────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():
    captain_id = request.form.get("captain", "shran")
    state = engine.initialize_game(captain_id)
    _save(state)
    return redirect(url_for("game"))


# ── Main game view ────────────────────────────────────────────────────────────

@app.route("/game")
def game():
    if "game" not in session:
        return redirect(url_for("index"))
    state = _game()
    module = engine.get_captain_module(state["captain_id"])
    captain_card = engine.get_card(state["captain_card"]) if state["captain_card"] else None
    do_card = engine.get_card(state["duty_officer_card"]) if state["duty_officer_card"] else None
    return render_template(
        "game.html",
        state=state,
        stats=engine.deck_stats(state),
        captain_info=module.CAPTAIN_INFO,
        captain_card=captain_card,
        do_card=do_card,
        turn_cards=[],
    )


# ── Draw cards ────────────────────────────────────────────────────────────────

@app.route("/game/draw", methods=["POST"])
def draw():
    count = max(1, min(int(request.form.get("count", 1)), 10))
    state = _game()

    drawn_displays = []
    for _ in range(count):
        card_id, state = engine.draw_card(state)
        if card_id is None:
            break
        display = engine.resolve_card_display(state, card_id)
        drawn_displays.append(display)

    _save(state)
    module = engine.get_captain_module(state["captain_id"])
    return render_template(
        "partials/draw_result.html",
        drawn=drawn_displays,
        state=state,
        stats=engine.deck_stats(state),
        captain_info=module.CAPTAIN_INFO,
    )


# ── Deck operations ───────────────────────────────────────────────────────────

@app.route("/game/deck/discard-top/<int:count>", methods=["POST"])
def deck_discard_top(count):
    state = _game()
    discarded, state = engine.discard_top(state, count)
    _save(state)
    cards = [engine.get_card(cid) for cid in discarded]
    return render_template(
        "partials/op_result.html",
        message=f"Discarded {len(cards)} card(s) from top of draw deck.",
        affected_cards=cards,
        stats=engine.deck_stats(state),
    )


@app.route("/game/deck/log-top", methods=["POST"])
def deck_log_top():
    state = _game()
    card_id, state = engine.log_top_card(state)
    _save(state)
    card = engine.get_card(card_id) if card_id else None
    return render_template(
        "partials/op_result.html",
        message="Logged top card of draw deck (removed from game).",
        affected_cards=[card] if card else [],
        stats=engine.deck_stats(state),
    )


@app.route("/game/deck/log/<card_id>", methods=["POST"])
def deck_log_card(card_id):
    state = _game()
    state = engine.log_card(state, card_id)
    _save(state)
    card = engine.get_card(card_id)
    return render_template(
        "partials/op_result.html",
        message=f"Logged '{card['name'] if card else card_id}' (removed from game).",
        affected_cards=[card] if card else [],
        stats=engine.deck_stats(state),
    )


@app.route("/game/deck/return/<card_id>", methods=["POST"])
def deck_return_card(card_id):
    state = _game()
    state = engine.return_card_to_deck(state, card_id)
    _save(state)
    card = engine.get_card(card_id)
    return render_template(
        "partials/op_result.html",
        message=f"Returned '{card['name'] if card else card_id}' to draw deck.",
        affected_cards=[],
        stats=engine.deck_stats(state),
    )


# ── Duty officer ──────────────────────────────────────────────────────────────

@app.route("/game/duty-officer/promote/<card_id>", methods=["POST"])
def do_promote(card_id):
    state = _game()
    state = engine.promote_duty_officer(state, card_id)
    _save(state)
    card = engine.get_card(card_id)
    do_name = card["name"] if card else card_id
    return render_template(
        "partials/op_result.html",
        message=f"'{do_name}' promoted to Duty Officer.",
        affected_cards=[],
        stats=engine.deck_stats(state),
        do_card=card,
        has_do=state["has_duty_officer"],
    )


@app.route("/game/duty-officer/log", methods=["POST"])
def do_log():
    state = _game()
    old_do = engine.get_card(state["duty_officer_card"]) if state["duty_officer_card"] else None
    state = engine.log_duty_officer(state)
    _save(state)
    do_name = old_do["name"] if old_do else "Duty Officer"
    return render_template(
        "partials/op_result.html",
        message=f"'{do_name}' logged (Duty Officer dismissed and removed from game).",
        affected_cards=[old_do] if old_do else [],
        stats=engine.deck_stats(state),
        has_do=False,
    )


@app.route("/game/duty-officer/dismiss", methods=["POST"])
def do_dismiss():
    state = _game()
    old_do = engine.get_card(state["duty_officer_card"]) if state["duty_officer_card"] else None
    state = engine.dismiss_duty_officer(state)
    _save(state)
    do_name = old_do["name"] if old_do else "Duty Officer"
    return render_template(
        "partials/op_result.html",
        message=f"'{do_name}' dismissed (returned to discard pile).",
        affected_cards=[],
        stats=engine.deck_stats(state),
        has_do=False,
    )


# ── Resources ─────────────────────────────────────────────────────────────────

@app.route("/game/resource", methods=["POST"])
def resource_update():
    state = _game()
    res   = request.form.get("resource")
    delta = int(request.form.get("delta", 0))
    state = engine.update_resource(state, res, delta)
    _save(state)
    return render_template("partials/resources.html", state=state)


# ── Gain card (common pool selector) ─────────────────────────────────────────

@app.route("/game/gain-card")
def gain_card_panel():
    """Returns the card-gain selector panel (HTMX GET)."""
    card_type = request.args.get("type", "")
    cards = common.BY_TYPE.get(card_type, []) if card_type else []
    all_types = list(common.BY_TYPE.keys())
    return render_template(
        "partials/gain_card.html",
        card_type=card_type,
        cards=cards,
        all_types=all_types,
    )


@app.route("/game/gain-card", methods=["POST"])
def gain_card_submit():
    state  = _game()
    card_id = request.form.get("card_id")
    if card_id:
        state = engine.gain_card(state, card_id)
        _save(state)
    card = engine.get_card(card_id) if card_id else None
    return render_template(
        "partials/op_result.html",
        message=f"'{card['name'] if card else '?'}' added to Bot discard pile.",
        affected_cards=[card] if card else [],
        stats=engine.deck_stats(state),
    )


# ── Reset ─────────────────────────────────────────────────────────────────────

@app.route("/game/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
