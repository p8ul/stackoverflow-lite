# Flask app

# Author: P8ul
# https://github.com/p8ul

from app import create_app
app = create_app("config.ProductionConfig")

if __name__ == "__main__":
    app = create_app("config.BaseConfig")
    app.run(debug=True)
