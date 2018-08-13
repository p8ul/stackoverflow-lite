#################
# imports 
#################

from flask import render_template, Blueprint, \
    request, flash, redirect, url_for

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
@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    error = None
    return render_template('index.html', error=error)
