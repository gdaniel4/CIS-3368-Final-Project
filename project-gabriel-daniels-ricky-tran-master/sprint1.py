
import flask
from flask import jsonify
from flask import request
import DB
import random

# creates connection between aws database and backend
connection = DB.create_connection("cis3368-db.c91jggj8tkq9.us-east-2.rds.amazonaws.com", "admin", "!CougarData274894Base?", "cis3368db")

# passes __name__ to the flask class in order for app to know where to pull all of info from
app = flask.Flask(__name__)
app.config["DEBUG"] = True # shows error message in browser

# maps urls to functions 
@app.route('/', methods=['GET'])
def home():
    return "<h1> WELCOME TO OUR FIRST API! </h1>"

# shows all movies from movielist database
@app.route('/api/movies/all', methods=['GET'])
def moive_all():
    getTable = ("SELECT * FROM movielist")
    cursor = connection.cursor()
    cursor.execute(getTable)
    result = cursor.fetchall()
    return jsonify(result)

# shows all movies for a specific friend
@app.route('/api/friendmovies', methods=['GET'])
def friendmovies():
    request_data = request.get_json()
    firstname = request_data['firstname']
    lastname = request_data['lastname']
    # getting friendid from database
    friendid = ("SELECT friendid FROM friend WHERE firstname = '%s' and lastname = '%s'" %(firstname, lastname))
    friendidnum = int(friendid)
    getTable = ("SELECT * FROM movielist WHERE friendid = '%s'" %(friendidnum))
    cursor = connection.cursor()
    cursor.execute(friendid)
    cursor.execute(getTable)
    result = cursor.fetchall()
    return jsonify(result)
    
# shows all friends from friend db
@app.route('/api/friends/all', methods=['GET'])
def friends_all():
    getTable = ("SELECT * FROM friend")
    cursor = connection.cursor()
    cursor.execute(getTable)
    result = cursor.fetchall()
    return jsonify(result)

# add new friends into friend db
@app.route('/api/addfriend', methods=['POST'])
def add_friend():
    request_data = request.get_json()
    firstname = request_data['firstname']
    lastname = request_data['lastname']
    # ensures the first and last names entered are lowercase to match with names in db 
    lowfn = firstname.lower()
    lowln = lastname.lower()
    query = ("INSERT INTO friend (firstname, lastname) VALUES ('%s', '%s')" %(lowfn, lowln))
    DB.execute_query(connection, query)
    return 'POST REQUEST WORKED'

#adds a movie to the db based on freind name
@app.route('/api/addmovie', methods=['POST'])
def addmovie():
    request_data = request.get_json()
    firstname = request_data['firstname']
    lastname = request_data['lastname']
    # getting friendid from database
    friendid = ("SELECT friendid FROM friend WHERE firstname = '%s' and lastname = '%s'" %(firstname, lastname))
    movie1 = request_data['movie1']
    movie2 = request_data['movie2']
    movie3 = request_data['movie3']
    movie4 = request_data['movie4']
    movie5 = request_data['movie5']
    movie6 = request_data['movie6']
    movie7 = request_data['movie7']
    movie8 = request_data['movie8']
    movie9 = request_data['movie9']
    movie10 = request_data['movie10']
    query = "INSERT INTO movielist (friendid, movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10) VALUES ('{}', {}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(friendid, movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10)
    DB.execute_query(connection, query)
    return 'POST REQUEST WORKED'

#menu for when the user wants to find a random moveie. We want to go with this menu layout
#We might change how it works depending on the UI but this menu does work with postman
def deleteoption():
    menu = ('Options\n'
    'n - I have someone that is not participating \n'
    'r - I am ready for a random movie!\n')
    print(menu, end = '\n')

#this is to find a random movie
@app.route('/api/random', methods=['GET'])
def randomMovie():
    request_data = request.get_json()
    result = ''
    option = ''
    while option != 'r':
        deleteoption()
        option = request_data['option']
        #This is for the user to input who will not be participating    
        if option == 'n':
            firstname = request_data['firstname']
            lastname = request_data['lastname']
            # getting friendid from database
            friendid = ("SELECT friendid FROM friend WHERE firstname = '%s' and lastname = '%s'" %(firstname, lastname))
            query = ("DELETE FROM movielist where friendid = '%s'"%(friendid))
            DB.execute_query(connection, query)
        elif option == 'r':
            while result == '':
                #picks a random number between 1 and 10 for movie1 to movie10
                movienum = random.randint(1,10)
                #then selects a random row with with the randome movie number
                query = "select movie{} from movielist order by rand () limit 1".format(movienum)
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
                #for now we want the user to input 0 if they do not want to enter a movie
                #for example, they can enter 3 movie names and then enter 0 for movie4-movie10
                if result[0] == ('0',):
                    result = ''
                else:
                    return jsonify(result)

app.run()
