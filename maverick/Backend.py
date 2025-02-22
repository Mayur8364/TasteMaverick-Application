import mysql.connector

# Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'Mayur@2064',  # Replace with your MySQL password
    'database': 'Tastemaverick'  # Replace with your database name
}

def store_and_recommend(data):
    """
    Store user data in the database and recommend a dish based on mood.
    """
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert user data
        insert_query = """
            INSERT INTO user_data (name, age, weight, height, gender, mobile_no, mood)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            data["name"], data["age"], data["weight"], data["height"],
            data["gender"], data["mobile_no"], data["mood"]
        ))
        conn.commit()

        # Recommend a dish based on mood
        select_query = """
            SELECT dish_name FROM dishes WHERE mood = %s ORDER BY RAND() LIMIT 1
        """
        cursor.execute(select_query, (data["mood"],))
        recommendation = cursor.fetchone()

        cursor.close()
        conn.close()

        if recommendation:
            return recommendation[0]
        else:
            return "No matching dish found."

    except Exception as e:
        return f"Error: {str(e)}"
