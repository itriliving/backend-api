from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Handle CORS for cross-origin requests
host = os.getenv('MYSQL_HOST')
password = os.getenv('MYSQL_PASSWORD')
# MySQL connection configuration (for XAMPP defaults)
db_config = {
    'user': 'root',  # Default XAMPP MySQL username
    'password': password,  # Default XAMPP MySQL password (empty string)
    'host': host,
    'database': 'itri',  # Database name
}

# Connect to the MySQL database
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

def get_security_token():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT token FROM security LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        return result[0]  # Returning the token
    return None

# Check if the security token in the request headers matches the database
def validate_token(headers):
    token_in_db = get_security_token()
    token_in_headers = headers.get('Authorization')  # Assuming the token is passed as 'Authorization' header
    return token_in_db == token_in_headers

#first section
# POST method to overwrite data (title, title2, p1 to p4)
@app.route('/post_data0', methods=['POST'])
def post_data0():
    if not validate_token(request.headers):
        return jsonify({"error": "Invalid or missing security token"}), 403
    data = request.get_json()
    a1 = data.get('a1')
    a2 = data.get('a2')
    a3 = data.get('a3')
    a4 = data.get('a4')
    a5 = data.get('a5')

    if not (a1 and a2 and a3 and a4 and a5):
        return jsonify({"error": "Missing data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM first")

    insert_query = """
    INSERT INTO first (a1, a2, a3, a4 , a5)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (a1, a2, a3, a4 , a5))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Data posted successfully"})




# GET method to retrieve data (title, title2, p1 to p4)
@app.route('/get_data0', methods=['GET'])
def get_data0():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT a1, a2, a3, a4 , a5 FROM first LIMIT 1")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404









#second section
# POST method to overwrite data (title, title2, p1 to p4)
@app.route('/post_data1', methods=['POST'])
def post_data1():
    if not validate_token(request.headers):
        return jsonify({"error": "Invalid or missing security token"}), 403
    data = request.get_json()

    title = data.get('title')
    title2 = data.get('title2')
    p1 = data.get('p1')
    p2 = data.get('p2')
    p3 = data.get('p3')
    p4 = data.get('p4')

    if not (title and title2 and p1 and p2 and p3 and p4):
        return jsonify({"error": "Missing data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM second")

    insert_query = """
    INSERT INTO second (title, title2, p1, p2, p3, p4)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (title, title2, p1, p2, p3, p4))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Data posted successfully"})


# GET method to retrieve data (title, title2, p1 to p4)
@app.route('/get_data1', methods=['GET'])
def get_data1():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT title, title2, p1, p2, p3, p4 FROM second LIMIT 1")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404









#third section
@app.route('/post_data2', methods=['POST'])
def post_data2():
    if not validate_token(request.headers):
        return jsonify({"error": "Invalid or missing security token"}), 403
    data = request.get_json()

    # Extracting each field individually
    title = data.get('title')
    title2 = data.get('title2')
    p1 = data.get('p1')
    p2 = data.get('p2')
    p3 = data.get('p3')
    p4 = data.get('p4')
    p5 = data.get('p5')
    p6 = data.get('p6')
    p7 = data.get('p7')
    p8 = data.get('p8')
    p9 = data.get('p9')
    p10 = data.get('p10')
    p11 = data.get('p11')
    p12 = data.get('p12')
    p13 = data.get('p13')
    p14 = data.get('p14')
    p15 = data.get('p15')
    p16 = data.get('p16')
    p17 = data.get('p17')
    p18 = data.get('p18')
    p19 = data.get('p19')

    # Check if all required fields are provided
    if not (title and title2 and p1 and p2 and p3 and p4 and p5 and p6 and p7 and p8 and p9 and p10 and p11 and p12 and p13 and p14 and p15 and p16 and p17 and p18 and p19):
        return jsonify({"error": "Missing data"}), 400

    # Overwrite the table data by deleting any existing rows and inserting new data
    conn = get_db_connection()
    cursor = conn.cursor()

    # Step 1: Delete any existing data
    cursor.execute("DELETE FROM third")

    # Step 2: Insert new data (all p1 to p19)
    insert_query = """
    INSERT INTO third (title, title2, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (title, title2, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Data posted successfully"})


# GET method to retrieve data (title, title2, p1 to p19)
@app.route('/get_data2', methods=['GET'])
def get_data2():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Fetch the only row in the table
    cursor.execute("""
        SELECT title, title2, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19 
        FROM third LIMIT 1
    """)
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404







#fourth section
# POST method to overwrite data (title, title2, p1 to p4)
@app.route('/post_data3', methods=['POST'])
def post_data3():
    if not validate_token(request.headers):
        return jsonify({"error": "Invalid or missing security token"}), 403
    data = request.get_json()
    b1 = data.get('b1')
    b2 = data.get('b2')
    b3 = data.get('b3')
    b4 = data.get('b4')
    b5 = data.get('b5')

    if not (b1 and b2 and b3 and b4 and b5):
        return jsonify({"error": "Missing data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM fourth")

    insert_query = """
    INSERT INTO fourth (b1, b2, b3, b4 , b5)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (b1, b2, b3, b4 , b5))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Data posted successfully"})




# GET method to retrieve data (title, title2, p1 to p4)
@app.route('/get_data3', methods=['GET'])
def get_data3():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT b1, b2, b3, b4 , b5 FROM fourth LIMIT 1")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404






#fifth section
# POST method to overwrite data (title, title2, p1 to p4)
@app.route('/post_data4', methods=['POST'])
def post_data4():
    if not validate_token(request.headers):
        return jsonify({"error": "Invalid or missing security token"}), 403
    data = request.get_json()
    c1 = data.get('c1')
    c2 = data.get('c2')
    c3 = data.get('c3')
    c4 = data.get('c4')
    c5 = data.get('c5')
    c6 = data.get('c6')
    c7 = data.get('c7')
    c8 = data.get('c8')
    c9 = data.get('c9')
    c10 = data.get('c10')
    c11 = data.get('c11')

    if not (c1 and c2 and c3 and c4 and c5  and c6 and c7 and c8 and c9 and c10 and c11  ):
        return jsonify({"error": "Missing data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM fifth")

    insert_query = """
    INSERT INTO fifth (c1, c2, c3, c4 , c5, c6, c7, c8, c9, c10, c11)
    VALUES (%s, %s, %s, %s, %s , %s , %s , %s , %s , %s , %s)
    """
    cursor.execute(insert_query, (c1, c2, c3, c4 , c5, c6, c7, c8, c9, c10, c11))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Data posted successfully"})




# GET method to retrieve data (title, title2, p1 to p4)
@app.route('/get_data4', methods=['GET'])
def get_data4():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT c1, c2, c3, c4 , c5, c6, c7, c8, c9, c10, c11 FROM fifth LIMIT 1")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404











#sixth section
# POST method to overwrite data (title, title2, p1 to p4)
@app.route('/post_data5', methods=['POST'])
def post_data5():
    if not validate_token(request.headers):
        return jsonify({"error": "Invalid or missing security token"}), 403
    data = request.get_json()
    d1 = data.get('d1')
    d2 = data.get('d2')
    d3 = data.get('d3')
    d4 = data.get('d4')


    if not (d1 and d2 and d3 and d4):
        return jsonify({"error": "Missing data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sixth")

    insert_query = """
    INSERT INTO sixth (d1, d2, d3, d4)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (d1, d2, d3, d4))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Data posted successfully"})




# GET method to retrieve data (title, title2, p1 to p4)
@app.route('/get_data5', methods=['GET'])
def get_data5():
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT d1, d2, d3, d4 FROM sixth LIMIT 1")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404










#seventh section
# POST method to overwrite data (e1 to e9)
@app.route('/post_data6', methods=['POST'])
def post_data6():
    if not validate_token(request.headers):
        return jsonify({"error": "Invalid or missing security token"}), 403
    data = request.get_json()
    e1 = data.get('e1')
    e2 = data.get('e2')
    e3 = data.get('e3')
    e4 = data.get('e4')
    e5 = data.get('e5')
    e6 = data.get('e6')
    e7 = data.get('e7')
    e8 = data.get('e8')
    e9 = data.get('e9')

    if not (e1 and e2 and e3 and e4 and e5 and e6 and e7 and e8 and e9):
        return jsonify({"error": "Missing data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM seventh")

    insert_query = """
    INSERT INTO seventh (e1, e2, e3, e4 , e5, e6, e7, e8, e9)
    VALUES (%s, %s, %s, %s, %s , %s , %s , %s , %s)
    """
    cursor.execute(insert_query, (e1, e2, e3, e4 , e5, e6, e7, e8, e9))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Data posted successfully"})



# GET method to retrieve data (title, title2, p1 to p4)
@app.route('/get_data6', methods=['GET'])
def get_data6():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT e1, e2, e3, e4 , e5, e6, e7, e8, e9 FROM seventh LIMIT 1")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404







#eighth section
# POST method to overwrite data (f1 to f16)
@app.route('/post_data7', methods=['POST'])
def post_data7():
    if not validate_token(request.headers):
        return jsonify({"error": "Invalid or missing security token"}), 403
    data = request.get_json()
    f1 = data.get('f1')
    f2 = data.get('f2')
    f3 = data.get('f3')
    f4 = data.get('f4')
    f5 = data.get('f5')
    f6 = data.get('f6')
    f7 = data.get('f7')
    f8 = data.get('f8')
    f9 = data.get('f9')
    f10 = data.get('f10')
    f11 = data.get('f11')
    f12 = data.get('f12')
    f13 = data.get('f13')
    f14 = data.get('f14')
    f15 = data.get('f15')
    f16 = data.get('f16')
    if not (f1 and f2 and f3 and f4 and f5 and f6 and f7 and f8 and f9 and f10 and f11 and f12 and f13 and f14 and f15 and f16):
        return jsonify({"error": "Missing data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM eighth")
    insert_query = """
    INSERT INTO eighth (f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Data posted successfully"})




@app.route('/get_data7', methods=['GET'])
def get_data7():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16 FROM eighth LIMIT 1")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404






if __name__ == '__main__':
    app.run(debug=True)