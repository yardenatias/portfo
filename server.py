from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)  # name of our app
print(__name__)


@app.route('/')  # decorator
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')  # decorator
def pages(page_name):
    # render looks in templates directory auto
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])  # get-send data post-save data
def submit_form():
    if request.method == 'POST':
        try:  # WE WANT TO SAVE THE USER'S DATA
            data = request.form.to_dict()  # so we get all the data in dict
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to db'
    else:
        return 'something went wrong,try again'


# def write_to_file(data):
#     with open("database.txt", mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open("database.csv", mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
