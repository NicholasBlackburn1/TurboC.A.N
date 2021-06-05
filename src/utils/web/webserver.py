"""
webserver for displaying car info over ip like a frc dashboard but in pure python
"""


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html",test="uwu")


if __name__ == "__main__":
    app.run()