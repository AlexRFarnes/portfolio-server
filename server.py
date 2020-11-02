from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_database(data):
    with open("database.txt", "a") as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("database.csv", "a", newline='') as csvfile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thanks.html")
        except:
            return "Data was not saved to the Database"
    else:
        return "Something went wrong"
