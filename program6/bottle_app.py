import sqlite3
from bottle import route, run, request, response, template

@route('/', method='GET')
def home():
    return template('home')

@route('/getDepartment', method='GET')
def get_department():
    return template('getDepartment')

@route('/editHours', method='GET')
def edit_hours():
    return template('editHours')

@route('/getDepartment', method='POST')#######################Review this code
def get_department():
    department = request.forms.get('department')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM departments WHERE name=?", (department,))
    data = cursor.fetchall()
    conn.close()
    return template('getDepartment', data=data)

@route('/editHours', method='POST')##########################Review this code
def edit_hours():
    emp_id = request.forms.get('emp_id')
    hrs_worked = request.forms.get('hrs_worked')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE pay_data SET hrs_worked=? WHERE emp_id=?", (hrs_worked, emp_id))
    conn.commit()
    conn.close()
    return template('editHours', success=True)