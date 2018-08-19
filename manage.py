# Flask app

# Author: P8ul
# https://github.com/p8ul

from app import create_app
app = create_app("config.BaseConfig")

if __name__ == "__main__":
    app.run(debug=True)
