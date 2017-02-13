from flask import Flask, make_response, request

app = Flask(__name__)

def transformation(text_file_contents):
        return text_file_contents.replace("=",",")

@app.route('/')
def form():
    return '<html><body><h1>Transform a file</h1><form action="/transform" method="post" enctype="multipart/form-data"><input type="file" name="data_file" /><input type="submit" /></form></body></html>'

@app.route("/transform", methods=['GET', 'POST'])
def transform_view():
    myfile = request.files['data_file']
    if not myfile:
        return "No input file given"
    file_contents = myfile.stream.read().decode()
    result = transform(file_contents)
    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    response.headers["Cache-Control"] = "must-revalidate"
    response.headers["Pragma"] = "must-revalidate"
    response.headers["Content-type"] = "application/csv"
    return response
