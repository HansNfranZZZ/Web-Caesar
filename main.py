from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
       
       <form method="post">
        <label for="rot">
            Rotate by:
            <input type="text" name="rot" value="0"/>
            

            
        </label>

        <br>
       
         <label for="text">
            
            <textarea>{0} </textarea>
            
        <br>
        
         <input type="submit" value="Submit"/>
         

         </form>
    

    </body>
</html>


"""

@app.route("/", methods=['POST'])
def encrypt(text,rot):
    text = request.form["text"]
    rot = request.form["rot"]
    rot = int(rot)
    encrypted = rotate_string(text,rot)

    return str("<h1>") + form.format(encrypted) + str("</h1>")


@app.route("/")
def index():
    return form.format("")

app.run()