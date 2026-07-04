from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for
)

from database.db import db

recruiter = Blueprint(
    "recruiter",
    __name__
)


# =====================================
# Helper
# =====================================

def recruiter_required():

    if "user_id" not in session:
        return False

    return session.get("role") == "recruiter"


# =====================================
# Dashboard
# =====================================

@recruiter.route("/recruiter/dashboard")
def dashboard():

    if not recruiter_required():
        flash("Unauthorized access.", "danger")
        return redirect(url_for("auth.login"))

    total_jobs = db.fetch_one(
        "SELECT COUNT(*) AS total FROM jobs WHERE recruiter_id=%s",
        (session["user_id"],)
    )

    total_candidates = db.fetch_one(
        "SELECT COUNT(*) AS total FROM applications"
    )

    return render_template(
        "recruiter_dashboard.html",
        total_jobs=total_jobs["total"],
        total_candidates=total_candidates["total"]
    )


# =====================================
# Create Job
# =====================================

@recruiter.route("/recruiter/create-job", methods=["GET", "POST"])
def create_job():

    if not recruiter_required():
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        skills = request.form["skills"]

        db.execute(

            """
            INSERT INTO jobs
            (title, description, skills, recruiter_id)

            VALUES
            (%s,%s,%s,%s)
            """,

            (
                title,
                description,
                skills,
                session["user_id"]
            )

        )

        flash("Job Created Successfully", "success")

        return redirect(url_for("recruiter.jobs"))

    return render_template("create_job.html")


# =====================================
# View Jobs
# =====================================

@recruiter.route("/recruiter/jobs")
def jobs():

    if not recruiter_required():
        return redirect(url_for("auth.login"))

    jobs = db.fetch(

        """
        SELECT *
        FROM jobs

        WHERE recruiter_id=%s

        ORDER BY created_at DESC
        """,

        (
            session["user_id"],
        )

    )

    return render_template(
        "jobs.html",
        jobs=jobs
    )


# =====================================
# Delete Job
# =====================================

@recruiter.route("/recruiter/delete-job/<int:id>")
def delete_job(id):

    if not recruiter_required():
        return redirect(url_for("auth.login"))

    db.execute(

        """
        DELETE FROM jobs
        WHERE id=%s
        """,

        (
            id,
        )

    )

    flash("Job Deleted", "success")

    return redirect(url_for("recruiter.jobs"))


# =====================================
# Applicants
# =====================================

@recruiter.route("/recruiter/applicants/<int:job_id>")
def applicants(job_id):

    if not recruiter_required():
        return redirect(url_for("auth.login"))

    applicants = db.fetch(

        """
        SELECT

            users.fullname,

            users.email,

            resumes.file_name,

            applications.ats_score,

            applications.status

        FROM applications

        JOIN users

        ON users.id=applications.user_id

        LEFT JOIN resumes

        ON resumes.user_id=users.id

        WHERE applications.job_id=%s

        ORDER BY applications.ats_score DESC

        """,

        (
            job_id,
        )

    )

    return render_template(

        "applicants.html",

        applicants=applicants

    )