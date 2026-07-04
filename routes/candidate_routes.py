from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    flash
)

from database.db import db

candidate = Blueprint(
    "candidate",
    __name__
)


# ==========================================
# Login Required
# ==========================================

def login_required():

    if "user_id" not in session:

        flash(
            "Please login first.",
            "warning"
        )

        return False

    return True


# ==========================================
# Candidate Dashboard
# ==========================================

@candidate.route("/candidate/dashboard")
def dashboard():

    if not login_required():
        return redirect("/login")

    user = db.fetch_one(

        """
        SELECT *
        FROM users
        WHERE id=%s
        """,

        (
            session["user_id"],
        )

    )

    total_applications = db.fetch_one(

        """
        SELECT COUNT(*) AS total
        FROM applications
        WHERE user_id=%s
        """,

        (
            session["user_id"],
        )

    )

    return render_template(

        "dashboard.html",

        user=user,

        total=total_applications["total"]

    )


# ==========================================
# Profile
# ==========================================

@candidate.route("/candidate/profile")
def profile():

    if not login_required():
        return redirect("/login")

    user = db.fetch_one(

        """
        SELECT *
        FROM users
        WHERE id=%s
        """,

        (
            session["user_id"],
        )

    )

    return render_template(

        "profile.html",

        user=user

    )


# ==========================================
# My Applications
# ==========================================

@candidate.route("/candidate/applications")
def applications():

    if not login_required():
        return redirect("/login")

    applications = db.fetch(

        """
        SELECT

            jobs.title,

            applications.ats_score,

            applications.status,

            applications.applied_at

        FROM applications

        JOIN jobs

        ON applications.job_id = jobs.id

        WHERE applications.user_id=%s

        ORDER BY applications.applied_at DESC

        """,

        (
            session["user_id"],
        )

    )

    return render_template(

        "applications.html",

        applications=applications

    )


# ==========================================
# ATS Score
# ==========================================

@candidate.route("/candidate/ats")
def ats():

    if not login_required():
        return redirect("/login")

    scores = db.fetch(

        """
        SELECT

            jobs.title,

            applications.ats_score

        FROM applications

        JOIN jobs

        ON jobs.id=applications.job_id

        WHERE applications.user_id=%s

        """,

        (
            session["user_id"],
        )

    )

    return render_template(

        "ranking.html",

        scores=scores

    )