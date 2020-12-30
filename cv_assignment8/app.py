from flask import Flask, redirect , url_for ,render_template

app = Flask(__name__)

#######################################################################################################
#1. Convert your personal website to a Flask project format:
#a. Create static folder, templates folder and app.py file
#b. Put all static files (images, ccs files, js files, etc.) inside static folder
#c. Put all html files inside templates folder
#d. Create a proper route to your root page (‘/’) as it was shown in the lecture
#e. Update all existing links (<a>, <script>, etc.) inside html files as it was shown
#in the lecture (hint: url_for() function)


@app.route('/')
def index2_func():
    #you get the name
    username = 'yazan'
    return render_template('cv.html')

##################################################################
###################################################################
#2. Create a new route called: ‘assignment8’. This route will lead to a new template
#(created by you) called ‘assignment8.html’. This template will, for instance,
#demonstrate your hobbies or/and preferences in music/art/films.
#3.
#c. Demonstrate at list one usage of conditions (if, else, elif)
#d. Demonstrate at list one usage of any kind of loops
#e. Demonstrate at list one usage of a block


@app.route('/assignment8')
def home_func():
    #extraction from DB
    user_from_DB={'firstname':'Yazan','lastname':'Yazbak','gender':'boy'}
    #user_from_DB= ''
    return render_template('Assignment8.html',
                           user=user_from_DB,
                           hoppies=['Surffing','Climbing', 'Teaching', 'Soccer', 'VolleyBall', 'Guitar'],
                           degrees=('B.Sc', 'M.Sc')

                           )

##################################################################
##################################################################
#3. Inside this new template (‘assignment8.html’)
#a. Use at list one filter applied on any variable
#upper lower litters

@app.route('/index')
def index_func():
    #you get the name
    username = 'yazan'
    return render_template('index2.html',
                           name=username, s_name='YaZbak')


##################################################################
##################################################################
#b. Demonstrate at list one usage of include function

@app.route('/about')
def about_func():
          return render_template('about.html')

##################################################################
##################################################################





if __name__ == '__main__':
    app.run(debug=True)

