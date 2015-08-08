from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
  return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    # return "Hello {}!".format(name.title())
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())   
    
@app.route("/jedi/<fname>/<lname>")
def jedi_name(fname, lname):
  """
    Jedi name consists of the first three letters of your last name, 
    followed by the first two letters of your first name
  """
  html = """ <h1> Your Jedi name is {}! </h1> """
  return html.format((lname[:3] + fname[:2]).capitalize())
  # return "Your jedi name is {}".format((lname[:3] + fname[:2]).lower())
  
if __name__ == "__main__":
  app.run(host=environ['IP'], 
    port=int(environ['PORT']))