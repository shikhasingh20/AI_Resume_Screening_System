from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/upload-resume")
def upload_resume():
    return render_template("upload_resume.html")

@app.route("/create-job")
def create_job():
    return render_template("create_job.html")

@app.route("/applicants")
def applicants():
    return render_template("applicants.html")

@app.route("/ranking")
def ranking():
    return render_template("ranking.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)