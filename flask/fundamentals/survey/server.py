from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'formkey'

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session['about'] = request.form['about']
    session['location'] = request.form['location']
    session['favlanguage'] = request.form['favlanguage']
    session['comments'] = request.form ['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True)