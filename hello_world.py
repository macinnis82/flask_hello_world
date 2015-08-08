from flask import Flask
from os import environ
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
  return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    return render_template('template.html', name=name.title())
    # return "Hello {}!".format(name.title())
    # html = """
    #     <h1>
    #         Hello {}!
    #     </h1>
    #     <p>
    #         Here's a picture of a kitten.  Awww...
    #     </p>
    #     <img src="http://placekitten.com/g/200/300">
    # """
    # return html.format(name.title())   
    
@app.route("/jedi/<fname>/<lname>")
def jedi_name(fname, lname):
  """
    Jedi name consists of the first three letters of your last name, 
    followed by the first two letters of your first name
  """
  return render_template('jedi.html', jname=(lname[:3] + fname[:2]).capitalize())  
  # html = """ <h1> Your Jedi name is {}! </h1> """
  # return html.format((lname[:3] + fname[:2]).capitalize())
  # return "Your jedi name is {}".format((lname[:3] + fname[:2]).lower())
  
if __name__ == "__main__":
  app.run(host=environ['IP'], 
    port=int(environ['PORT']))