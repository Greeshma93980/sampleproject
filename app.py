from flask import Flask,render_template
app=Flask(__name__)
@app.route("/home")
def home():
    return "Home page"
@app.route("/")
def index():
    return render_template("index.html")
def index():
    return "Welcome to Flask"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=10000)