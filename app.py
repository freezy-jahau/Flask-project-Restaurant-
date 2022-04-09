from flask import Flask, render_template,url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/item/')
def item():
    return render_template("item.html")

@app.route('/order/')
def order():
    return render_template("order.html")

if __name__=="__main__":
    app.run(host='127.0.0.1' ,port=5500 ,debug=True)