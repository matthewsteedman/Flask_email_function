from flask import render_template, Flask, request

import smtplib

app = Flask(__name__)


@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/about/')
def about(name=None):
    return render_template('about.html', name=name)


@app.route('/portfolio/')
def portfolio(name=None):
    return render_template('portfolio.html', name=name)


@app.route('/contact/')
def contact(name=None):
    return render_template('contact.html', name=name)


@app.route('/send-email/', methods=['POST'])
def email_funct():
    # print('button clicked')
    user_email = request.form['email_add']
    user_password = request.form['user_psswd']
    user_sub = request.form['sub']
    user_mes = request.form['mes']

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        sender_email_id = user_email
        receiver_email_id = 'msteedman77@gmail.com'

        s.starttls()

        s.login(sender_email_id, user_password)
        s.sendmail(sender_email_id, receiver_email_id, user_sub, user_mes)

        s.quit()
    except:
        print("You have received an error")
    finally:
        print("email sent")

    return "Email Sent"
