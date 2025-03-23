# Films Database Application

Simple GUI application built with wxPython that allows users to display and insert film records into a SQLite database. Users can view the list of films stored in the database and add new films through a form. The application connects to a SQLite database named movies.db and interacts with a table named afilms.

# Dependencies
Python 3.x
wxPython
SQLite3
# Installation
Install Python 3.x: Download and install Python from python.org.
Install wxPython: Open a terminal or command prompt and run: pip install wxPython
Ensure SQLite3 is available: SQLite3 is included with Python, but you can verify its availability by running: python -c "import sqlite3; print(sqlite3.sqlite_version)"
Running the Program
Ensure the movies.db SQLite database exists and contains a table named afilms with the appropriate schema.
Run the program by executing the films.py script: python films.py
