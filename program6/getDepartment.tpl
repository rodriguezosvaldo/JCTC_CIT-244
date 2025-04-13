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
            <h1>Get Payroll by Department</h1><br>
            <form action="/getDepartment" method="POST">
                <label for="department">Select a department</label>
                <select name="department" id="department" class="form-control">
                    {foreach from=$departments item=department}
                        <option value="{$department.id}">{$department.name}</option>
                    {/foreach}
                </select><br>
                <input type="submit" value="Get Payroll" class="btn btn-primary">
            </form>
        </main>
    </body>
</html>