from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def view_photos():
    return ''' 
         <h1>Upload new File </h1>
        <form method="post" action="/upload-photos"
            enctype="multipart/form-data">
            <input type="file" name="photos" multiple >  
            <input type="submit" >  
        </form>
        ''' 

@app.route("/upload-photos", methods=["POST"])
def upload_photos():
    filenames = ""
    for file in request.files.getlist("photos"):
            filenames += file.filename + " "
    return "<p>Uploaded: {}</p>".format(filenames)