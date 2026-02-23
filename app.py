from flask import Flask, request, render_template, url_for, redirect, url_for
app =  Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/other_but_not_other")
def other():
    some_text = "Some Text"
    return render_template("other.html",some_text=some_text)


@app.route("/redirect_endpoint")
def redirect_endpoint():
    return redirect(url_for("other"))


# Filters

@app.template_filter("reverse_string")
def reverse_string(s):
    return s[::-1]

@app.template_filter("repeat")
def repeat(s, times=2):
    return s * times

@app.template_filter("alternate_case")
def alternate_case(s):
    return "".join(c.upper() if i%2 == 0 else c.lower() for i,c in enumerate(s))

if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5555)