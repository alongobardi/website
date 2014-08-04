from flask import Flask, render_template

def get_ads():

  # Useful imports
  import re
  import urllib2
  import random

  # Static values
  BASE_PAGE = "http://apod.nasa.gov/apod/"
  IMAGE_STORED = "templates/apod.jpg"
  IMAGE_LOG = "templates/last_image.log"
  BACKUP_URL = "http://thoselondonstudents.files.wordpress.com/2013/07/dsc_0500.jpg"

  # Obtain the webpage
  response = urllib2.urlopen(BASE_PAGE)
  html = response.read()

  # RegEx that looks for the image name
  pattern = re.compile("<IMG SRC=\"image/.*\.jpg")
  search = re.search(pattern, html)

  # Just in case it does not match pattern correctly
  try:
    image_link = search.group().replace("<IMG SRC=\"", "")
    ads_url = "{0}{1}".format(BASE_PAGE, image_link)
  except:
    ads_url = BACKUP_URL

  # Add some flare
  rand = random.random()
  if rand > 0.5:
    ads_url = BACKUP_URL

  return ads_url


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', ads_url=get_ads())

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
