from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html",rows=8,columns=8,first_color='pink',second_color='green')


@app.route('/<int:x>')
def rows(x):
    return render_template("index.html",rows=x,columns=8,first_color='pink',second_color='green')

@app.route('/<int:x>/<int:y>')
def rows_columns(x,y):
    return render_template("index.html",rows=x,columns=y,first_color='pink',second_color='green')

@app.route('/<int:x>/<int:y>/<string:one>')
def rows_columns_one(x,y,one):
    return render_template("index.html",rows=x,columns=y,first_color=one,second_color='green')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def rows_columns_two(x,y,one,two):
    return render_template("index.html",rows=x,columns=y,first_color=one,second_color=two)

if __name__=="__main__":
    app.run(debug=True)