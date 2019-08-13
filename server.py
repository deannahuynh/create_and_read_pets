from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route('/')
def index():
    mysql = connectToMySQL('pets')
    pets = mysql.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route('/create_pet', methods=['POST'])
def create_pet():
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(pname)s, %(ptype)s, NOW(), NOW());"
    data = {
        'pname': request.form['pet_name'],
        'ptype': request.form['pet_type']
    }
    mysql = connectToMySQL('pets')
    mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)
