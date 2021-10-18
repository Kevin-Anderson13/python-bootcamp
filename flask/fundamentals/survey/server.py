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
    session['name'] = request.form['field1']
    session['about'] = request.form['field2']
    session['location'] = request.form['field3']
    session['favlanguage'] = request.form['field4']
    session['comments'] = request.form ['field5']
    return redirect("/result")

@app.route('/result')
def show_info():
    return render_template("result.html", field1=session['name'], field2=['about'], field3=session['location'], field4=session['favlanguage'], field5=session['comments'])


if __name__=="__main__":
    app.run(debug=True)