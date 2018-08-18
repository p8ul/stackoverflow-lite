#################
# imports 
#################

from flask import Blueprint, redirect
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
    return redirect("/api/v1/questions", code=302)
    # return render_template('index.html', error=error)
