<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Get Department</title>
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    </head>
    <body class="container">
        <header>
            <nav class="navbar navbar-default"> 
                <ul class="nav navbar-nav"> 
                    <li>
                        <a>Payroll Website</a>
                    </li> 
                    <li>
                        <a href="/">Home</a>
                    </li> 
                    <li class="active">
                        <a href="/getDepartment">View by Department</a>
                    </li>  
                    <li>
                        <a href="/editHours">Edit employee data</a>
                    </li>  
                </ul> 
            </nav>
        </header>
        <main>
            <h1>Department: <span>{{department}}</span></h1><br>
            <table class="table table-striped">
                <thead>    
                    <tr>
                        <th>Emp ID</th>
                        <th>Name</th>
                        <th>Wage</th>
                        <th>Hours Worked</th>
                        <th>Weekly pay</th>
                    </tr>
                </thead>
                <tbody>
                    %for employee in employees_data:
                    <tr>
                        <td>{{employee[0]}}</td>
                        <td>{{employee[1]}}</td>
                        <td>{{employee[2]}}</td>
                        <td>{{employee[3]}}</td>
                        <td>{{employee[4]}}</td>
                    </tr>
                    %end
                </tbody>
            </table>

        </main>
    </body>
</html>