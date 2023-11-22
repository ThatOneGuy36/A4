# A4
My submission for assignment 4 for COMP3005


Setup Instructions:
1. Install both Flask and psycopg2 using the pip installer for python (version numbers included in the requirements file). Use:
	- pip install Flask
	- pip install psycopg2
in the command line before running the application.

2. Download all the files and put them in a new folder together. Place the html files in a folder named 'templates' and the CSS/JavaScript files in a folder named 'static' (these are case sensitive). The python file should be outside of both folders.

3. Create a new database in pgAdmin4 (any name is fine, just keep note of it)

4. Run the SQL code provided in the 'generateTable' file in the pgadmin4 database query tool in order to create and populate the table
   
5. Open 'Main.py' and set the value of the variables at the top with:
	- Your database name
	- Your username and password for pgadmin4
	- The name of the host (likely localhost)
	- The port number (likely 5432)



Steps to Compile and Run Application:
1. Navigate to your new folder location in the command prompt window, and type 'python Main.py'

2. Go to the link provided in the line 'Running on http:// ...' to use the application



Brief Explanation of each Function:
checkDateValidity:
- Checks to see if the date inputted was written in a valid format. If so, it returns true, and if not, it handles the error that would be returned and returns false.

index:
- Handles the logic of the landing page by connecting to the database and printing all student records to the screen.

create:
- Handles the values received when creating a new student record, and attempts to run the corresponding SQL code. If any error is encountered, it will send the user to the error page and abort the SQL operation.

delete:
- Handles the value received when attempting to delete a record from the table. If there are no errors, the corresponding SQL code is run.

update:
- Handles the values received when changing the email for a given student record, and attempts to run the corresponding SQL code. If any error is encountered, it will send the user to the error page and abort the SQL operation.

addStudent / deleteStudent / updateStudent:
- Each of these functions will make the corresponding form appear, and disable the other 2 buttons, allowing the user to perform only 1 operation at a time.



Link to Video Explanation:
https://youtu.be/Gl3Hby8eaL8
