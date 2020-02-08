from flask import Flask
import db

# Initialize the app
app = Flask(__name__)

# routings plus functionalities

# home route
@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb atlas!"

@app.route('/addUser/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % escape(subpath)

#test to insert data to the data base
@app.route("/addPerformanceData")
def test():
    db.user_collection.insert_one({"name": "John"})
    return "Connected to the data base!"
    
# serve the files on localhost port
if __name__ == '__main__':
    app.run(port=8000)