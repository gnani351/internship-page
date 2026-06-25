from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# ================= EMAIL CONFIG =================
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gnanig809@gmail.com'
app.config['MAIL_PASSWORD'] = 'acac tgkb dxar aaoy'  # NOT normal password
app.config['MAIL_DEFAULT_SENDER'] = 'gnanig809@gmail.com'

mail = Mail(app)

# ================= UPLOAD FOLDER =================
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ================= ROUTES =================
@app.route('/')
def home():
    return render_template('form.html')


@app.route('/register', methods=['POST'])
def register():

    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    dob = request.form['dob']
    gender = request.form['gender']
    college = request.form['college']
    degree = request.form['degree']
    branch = request.form['branch']
    year = request.form['year']
    domain = request.form['domain']

    # Resume upload
    resume = request.files['resume']
    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume.filename)
    resume.save(resume_path)

    # ================= EMAIL CONTENT =================
    msg = Message(
        subject="New Internship Application Received",
        recipients=["gnanig809@gmail.com"]
    )

    msg.body = f"""
New Internship Application:

Name: {fullname}
Email: {email}
Phone: {phone}
DOB: {dob}
Gender: {gender}
College: {college}
Degree: {degree}
Branch: {branch}
Year: {year}
Domain: {domain}
"""

    # Attach resume
    with open(resume_path, "rb") as f:
        msg.attach(resume.filename, "application/octet-stream", f.read())

    mail.send(msg)

    return render_template('thank.html')

if __name__ == '__main__':
    app.run(debug=True)