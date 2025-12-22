from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# ---------- Your Gmail credentials ----------
EMAIL_ADDRESS = "samarthagrawal252525@gmail.com"  # the email where you want to receive enquiries
EMAIL_PASSWORD = "ffjb wtfd hjlo rlnc"   # use app password if 2FA is on

# ---------- HOME PAGE ----------
@app.route('/')
def home():
    return render_template('home.html')  # make sure this is your home page filename

# ---------- ABOUT PAGE ----------
@app.route('/about')
def about():
    return render_template('about.html')

# ---------- APPROACH PAGE ----------
@app.route('/approach')
def approach():
    return render_template('approach.html')

# ---------- COMPLIANCE PAGE ----------
@app.route('/compliance')
def compliance():
    return render_template('compliance.html')

# ---------- TEAM PAGE ----------
@app.route('/team')
def team():
    return render_template('team.html')

# ---------- CONTACT PAGE ----------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        # Prepare email
        msg = EmailMessage()
        msg["Subject"] = "New Enquiry - Arthasanchay Growth Fund"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg.set_content(
            f"""
New enquiry received:

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
            """
        )

        # Send email
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
        except Exception as e:
            print("Error sending email:", e)

        # Redirect to contact page after sending
        return redirect(url_for("contact"))

    return render_template("contact.html")

# ---------- RUN APP ----------

import os

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    