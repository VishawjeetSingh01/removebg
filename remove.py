from rembg import remove
import easygui
from PIL import Image 

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/edit", methods=["GET","POST"])

def edit():
    if request.method == "POST":
      inputPath = easygui.fileopenbox(title='select image file')
    outputPath = easygui.filesavebox(title='Save file to...')

    input = Image.open(inputPath)
    output = remove(input)
    output.save(outputPath)
    return render_template("index.html")


app.run()