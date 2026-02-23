from flask import Flask, request, render_template
app =  Flask(__name__, template_folder="templates",static_folder="satic")

@app.route("/")
def index():
    myvalue = "Neural Nine"
    myresults = 10+20
    mylist = [x for x in range(10)]
    return render_template("index.html",myvalue=myvalue,myresults=myresults,mylist=mylist)

@app.route("/other")
def other():
    some_text = "Some Text"
    return render_template("other.html",some_text=some_text)

@app.template_filter("reveres_string")
def reveres_string(s):
    return s[::-1]

@app.template_filter("repeat")
def repeat(s,times=2):
    return s * 5

@app.template_filter("alternate_case")
def alternate_case(s):
    return "".join(c.upper() if i%2 == 0 else c.lower() for i,c in enumerate(s))

if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5555)