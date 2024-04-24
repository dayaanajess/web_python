from flask import Flask

app = Flask(__name__)

@app.route("/")
def p1():
    return "Hello Future!"

@app.route("/second_page")
def p2():
    return "Home!"

if __name__ == "__main__":
    app.run()

