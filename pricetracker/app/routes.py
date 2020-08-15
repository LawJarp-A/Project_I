from app import app
from app.forms import get_url
from app.pricet import price
from flask import render_template, redirect


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title = "Welcome")
    # form = get_url()
    # if form.validate_on_submit():
    #     pr = price(form.enter_url.data)
    #     form.enter_url.data = ""
    #     return render_template('index.html', form = form, price = pr)
    # return render_template('index.html', form = form)

@app.route("/getprice", methods = ['GET','POST'])
def get_price():
    form = get_url()
    if form.validate_on_submit():
        pr = price(form.enter_url.data)
        form.enter_url.data = ""
        return render_template('getprice.html', form = form, price = pr, title = "Get Price")
    return render_template('getprice.html', form = form, title = "Get Price")
