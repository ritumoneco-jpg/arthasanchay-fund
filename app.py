from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "secretkey"

# ================= MAIL CONFIG =================
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "samarthagrawal252525@gmail.com"
app.config["MAIL_PASSWORD"] = "gsgqhnlueomxnsrd"
app.config["MAIL_DEFAULT_SENDER"] = "samarthagrawal252525@gmail.com"

mail = Mail(app)

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

            msg = Message(
                subject="New Contact Form Submission",
                recipients=["samarthagrawal252525@gmail.com"],
                body=f"""
Name: {name}
Email: {email}

Message:
{message}
"""
            )

            mail.send(msg)
            flash("Thank you for your response!", "success")

        except Exception as e:
            print(e)
            flash("Something went wrong. Please try again.", "error")

        return redirect(url_for("contact"))

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)