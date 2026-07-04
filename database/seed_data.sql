USE ai_resume_screening;

-- ==========================================
-- USERS
-- ==========================================

INSERT INTO users(fullname,email,password,role)

VALUES

('Admin','admin@gmail.com','admin123','recruiter'),

('Rahul Sharma','rahul@gmail.com','rahul123','candidate'),

('Priya Singh','priya@gmail.com','priya123','candidate'),

('Aman Kumar','aman@gmail.com','aman123','candidate'),

('HR Manager','hr@gmail.com','hr123','recruiter');



-- ==========================================
-- JOBS
-- ==========================================

INSERT INTO jobs

(title,description,skills,recruiter_id)

VALUES

(

'Python Developer',

'Looking for Python Developer having Flask and MySQL knowledge.',

'Python,Flask,MySQL,Git',

1

),

(

'Java Developer',

'Looking for Java Developer with Spring Boot.',

'Java,Spring Boot,MySQL,Git',

1

),

(

'Data Analyst',

'Data analysis and visualization.',

'Python,Pandas,SQL,Power BI',

5

);



-- ==========================================
-- RESUMES
-- ==========================================

INSERT INTO resumes

(user_id,file_name,file_path)

VALUES

(2,'rahul_resume.pdf','uploads/resumes/rahul_resume.pdf'),

(3,'priya_resume.pdf','uploads/resumes/priya_resume.pdf'),

(4,'aman_resume.pdf','uploads/resumes/aman_resume.pdf');



-- ==========================================
-- APPLICATIONS
-- ==========================================

INSERT INTO applications

(user_id,job_id,ats_score,status)

VALUES

(2,1,87.50,'Shortlisted'),

(3,1,79.00,'Pending'),

(4,2,92.00,'Shortlisted');