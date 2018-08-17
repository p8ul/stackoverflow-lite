#################
# imports 
#################

from flask import render_template, Blueprint

################
# config
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)  

################
# routes 
################


# use decorators to link the function to a url
@home_blueprint.route('/home', methods=['GET', 'POST'])
def home():
    error = None
    return render_template('index.html', error=error)
