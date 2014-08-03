from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/interests/')
def interests():
	return render_template('interests.html')

@app.route('/publications/')
def publications():
	return render_template('publications.html')

@app.route('/cv/')
def cv():
	return render_template('cv.html')

@app.route('/contact/')
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
  app.run()
