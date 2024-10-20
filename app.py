from flask import Flask, render_template, request
from sqlmodel import select
from database import session, Pizza


app = Flask(__name__)
app.secret_key = "iuwefuoebnfbbh90DSfh;"
title = "Oderman"

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


# def mock_data():
#     pizzas = [Pizza(name=f"{x}", price=x, summary=f"{x}") for x in range(1, 11)]
#     session.add_all(pizzas)
#     session.commit()


def add_data(name, price, summary):
    pizza = Pizza(name=name, price=price, summary=summary)
    session.add(pizza)
    session.commit()

if __name__ == "__main__":
    # mock_data()
    add_data(name="margarita", price=99, summary="peperoni, cheese, tomato")
    app.run(debug=True)