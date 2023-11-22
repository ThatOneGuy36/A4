from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from datetime import datetime


app = Flask(__name__)

# Stored variables for accessing the postgres database
db_name = "A4"
db_username = "postgres"
db_password = "myPOSTGRES"
db_host = "localhost"
db_port = "5432"


# Checks to see if the user has input a valid date
# If the input is invalid (or empty), handle the error and return False
def checkDateValidity(date_str):
    format = "%Y-%m-%d"
    
    try: 
        datetime.strptime(date_str, format)
        return True
    
    except ValueError:
        return False


# The homepage of the application
@app.route('/')
def index():
    # Connect to the database
    try:
        conn = psycopg2.connect(database=db_name,
                                user=db_username,
                                password=db_password,
                                host=db_host,
                                port=db_port)
        print("Database connected successfully")
    
    except:
        print("Database not connected successfully")
                
    
    cur = conn.cursor()
    
    # Get all records from the table and display them accordingly on the homepage
    cur.execute("SELECT * FROM students")
    data = cur.fetchall() 
        
    cur.close() 
    conn.close() 
    
    return render_template('Main.html', data=data)
    
    
# Gives the user the ability to add a record to the database, assuming all inputs are valid   
@app.route('/create', methods=['POST'])
def create():
    # Connect to the database
    try:
        conn = psycopg2.connect(database=db_name,
                                user=db_username,
                                password=db_password,
                                host=db_host,
                                port=db_port)
    
    except:
        print("Database not connected successfully")
                
    
    cur = conn.cursor()
    
    # Get all of the user's inputs
    fName = request.form['FirstName']
    lName = request.form['LastName']
    email = request.form['Email']
    enrollDate = request.form['EnrollmentDate']
    
    
    # Make sure the user has filled out all the required forms
    # If not, send them to the error page
    if (fName == ""):
        return render_template('Error.html', data=('create', 'Missing field: `First Name`'))
        
    elif (lName == ""):
        return render_template('Error.html', data=('create', 'Missing field: `Last Name`'))
        
    elif (email == ""):
        return render_template('Error.html', data=('create', 'Missing field: `Email`'))
        
    elif (checkDateValidity(enrollDate) == False):
        enrollDate = '1500-01-01'
        
    else:
        pass
        
    
    
    # See if the email has already been used, and handle error accordingly
    try:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date)"
                    "VALUES (%s, %s, %s, %s)", (fName, lName, email, enrollDate))
    
    except:
        return render_template('Error.html', data=('create', 'Non-unique email entered'))
    
    conn.commit()
        
    cur.close() 
    conn.close() 
    
    return redirect(url_for('index'))
    

# Allows the user to delete a student record from the database, assuming the student ID exists
@app.route('/delete', methods=['POST'])
def delete():
    # Connect to the database
    try:
        conn = psycopg2.connect(database=db_name,
                                user=db_username,
                                password=db_password,
                                host=db_host,
                                port=db_port)
    
    except:
        print("Database not connected successfully")
                
    
    cur = conn.cursor()
    
    stuID = request.form['StudentID']


    if (stuID == ""):
        return render_template('Error.html', data=('delete', 'Missing field: `Student ID`'))


    cur.execute("DELETE FROM students WHERE student_id = %s", (stuID,))
    conn.commit()

        
    cur.close() 
    conn.close() 
    
    return redirect(url_for('index'))
    

# Allows the user to modify a current student's email in the database
@app.route('/update', methods=['POST'])
def update():
    # Connect to the database
    try:
        conn = psycopg2.connect(database=db_name,
                                user=db_username,
                                password=db_password,
                                host=db_host,
                                port=db_port)
    
    except:
        print("Database not connected successfully")
                
    
    cur = conn.cursor()
    
    stuID = request.form['StudentID']
    email = request.form['Email']
    
    
    if (stuID == ""):
        return render_template('Error.html', data=('update', 'Missing field: `Student ID`'))
    
    elif (email == ""):
        return render_template('Error.html', data=('update', 'Missing field: `Email`'))


    # Need to make sure the email isn't already in use, and handle the potential error accordingly
    try:
        cur.execute("UPDATE students SET email=%s WHERE student_id=%s", (email, stuID))
    
    except Exception as e:
        return render_template('Error.html', data=('update', 'Non-unique email entered'))
    
    conn.commit()

        
    cur.close() 
    conn.close() 
    
    return redirect(url_for('index'))
    

if __name__ == '__main__':
   app.run()
