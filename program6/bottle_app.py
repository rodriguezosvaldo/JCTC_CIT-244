import sqlite3
from bottle import route, run, request, response, template

@route('/', method='GET')
def home():
    return template('home')

@route('/getDepartment', method='GET')
def get_department():
    conn = sqlite3.connect('payroll.db')
    cursor = conn.cursor()
    cursor.execute("SELECT department FROM employees")
    departments_data = cursor.fetchall()
    departments = []
    for i in departments_data:
        departments.append(i[0]) if i[0] not in departments else None
    
    cursor.close()
    conn.close()
    return template('getDepartment', departments=departments)

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





run(host='localhost', port=8080)