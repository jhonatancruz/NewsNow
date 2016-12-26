from flask import Flask, request, render_template

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/verify')
def verify():
    return '<h1>NewsNowVerify</h1>'


if __name__ =="__main__":
    app.run(debug=True)
