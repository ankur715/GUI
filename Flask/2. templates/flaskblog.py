# application code

from flask import Flask, render_template, url_for
app = Flask(__name__)  #name of module (name or main)

posts = [
		{
			'author': 'Bob Smith',
			'title': 'Blog Post 1',
			'content': 'First post content',
			'date_posted': 'April 10, 2020'
		},
		{
			'author': 'Jack Will',
			'title': 'Blog Post 2',
			'content': 'Second post content',
			'date_posted': 'May 10, 2020'
		}
]

@app.route("/")  #route to go to pages #route decorators
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)  
    #pass posts in home template
    #since no title, go to else condition

@app.route("/about")  
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":  #if using Python
	app.run(debug=True)