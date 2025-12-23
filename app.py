
from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Replace with your Gmail and app password (no spaces)
EMAIL_ADDRESS = "samarthagrawal252525@gmail.com"
EMAIL_PASSWORD = "nfdwahhxpyldlzop"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/approach')
def approach():
    return render_template('approach.html')

@app.route('/compliance')
def compliance():
    return render_template('compliance.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        # Create email
        msg = EmailMessage()
        msg["Subject"] = "New Enquiry - Arthsanchay Growth Fund"
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

        # Send email using Gmail SMTP
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
        except Exception as e:
            print("Error sending email:", e)

        return redirect(url_for("contact"))

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
    