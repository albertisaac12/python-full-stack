from flask import Flask, request, render_template, url_for, redirect, url_for, Response,send_from_directory
app =  Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        print(password,username)

        if username == "abhi" and password == "password":
            return "Success",200
        else:
            return "Failure",403

@app.route("/file_upload", methods=["POST"])
def file_upload():
    file = request.files.get("file")
    # file.content_type()
    # file.read().decode()
    
    if not file:
        return {"error": "No file provided"}, 400
    
    from pypdf import PdfReader
    import io

    reader = PdfReader(io.BytesIO(file.read()))
    
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    return {"content": text}, 200 


@app.route("/convert_csv",methods=["POST"])
def convert_csv():
    import pandas as pd
    file = request.files.get("file")
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename = result.csv"
        }
    )
    return response

@app.route("/convert_csv_two",methods=["POST"])
def convert_csv_two():
    import pandas as pd
    import os
    import uuid
    file = request.files.get("file")
    df = pd.read_excel(file)

    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    
    filename = f"{uuid.uuid4()}.csv"
    df.to_csv(os.path.join("downloads",filename))

    return render_template(template_name_or_list="download.html",filename=filename)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(directory="downloads",path=filename,download_name="result.csv")

if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5555)