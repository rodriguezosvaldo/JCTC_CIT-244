import sqlite3
from bottle import route, run, request, response, template

@route('/' , method='GET')
def index():
    return template('index')

@route('/menu', method='GET')
def menu():
    year = request.get_cookie("year")
    if not year:
        return template('status', message="Please login first")
    return template('menu')

@route('/login', method='POST')
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    conn = sqlite3.connect('movies5.db')
    cursor = conn.cursor()
    sql = "SELECT year FROM users WHERE name = ? AND password = ?"
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        response.set_cookie("year", result[0])
        return template("menu")
    else:
        return template('status', message="Invalid username or password")
    
@route('/logout', method='GET')
def logout():
    response.set_cookie("year", "", expires=0)  
    return template('index')
   
@route('/films', method='GET')
def display_films():
    year = request.get_cookie("year")
    if not year:
        return template('status', message="Please login first")

    conn = sqlite3.connect('movies5.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM films WHERE release_year = ?", (year,)) 
    films = cursor.fetchall()
    cursor.close()
    conn.close()
    return template('films', films=films)

@route('/addFilmTemplate', method='GET')
def add_film_template():
    year = request.get_cookie("year")
    if not year:
        return template('status', message="Please login first")

    return template('add_film')

@route('/addFilm', method='POST')
def add_film():
    title = request.forms.get('title')
    description = request.forms.get('description')
    release_year = request.get_cookie("year")
    length = request.forms.get('length')
    category = request.forms.get('category')

    conn = sqlite3.connect('movies5.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO films (title, description, release_year, length, category)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, description, release_year, length, category))
    conn.commit()
    cursor.close()
    conn.close()
    return template('status', message="Film added successfully")

@route('/deleteFilm', method='POST')
def delete_film():
    year = request.get_cookie("year")
    if not year:
        return template('status', message="Please login first")

    film_id = request.forms.get('film_id')
    conn = sqlite3.connect('movies5.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM films WHERE film_id = ?', (film_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return template('status', message="Film deleted successfully")

    

run(host='localhost', port=8080)