import pyodbc 
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

def connectToDB():
    server = 'DESKTOP-5GFQ4D9'
    database = 'BackendDevTest'
    username = 'userpython'
    password = 'user'
    driver = '{ODBC Driver 17 for SQL Server}' 

    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

    try:
        connection = pyodbc.connect(connection_string)
        return connection
        
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
        return None

@app.route('/api/getdata', methods=['GET'])
def getAllData():
    connection = connectToDB()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM employees"
            cursor.execute(query)
            rows = cursor.fetchall()
            data = []
            for row in rows:
                data.append({
                    'Employee ID': row[0],  
                    'Birth Date': row[1],  
                    'First Name': row[2], 
                    'Last Name': row[3], 
                    'Gender': row[4],
                    'Hire Date': row[5]
                })
            return jsonify(data)
        except pyodbc.Error as e:
            print(f"Error executing SQL query: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500
        finally:
            cursor.close()
            connection.close()

@app.route('/api/postdata', methods=['POST'])
def postData():
    connection = connectToDB()
    if connection:
        try:
            newEmployee = request.get_json()
        
            # Insert data to db
            cursor = connection.cursor()
            query = "INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (newEmployee['Employee No'], datetime.strptime(newEmployee['Birth Date'], '%Y-%m-%d'), newEmployee['First Name'], newEmployee['Last Name'], newEmployee['Gender'], datetime.strptime(newEmployee['Hire Date'],'%Y-%m-%d')))
            connection.commit()
            
            return jsonify({'message': 'Data added successfully'}), 201
        except pyodbc.Error as e:
            print(f"Error executing SQL query: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500
        finally:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
