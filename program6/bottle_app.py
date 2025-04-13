import sqlite3
from bottle import route, run, request, template

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

@route('/getDepartment', method='POST')
def get_department():
    department = request.forms.get('department')
    conn = sqlite3.connect('payroll.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT employees.emp_id, employees.emp_name, employees.wage, pay_data.hrs_worked 
                   FROM employees INNER JOIN pay_data ON employees.emp_id = pay_data.emp_id 
                   WHERE employees.department = ? ''', (department,))
    data = cursor.fetchall()
    employees_data = []
    for employee in data:
        if employee[3] > 40:
            overtime_pay = (employee[3] - 40)*1.5*employee[2]
            weekly_pay = 40*employee[2] + overtime_pay
        else:
            weekly_pay = employee[3]*employee[2]
        employee += (weekly_pay,)
        employees_data.append(employee)
    
    cursor.close()
    conn.close()
    return template('employeesByDepartment', employees_data=employees_data, department=department)

@route('/editHours', method='POST')
def edit_hours():
    emp_id = request.forms.get('emp_id')
    hrs_worked = request.forms.get('hrs_worked')
    conn = sqlite3.connect('payroll.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE pay_data SET hrs_worked=? WHERE emp_id=?", (hrs_worked, emp_id))
    cursor.execute("SELECT emp_name FROM employees WHERE emp_id=?", (emp_id,))
    name = cursor.fetchone()[0]
    cursor.execute("SELECT department FROM employees WHERE emp_id=?", (emp_id,))
    department = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return template('status', emp_id=emp_id, name=name, department=department, hrs_worked=hrs_worked)


run(host='localhost', port=8080)