from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def names():
    full_names= [
        {'first_name' : 'Kevin', 'last_name' : 'Anderson'},
        {'first_name' : 'Kelsee', 'last_name' : 'Anderson'},
        {'first_name' : 'Tyson', 'last_name' : 'Galovich'},
        {'first_name' : 'Maddy', 'last_name' : 'Galovich'},
        {'first_name' : 'Zander', 'last_name' : 'Johnson'}
    ]
    return render_template("index.html", names = full_names)


if __name__=="__main__":
    app.run(debug=True)