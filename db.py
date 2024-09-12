import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        Driver="{ODBC Driver 17 for SQL Server}",
        Server="DESKTOP-TNVFUGD\\SQLEXPRESS",
        Database="loan",
        Trusted_Connection="Yes",
    )
    return conn

def fetch_data_from_db(query):
        conn=get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows=cursor.fetchall()
        # Get column names from cursor description
        columns = [column[0] for column in cursor.description]
        # # Convert rows into a list of dictionaries
        data = [dict(zip(columns, row)) for row in rows]
        # row=cursor.fetchone()
        # columns = [column[0] for column in cursor.description]
        # # # Convert the row into a dictionary
        # result = dict(zip(columns, row)) if row else None
        # print(result)
        cursor.close()
        return data
# query1="SELECT * FROM temp_py"
# fetch_data_from_db(query1)

def execute_procedure(procedure, params=None):
    """
    Helper function to execute a stored procedure.
    """
    connection=get_db_connection()
    cursor=connection.cursor()
    query = f"EXEC {procedure}"
    if params:
        query += f" {params}"
    cursor.execute(query)
    connection.commit()