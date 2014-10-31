from flask import Flask, render_template

def get_ads():

  # Useful imports
  import re
  import urllib3
  import random

  # Static values
  BASE_PAGE = "http://apod.nasa.gov/apod/"
  IMAGE_STORED = "templates/apod.jpg"
  #BACKUP_URL = "http://thoselondonstudents.files.wordpress.com/2013/07/dsc_0500.jpg"
                

  BACKUP_URL = ["https://lh4.googleusercontent.com/-Y8gMy_GeFNM/VFOcLtFapPI/AAAAAAAAAEY/HdicNXq4yH0/w1598-h899-no/P1030294.jpg"
,"https://lh6.googleusercontent.com/-soRMKsuGS7c/VFOcHveKmAI/AAAAAAAAAEM/u4SCIp3gX2o/w1598-h899-no/P1030253.jpg"
,"https://lh3.googleusercontent.com/-iu_9L35Ong0/VFOb_rpfIKI/AAAAAAAAAD4/1b9KD9zzCv0/w1598-h899-no/P1030193%2B-%2BVersion%2B2.jpg"
,"https://lh5.googleusercontent.com/-ZjrwsMlhoKQ/VFOb15W1iII/AAAAAAAAAEs/lcH_S9Pb4gs/w1598-h700-no/P1030187.jpg"
  #BACK_URLS = ["one.jpg", "two.jpg"]

  # Obtain the webpage
  http = urllib3.PoolManager()
  html = http.request('GET', BASE_PAGE).data

  # RegEx that looks for the image name
  pattern = re.compile("<IMG SRC=\"image/.*\.jpg")
  search = re.search(pattern, html)

  # Just in case it does not match pattern correctly
  try:
    image_link = search.group().replace("<IMG SRC=\"", "")
    ads_url = "{0}{1}".format(BASE_PAGE, image_link)
  except:
    #ads_url = BACKUP_URL
    ads_url = BACKUP_URL[0]

  # Add some flare
  rand = random.random()
  if rand > 0.5:
    rand_index = int(random.random()*len(BACK_URL))
    #ads_url = BACKUP_URL
    ads_url = BACKUP_URL[rand_index]


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
