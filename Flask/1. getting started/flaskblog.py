from flask import Flask
app = Flask(__name__)  #name of module (name or main)


@app.route("/")  #route to go to pages #route decorators
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"  #html heading 1 tags


@app.route("/about")  
def about():
    return "<h1>About Page</h1>"  


if __name__ == "__main__":  #if using Python
	app.run(debug=True)