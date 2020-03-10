from flask import Flask, redirect, url_for

app = Flask(__name__)

joe = ("Joe", "Mark", -1,500)

def greeting(first_name, last_name):
    return f"Hello {first_name} {last_name}!"

def current_balance(balance):
    return f"<h1> Your current balance is </h1> {balance}"

@app.route("/")
def menu():
    return "<h1> Welcome to your virtual wallet </h1>"

@app.route("/manage_account")
def manage_account():
    return greeting(joe), current_balance(joe)

if __name__ == "__main__":
    app.run()