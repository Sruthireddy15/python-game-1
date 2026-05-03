from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

html = """
<h1>Rock Paper Scissors</h1>

<form method="POST">
    <button name="move" value="rock">Rock</button>
    <button name="move" value="paper">Paper</button>
    <button name="move" value="scissors">Scissors</button>
</form>

<h2>{{ result }}</h2>
"""

def game(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You Win"
    else:
        return "Computer Wins"
def game(sruthi, computer):

    if sruthi == computer:
        return "Tie"

    if sruthi == "rock" and computer == "scissors":
        return "You Win"

    if sruthi == "paper" and computer == "rock":
        return "You Win"

    if sruthi == "scissors" and computer == "paper":
        return "You Win"

    return "Computer Wins"

@app.route("/", methods=["GET", "POST"])
def home():
    result = "Click a button!"

    if request.method == "POST":
        user = request.form["move"]
        computer = random.choice(choices)
        result = f"You: {user} | Computer: {computer} → {game(user, computer)}"

    return render_template_string(html, result=result)


if __name__ == "__main__":
    app.run(debug=True)