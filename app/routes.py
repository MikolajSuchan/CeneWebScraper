from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/extraction')
def extraction():
    return render_template('extraction.html')

@app.route('/products_list')
def products_list():
    return render_template('products_list.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/author')
def author():
    return render_template('author.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

