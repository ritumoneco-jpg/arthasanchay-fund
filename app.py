from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# ===== EMAIL CONFIG =====
EMAIL_ADDRESS = "samarthagrawal2525@gmail.com"
EMAIL_PASSWORD = "gsgqhnlueomxnsrd"   # Gmail App Password (no spaces)

# ===== ROUTES =====

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/approach")
def approach():
    return render_template("approach.html")

@app.route("/compliance")
def compliance():
    return render_template("compliance.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        try:
            msg = EmailMessage()
            msg["Subject"] = "New Enquiry - Arthasanchay"
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

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

        except Exception as e:
            print("EMAIL ERROR:", e)  # for Render logs
            return redirect(url_for("contact"))

        return redirect(url_for("contact"))

    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
    