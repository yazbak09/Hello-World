from flask import Flask, render_template, url_for, redirect, session, request, Blueprint
import mysql.connector

assignment10 = Flask(__name__)

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')


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


@assignment10.route('/assignment10')
def users():
    query = "SELECT * FROM users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('/users.html', users=query_result)


@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        query = "INSERT INTO users(first_name,last_name,email,password) VALUES ('%s','%s','%s','%s')" % (
        name, lastname, email, password)
        interact_db(query, query_type='commit')
        return redirect('/assignment10')

    return render_template('assignment10.html')


@assignment10.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        u_id = request.form['id']
        u_email = request.form['email']

        query = "UPDATE users SET  email = '%s' WHERE id='%s'" % (u_email, u_id)
        interact_db(query, query_type='commit')
        return redirect('/assignment10')
    return render_template('assignment10.html')


@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        user_id = request.args['id']
        query = "DELETE FROM users WHERE id='%s';" % user_id
        interact_db(query, query_type='commit')
        return redirect('/assignment10')
    return render_template('assignment10.html')
