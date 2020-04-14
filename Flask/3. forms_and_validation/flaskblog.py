# application code

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm 
app = Flask(__name__)  #name of module (name or main)

app.config['SECRET_KEY'] = '0fee3c1ee6b7b994e59471e7c8c72a7c'  #random characters from import secrets .token_hex(16)

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

@app.route("/register", methods=['GET','POST'])  #allows submit  
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')  
		return redirect(url_for('home'))  #redirect to homepage home function
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])  
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'ankur@blog.com' and form.password.data == 'ankur':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":  #if using Python
	app.run(debug=True)