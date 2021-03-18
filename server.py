from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello flask is successful"


@app.route("/<string:page_name>")
def page(page_name):
    return render_template(page_name)


def data_to_write(data):
    with open("webserver/database1.txt", mode="a") as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = database.write(f" \n Name : {name} , \n Email: {email} , \n Message: {message} ")


def write_as_csv(data):
    with open("webserver/database.csv", newline='', mode='a' ) as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',  quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])



@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        data_to_write(data)
        write_as_csv(data)
        return redirect("/generic.html")

    else:
        return "something went wrong"