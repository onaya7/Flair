from flask import Blueprint , render_template


view = Blueprint('view', __name__ ,template_folder="templates", static_folder='static') 

@view.route('/' , methods=['POST', 'GET'])
def main():

    return render_template('index.html', title='Flair')

@view.route('/welcome' , methods=['POST', 'GET'])
def welcome():

    return render_template('welcome.html', title='Welcome')

@view.route('/signin' , methods=['POST', 'GET'])
def signin():

    return render_template('signin.html', title='Sign in')



@view.route('/home' , methods=['POST', 'GET'])
def home():
    
    return render_template('home.html', title='Home')