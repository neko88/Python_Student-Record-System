from aifc import Error

import mysql

"""
Function to connect to mySQL server. 
"""
def connect_to_db(host_name, username, pswrd, rtn_cursor = False):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = username,
            password = pswrd
        )
        print("[** Successfully connected to MySQL database.**]")

    except Error as err:
        print(f"[**!! Error:" '{err} !!**]')

    if rtn_cursor is True:
        return connection.cursor()
    else:
        return connection
