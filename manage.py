### Flask app

# Author: P8ul Kinuthia
# https://github.com/p8ul

from app import create_app
app = create_app("config.BaseConfig")

if __name__ == "__main__":
    app = create_app("config.BaseConfig")
    app.run(debug=False)
