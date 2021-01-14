from flask import Flask, render_template, url_for, request, session, redirect

app = Flask(__name__)



@app.route('/')
def main_cv():
    return render_template('cv.html')


@app.route('/contacts')
def contacts():
    return render_template('JSON.html')


@app.route('/Assignment9', methods=['GET', 'POST'])
def ass_9():
    res = ''
    list = []
    users = ['Michael Lawson', 'Lindsay Ferguson', 'Tobias Funke', 'Byron Fields', 'George Edwards', 'Rachel Howell']
    emails = {'Michael Lawson': 'michael.lawson@reqres.in',
              'Lindsay Ferguson': 'lindsay.ferguson@reqres.in',
              'Tobias Funke': 'tobias.funke@reqres.in',
              'Byron Fields': 'byron.fields@reqres.in',
              'George Edwards': 'george.edwards@reqres.in',
              'Rachel Howell': 'rachel.howell@reqres.in'}
    if request.method == 'GET':

        if 'name' in request.args:
            res = request.args['name']
            answer_U = [i for i in users if res in i]
            for v in answer_U:
                list.append(emails[str(v)])
            return render_template('assignment99.html', name=answer_U, email=list)
    if request.method == 'POST':

        return render_template('assignment99.html', session = 'TRUE' ,username = 'name' )
    return render_template('assignment99.html')



if __name__ == '__main__':
    app.run()



#
#
    # username=''
    # second_name = ''
    #
    # if request.method == 'POST':
    #
    #     username = request.form['username']
    #     session['logged_in'] = True
    #     session['username'] = username
    #
    #
    #
    # if request.method == 'GET':
    #     if 'second_name' in request.args:
    #          second_name = request.args['second_name']
    #
    # return render_template('assignment99.html',
    #                        request_method=request.method,
    #                        username=username,
    #                        second_name=second_name)
    #

#
#
#
#
# @app.route('/catalog')
# def catalog_func():
#
#
#     if 'id' in request.args:
#         curr_id = request.args['id']
#         name=request.args['name']
#         return f'Username:{name},The id of product:{curr_id} '
#     return 'in Catalog'
#
#
#
#
#
#
#
#
# ##################################################################
# ##################################################################
#
# @app.route('/about')
# def about_func():
#           return render_template('about.html')
#
#
#



if __name__ == '__main__':

            app.run(debug=True)

