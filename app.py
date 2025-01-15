from flask import Flask
from flask import render_template,request

app= Flask(__name__) ##variable is same as file name

@app.route("/")
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()