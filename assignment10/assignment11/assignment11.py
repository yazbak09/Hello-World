from flask import Blueprint, render_template, redirect, url_for, request, session
import mysql.connector
from flask import jsonify

assignment11 = Blueprint('assignment11', __name__,
                         static_folder='static',
                         static_url_path='/assignment11',
                         template_folder='templates'
                         )


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='myworld',
                                         database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# user list

@assignment11.route('/assignment11/<users>')
def get_userlist(users):
    query = "SELECT * FROM users"
    query_result = interact_db(query, 'fetch')
    if len(query_result) == 0:
        return jsonify({
            'success': 'False',
            "data": []
        })
    else:
        return jsonify({
            'success': 'True',
            "data": [query_result]
        })
    return f'Users: {query_result}'


# to chose user email from db
@assignment11.route('/assignment11', defaults={'email': 'yazzaaaaa@psws.com'})
@assignment11.route('/assignment11/users/<email>')
def get_user(email):
   # if request.method == "GET":
        query = "SELECT * FROM users  WHERE email='%s';" % email
        query_result = interact_db(query, 'fetch')
        if len(query_result) == 0:
            return jsonify({
                'success': 'False',
                "data": []
            })
        else:
            return jsonify({
                'success': 'True',
                "data": [query_result]
            })
 #   if request.method == "POST":
        return f'Users: {query_result}'
