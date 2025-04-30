from flask import Flask, render_template, request, redirect, url_for
import math
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        income = int(request.form["income"])
        return redirect(url_for('pick_game', budget=income/100))
    return render_template("index.html")

@app.route("/pick_game")
def pick_game():
    budget = float(request.args.get('budget'))
    return render_template("pick_game.html", budget=budget)

@app.route("/fgo", methods=["GET", "POST"])
def fgo():
    budget = float(request.args.get("budget"))

    if request.method == "POST":
        summon_choice = request.form["summon_choice"]
        summon_cost = 3
        rates = {
            "1": 0.8,
            "2": 1,
            "3": 0.11,
            "4": 1.4
        }
        choice = rates.get(summon_choice, 0)
        hypo_guarantee = 100 / choice
        sq_needed = hypo_guarantee * summon_cost
        cost_estimate = sq_needed / 1.575

        current_pulls = int(request.form.get("current_pulls", 0))
        needed_sq = sq_needed - (current_pulls * summon_cost)
        remaining_cost = needed_sq / 1.575

        over_budget = remaining_cost > budget
        months_to_wait = round(remaining_cost / budget, 1) if over_budget else 0

        return render_template("result.html",
                               choice=choice,
                               hypo_guarantee=hypo_guarantee,
                               sq_needed=sq_needed,
                               cost_estimate=cost_estimate,
                               remaining_cost=remaining_cost,
                               budget=budget,
                               over_budget=over_budget,
                               months_to_wait=months_to_wait)

    # GET method just renders the summon form
    return render_template("summon_options.html", budget=budget)

@app.route("/roulette", methods=["GET", "POST"])
def roulette():
    budget = float(request.args.get("budget"))

    if request.method == "POST":
        roulette_choice = request.form["roulette_choice"]

        odds = {
            "1": 48.6,
            "2": 48.6,
            "3": 48.6,
            "4": 48.6,
            "5": 32.4,
            "6": 32.4,
            "7": 32.4,
            "8": 2.7,
            "9": 5.4,
            "10": 8.1,
            "11": 10.8,
            "12": 16.2
        }

        chance = odds.get(roulette_choice, 0)
        hypo_guarantee = math.ceil(100 / chance)
        money_per_attempt = budget / hypo_guarantee

        return render_template("result.html",
                               game="roulette",
                               choice=chance,
                               hypo_guarantee=hypo_guarantee,
                               sq_needed=0,  # Not relevant
                               cost_estimate=0,  # Not relevant
                               remaining_cost=0,  # Not relevant
                               budget=budget,
                               over_budget=False,
                               months_to_wait=0,
                               money_per_attempt=round(money_per_attempt, 2))

    return render_template("roulette.html", budget=budget)

if __name__ == "__main__":
    app.run(debug=True)
