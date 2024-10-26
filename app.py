from flask import Flask, render_template, request
from sqlmodel import select
from database import session, Pizza


app = Flask(__name__)
app.secret_key = "iuwefuoebnfbbh90DSfh;"
title = "Oderman"
poll_data = {
'question': 'Which web framework do you use?',
'answers': ['Flask', 'Django']
}

@app.get("/")
def index():
    return render_template("index.html")


@app.get("/pizzas")
def pizza():
    pizzas = session.scalars(select(Pizza)).all()
    return render_template("index.html", pizzas = pizzas)


@app.get("/pizza_view")
def pizza_view():
    id = int(request.args.get("pizza_id"))
    pizza = session.get_one(Pizza, id)
    pizza = pizza.model_dump()
    return render_template("view.html", pizza = pizza)

@app.get("/poll")
def poll():
    return render_template("poll.html", poll_data = poll_data)


@app.get("/poll_results")
def poll_results():
    vote = request.args.get('answers')
    with open("data.txt", 'a') as f:
        f.write(vote)
        f.close()
    return render_template('poll_results.html', poll_data = poll_data, votes=vote)


def add_data(name, price, summary):
    pizza = Pizza(name=name, price=price, summary=summary)
    session.add(pizza)
    session.commit()

if __name__ == "__main__":
    add_data(name="margarita", price=99, summary="peperoni, cheese, tomato")
    app.run(debug=True)