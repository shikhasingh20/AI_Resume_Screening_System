-- =====================================
-- AI Resume Screening System Database
-- =====================================

CREATE DATABASE IF NOT EXISTS ai_resume_screening;

USE ai_resume_screening;

-- =====================================
-- USERS TABLE
-- =====================================

CREATE TABLE users (

    id INT PRIMARY KEY AUTO_INCREMENT,

    fullname VARCHAR(100) NOT NULL,

    email VARCHAR(100) UNIQUE NOT NULL,

    password VARCHAR(255) NOT NULL,

    role ENUM('candidate','recruiter')
    NOT NULL,

    created_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP

);

-- =====================================
-- JOBS TABLE
-- =====================================

CREATE TABLE jobs (

    id INT PRIMARY KEY AUTO_INCREMENT,

    title VARCHAR(200) NOT NULL,

    description TEXT NOT NULL,

    skills TEXT,

    recruiter_id INT,

    created_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (recruiter_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);

-- =====================================
-- RESUMES TABLE
-- =====================================

CREATE TABLE resumes (

    id INT PRIMARY KEY AUTO_INCREMENT,

    user_id INT NOT NULL,

    file_name VARCHAR(255),

    file_path VARCHAR(255),

    uploaded_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);

-- =====================================
-- APPLICATIONS TABLE
-- =====================================

CREATE TABLE applications (

    id INT PRIMARY KEY AUTO_INCREMENT,

    user_id INT NOT NULL,

    job_id INT NOT NULL,

    ats_score FLOAT DEFAULT 0,

    status VARCHAR(50)
    DEFAULT 'Pending',

    applied_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON DELETE CASCADE,

    FOREIGN KEY (job_id)
    REFERENCES jobs(id)
    ON DELETE CASCADE

);