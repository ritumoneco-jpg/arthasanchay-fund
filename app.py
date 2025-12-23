from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# ================= EMAIL CONFIG =================
EMAIL_ADDRESS = "samarthagrawal252525@gmail.com"
EMAIL_PASSWORD = "gsgqhnlueomxnsrd"   # Gmail App Password (no spaces)

# ================= ROUTES =================

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/approach")
def approach():
    return render_template("approach.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/compliance")
def compliance():
    return render_template("compliance.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            message = request.form.get("message")

            msg = EmailMessage()
            msg["Subject"] = "New Enquiry - Arthasanchay"
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = EMAIL_ADDRESS

            msg.set_content(f"""
New Contact Enquiry

Name: {name}
Email: {email}

Message:
{message}
""")

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

            # SUCCESS
            return render_template("contact.html", success=True)

        except Exception as e:
            print("EMAIL ERROR:", e)
            return render_template("contact.html", error=True)

    return render_template("contact.html")

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)
    