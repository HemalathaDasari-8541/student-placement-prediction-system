from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = "placement_project_secret"

# ---------------------------------------
# STORE REGISTERED USER
# ---------------------------------------

user_data = {}

# ---------------------------------------
# STORE STUDENT DETAILS
# ---------------------------------------

student_data = {}

# ---------------------------------------
# HOME PAGE (LOGIN)
# ---------------------------------------

@app.route("/")
def home():
    return render_template("index.html")

# ---------------------------------------
# REGISTER PAGE
# ---------------------------------------

@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

# ---------------------------------------
# CREATE ACCOUNT
# ---------------------------------------

@app.route("/register", methods=["POST"])
def register_account():

    global user_data

    user_data = {

        "fullname": request.form["fullname"],

        "email": request.form["email"],

        "mobile": request.form["mobile"],

        "password": request.form["password"]

    }

    return redirect(url_for("personal"))

# ---------------------------------------
# LOGIN
# ---------------------------------------

@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]

    password = request.form["password"]

    if (

        user_data

        and

        email == user_data["email"]

        and

        password == user_data["password"]

    ):

        return redirect(url_for("personal"))

    else:

        return """

        <script>

        alert("Invalid Email or Password");

        window.location.href="/";

        </script>

        """

# ---------------------------------------
# PERSONAL INFORMATION
# ---------------------------------------

@app.route("/personal")
def personal():
    return render_template("personal.html")
# ---------------------------------------
# DASHBOARD
# ---------------------------------------

@app.route("/dashboard", methods=["POST"])
def dashboard():

    global student_data

    student_data = {

        "name": request.form["name"],

        "father": request.form["father"],

        "mother": request.form["mother"],

        "dob": request.form["dob"],

        "gender": request.form["gender"],

        "phone": request.form["phone"],

        "email": request.form["email"],

        "qualification": request.form["qualification"],

        "branch": request.form["branch"],

        "tenth": request.form["tenth"],

        "inter": request.form["inter"],

        "cgpa": request.form["cgpa"],

        "skills": request.form["skills"]

    }

    return render_template(

        "dashboard.html",

        **student_data

    )
# ---------------------------------------
# PLACEMENT RESULT
# ---------------------------------------

@app.route("/output")
def output():

    if not student_data:
        return redirect(url_for("personal"))

    tenth = float(student_data["tenth"])
    inter = float(student_data["inter"])
    cgpa = float(student_data["cgpa"])

    qualification = student_data["qualification"]
    branch = student_data["branch"]
    skills = student_data["skills"].lower()

    # -------------------------
    # SKILL SCORE
    # -------------------------

    skill_list = [

        "python",
        "java",
        "c",
        "c++",
        "html",
        "css",
        "javascript",
        "sql",
        "machine learning",
        "data science"

    ]

    skill_count = 0

    for skill in skill_list:

        if skill in skills:
            skill_count += 1

    skill_score = min(skill_count * 5, 20)

    # -------------------------
    # ACADEMIC SCORE
    # -------------------------

    academic_score = (

        (tenth * 0.25) +

        (inter * 0.25) +

        ((cgpa / 10) * 50)

    )

    placement_score = round(

        academic_score * 0.8 +

        skill_score

    )

    if placement_score > 100:
        placement_score = 100

    # -------------------------
    # STATUS
    # -------------------------

    if placement_score >= 75:

        status = "🎉 High Chance of Placement"

    elif placement_score >= 50:

        status = "⚡ Moderate Chance of Placement"

    else:

        status = "📚 Needs Improvement"

    # -------------------------
    # JOB ROLES & SKILLS
    # -------------------------

    improve_skills = []
    job_roles = []

    if qualification in ["B.Tech", "B.E"]:

        if "Computer Science" in branch or "Information Technology" in branch:

            improve_skills = [
                "Data Structures & Algorithms",
                "SQL",
                "Web Development",
                "Problem Solving"
            ]

            job_roles = [
                "Software Developer",
                "Python Developer",
                "Web Developer",
                "Data Analyst"
            ]

        elif "Artificial Intelligence" in branch or "Data Science" in branch:

            improve_skills = [
                "Machine Learning",
                "Python",
                "Statistics",
                "Deep Learning"
            ]

            job_roles = [
                "AI Engineer",
                "Machine Learning Engineer",
                "Data Scientist",
                "Data Analyst"
            ]

        elif "Electronics" in branch:

            improve_skills = [
                "Embedded Systems",
                "VLSI",
                "Microcontrollers",
                "Programming"
            ]

            job_roles = [
                "Embedded Engineer",
                "VLSI Engineer",
                "Electronics Engineer",
                "IoT Developer"
            ]

        elif "Electrical" in branch:

            improve_skills = [
                "Power Systems",
                "PLC",
                "Automation",
                "Programming"
            ]

            job_roles = [
                "Electrical Engineer",
                "Automation Engineer",
                "Control Engineer",
                "Embedded Engineer"
            ]

        elif "Mechanical" in branch:

            improve_skills = [
                "AutoCAD",
                "CAD/CAM",
                "Manufacturing",
                "Design"
            ]

            job_roles = [
                "Mechanical Engineer",
                "Design Engineer",
                "Production Engineer",
                "CAD Engineer"
            ]

        elif "Civil" in branch:

            improve_skills = [
                "AutoCAD",
                "Structural Analysis",
                "Project Management",
                "Construction"
            ]

            job_roles = [
                "Civil Engineer",
                "Site Engineer",
                "Structural Engineer",
                "Project Engineer"
            ]

    elif qualification == "BCA":

        improve_skills = [
            "Programming",
            "SQL",
            "Web Development",
            "Software Testing"
        ]

        job_roles = [
            "Software Developer",
            "Web Developer",
            "Software Tester",
            "Application Developer"
        ]

    elif qualification == "MCA":

        improve_skills = [
            "Cloud Computing",
            "Advanced Java",
            "DSA",
            "System Design"
        ]

        job_roles = [
            "Software Engineer",
            "Full Stack Developer",
            "Cloud Engineer",
            "System Analyst"
        ]

    elif qualification == "B.Com":

        improve_skills = [
            "Advanced Excel",
            "Tally",
            "Financial Analysis",
            "Communication"
        ]

        job_roles = [
            "Accountant",
            "Financial Analyst",
            "Bank Executive",
            "Business Analyst"
        ]

    else:

        improve_skills = [
            "Communication Skills",
            "Computer Skills",
            "Problem Solving",
            "Industry Knowledge"
        ]

        job_roles = [
            "Management Trainee",
            "Business Executive",
            "Office Administrator",
            "Customer Support Executive"
        ]

    return render_template(

        "output.html",

        **student_data,

        placement_score=placement_score,

        status=status,

        improve_skills=improve_skills,

        job_roles=job_roles

    )
# ---------------------------------------
# RUN APPLICATION
# ---------------------------------------

if __name__ == "__main__":
    app.run(debug=True)