<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Films</title>
</head>
<body>
    <h2>Your Films</h2><br><br>
    
    <table border="1">
        <tr>
            <th>Film_ID</th>
            <th>Title</th>
            <th>Description</th>
            <th>Release Year</th>
            <th>Length (minutes)</th>
        </tr>
        % for film in films:
        <tr>
            <td>{{film[0]}}</td>
            <td>{{film[1]}}</td>
            <td>{{film[2]}}</td>
            <td>{{film[3]}}</td>
            <td>{{film[4]}}</td>
        </tr>
        % end
    </table><br><br>

    <h2>Delete a Film</h2>
    <form action="/deleteFilm" method="post">
        <label for="film_id">Film ID</label>
        <input type="text" id="film_id" name="film_id"><br><br>
        <input type="submit" value="Delete Film">
    </form><br><br>

    <form action="/logout" method="get">
        <button type="submit">Logout</button>
    </form>
</body>
</html>