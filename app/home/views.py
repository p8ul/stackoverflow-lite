#################
# imports 
#################

from flask import Blueprint, render_template
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
    return render_template('home.html')
    # return redirect("/api/v1/questions", code=302)
