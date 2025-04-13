<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add a Film</title>
</head>
<body>
    <h2>Add a new film to the database</h2>
    <form action="/addFilm" method="post">
        <label for="title">Title</label>
        <input type="text" id="title" name="title" required><br><br>

        <label for="description">Description</label>
        <input type="text" id="description" name="description" required><br><br>

        <p>release_year will be your default year</p>

        <label for="length">Length in minutes</label>
        <input type="text" id="length" name="length" required><br><br>

        <label for="category">Category</label>
        <select id="category" name="category" required>
            <option value="1">Action</option>
            <option value="2">Animation</option>
            <option value="3">Children</option>        
            <option value="4">Classic</option>
            <option value="5">Comedy</option>
            <option value="6">Documentary</option>
            <option value="7">Drama</option>
            <option value="8">Family</option>
            <option value="9">Foreign</option>
            <option value="10">Horror</option>
            <option value="11">Musical</option>
            <option value="12">Sci-Fi</option>
        </select>

        <input type="submit" value="Add Film">
    </form><br><br>

    <form action="/logout" method="get">
        <button type="submit">Logout</button>
    </form>
</body>
</html>