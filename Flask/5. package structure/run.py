# flaskblog package, app in __init__.py file
from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)