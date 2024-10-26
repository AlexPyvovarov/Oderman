from flask import Flask, render_template, request, redirect, url_for
from sqlmodel import select
from database import session, Pizza, Question, Option, Vote


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

@app.get("/poll")
def poll():
    questions = session.scalars(select(Question)).all()
    return render_template("poll.html", questions=questions)


@app.post("/votes_result")
def votes_result():
    question_id = request.form.get("question_id")
    option_id = request.form.get("option_id")
    question = session.get(Question, question_id)
    option = session.get(Option, option_id)
    if question and option:
        session.add(Vote(question=question, option=option))
        return redirect(url_for(index.__name__))
    return redirect(url_for(poll.__name__))


def add_data(name, price, summary):
    pizza = Pizza(name=name, price=price, summary=summary)
    session.add(pizza)
    session.commit()




if __name__ == "__main__":
    add_data(name="margarita", price=99, summary="peperoni, cheese, tomato")
    app.run(debug=True)