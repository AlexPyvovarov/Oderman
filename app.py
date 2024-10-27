from flask import Flask, render_template, request, redirect, url_for
from sqlmodel import select
from database import session, Pizza, Question, Option, Vote


app = Flask(__name__)
app.secret_key = "iuwefuoebnfbbh90DSfh;"
title = "Oderman"


def mock():
        lang = Question(
            name="Ваша улюблена мова програмування",
            options=[
                Option(name="Python"),
                Option(name="Java"),
                Option(name="JavaScript"),
                Option(name="C#"),
                Option(name="C++"),
            ],
        )
        gender = Question(
            name="Оберіть зайве",
            options=[
                Option(name="Male"),
                Option(name="Female"),
                Option(name="Neither"),
                Option(name="Helicopter"),
                Option(name="Quadrobber"),
            ],
        )
        session.add(gender)
        session.add(lang)
        session.commit()


def add_data(name, price, summary):
    pizza = Pizza(name=name, price=price, summary=summary)
    session.add(pizza)
    session.commit()



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


@app.post("/poll/result")
def vote_result():
    question_id = request.form.get("question_id")
    option_id = request.form.get("option_id")
    question = session.get(Question, question_id)
    option = session.get(Option, option_id)
    if question and option:
        session.add(Vote(question=question, option=option))
        return redirect(url_for(index.__name__))
    return redirect(url_for(poll.__name__))





if __name__ == "__main__":
    add_data(name="margarita", price=99, summary="peperoni, cheese, tomato")
    mock()
    app.run(debug=True)