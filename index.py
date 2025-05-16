from flask import Flask, jsonify 
import mysql.connector

app = Flask(__name__)

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="20033011",
    database="flask"
)

@app.route('/getTables', methods=['GET'])
def get_tables():
    cursor = con.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    cursor.close()
    table_names = [table[0] for table in tables]
    return jsonify ({'tables': table_names}), 200

if __name__ == '__main__':
    app.run(debug=True)
