from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="20033011",
    database="flask"
)

# @app.route('/getTables', methods=['GET'])
# def get_tables():
#     cursor = con.cursor()
#     cursor.execute("SHOW TABLES")
#     tables = cursor.fetchall()
#     cursor.close()
#     table_names = [table[0] for table in tables]
#     return jsonify ({'tables': table_names}), 200

# add Students
@app.route('/add', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data['name']
    email = data['email']
    department = data['department']
    cursor = con.cursor()
    cursor.execute("INSERT INTO students (name, email, department) VALUES (%s, %s, %s)", (name, email, department))
    con.commit()
    cursor.close()
    return jsonify({"message": "User created"}), 201

# view all 
@app.route('/view', methods=['GET'])
def view_students():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    students_list = []
    for student in students:
        students_list.append({
            'id': student[0],
            'name': student[1],
            'email': student[2],
            'department': student[3]
        })
    return jsonify(students), 200






if __name__ == '__main__':
    app.run(debug=True)
