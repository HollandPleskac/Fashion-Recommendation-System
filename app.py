from flask import Flask, render_template, request
from fashion import getRecommendations
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        submitted_text = request.form['recommendation']
        recommendations = getRecommendations(submitted_text)
        return render_template("output.html", recommendations=recommendations)


@app.route("/home")
def home():
    return "Welcome to the home page!"

if __name__ == "__main__":
  app.run()
# debug=True, host="0.0.0.0"
# integration fashion-recommender with the server
# user input in html input box -> give recommendation based on what they type
# presentation (website) -> what app looks like (design look), questions by monday
