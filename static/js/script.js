console.log("AI Resume Screening System Loaded");

/* ==========================
   Password Validation
========================== */

function validatePassword() {

    let password =
        document.getElementById("password");

    if (!password) return;

    if (password.value.length < 6) {

        password.style.border =
            "2px solid red";

    } else {

        password.style.border =
            "2px solid green";
    }
}

/* ==========================
   Confirm Password Check
========================== */

function checkPasswordMatch() {

    let password =
        document.getElementById("password");

    let confirmPassword =
        document.getElementById("confirm_password");

    if (!password || !confirmPassword) return;

    if (
        confirmPassword.value !== "" &&
        password.value !== confirmPassword.value
    ) {

        confirmPassword.style.border =
            "2px solid red";

    } else {

        confirmPassword.style.border =
            "2px solid green";
    }
}

/* ==========================
   Resume Upload Validation
========================== */

function validateResume() {

    let resume =
        document.getElementById("resume");

    if (!resume) return;

    let file =
        resume.files[0];

    if (!file) return;

    let extension =
        file.name.split(".").pop().toLowerCase();

    if (
        extension !== "pdf"
    ) {

        alert(
            "Only PDF resumes are allowed."
        );

        resume.value = "";
    }
}

/* ==========================
   Preview Resume File Name
========================== */

function showFileName() {

    let resume =
        document.getElementById("resume");

    let filename =
        document.getElementById("filename");

    if (!resume || !filename) return;

    if (resume.files.length > 0) {

        filename.innerHTML =
            "Selected File: " +
            resume.files[0].name;
    }
}

/* ==========================
   Search Applicant Table
========================== */

function searchApplicants() {

    let input =
        document.getElementById("searchInput");

    if (!input) return;

    let filter =
        input.value.toUpperCase();

    let table =
        document.getElementById("applicantTable");

    let tr =
        table.getElementsByTagName("tr");

    for (let i = 1; i < tr.length; i++) {

        let td =
            tr[i].getElementsByTagName("td")[0];

        if (td) {

            let text =
                td.textContent ||
                td.innerText;

            if (
                text.toUpperCase().indexOf(filter)
                > -1
            ) {

                tr[i].style.display = "";

            } else {

                tr[i].style.display = "none";
            }
        }
    }
}

/* ==========================
   Page Loaded
========================== */

window.onload = function () {

    let password =
        document.getElementById("password");

    let confirmPassword =
        document.getElementById("confirm_password");

    let resume =
        document.getElementById("resume");

    if (password) {
        password.addEventListener(
            "keyup",
            validatePassword
        );
    }

    if (confirmPassword) {
        confirmPassword.addEventListener(
            "keyup",
            checkPasswordMatch
        );
    }

    if (resume) {

        resume.addEventListener(
            "change",
            validateResume
        );

        resume.addEventListener(
            "change",
            showFileName
        );
    }
};