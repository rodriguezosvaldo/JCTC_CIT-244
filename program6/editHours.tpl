<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Edit Hours</title>
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    </head>
    <body class="container">
        <header>
            <nav class="navbar navbar-default"> 
                <ul class="nav navbar-nav"> 
                    <li class="active">
                        <a>Payroll Website</a>
                    </li> 
                    <li>
                        <a href="/">Home</a>
                    </li> 
                    <li>
                        <a href="/getDepartment">View by Department</a>
                    </li>  
                    <li class="active">
                        <a href="/editHours">Edit employee data</a>
                    </li>  
                </ul> 
            </nav>
        </header>
        <main>
            <h1>Enter Employer ID and Hours Worked</h1>
            <form action="/editHours" method="POST">
                <input type="text" id="employeeId" name="emp_id" placeholder="Employee ID" class="form-control" style="width: 20%;"><br>
                <input type="text" id="hoursWorked" name="hrs_worked" placeholder="Hours Worked" class="form-control" style="width: 20%;"><br>
                <input type="submit" value="Submit" class="btn btn-primary" id="submitButton"><br><br>
            </form>
        </main>
    </body>
</html>