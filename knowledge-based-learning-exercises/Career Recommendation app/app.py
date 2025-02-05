#Flask used for creating the User Interface
#Render_template used for rendering the HTML templates
#Request used for getting the user input from the form
from flask import Flask, render_template, request

#Initialize the Flask app
app = Flask(__name__)

# Define the knowledge base - store career data
#career_data has key features such as skills, interests, work environment and education
career_data = { 
    "Software Engineer": {
        "skills": ["programming", "problem-solving", "algorithms", "debugging"],
        "interests": ["technology", "coding", "software development", "AI"],
        "work_environment": ["remote", "office"],
        "education": ["Computer Science", "Software Engineering"]
    },
    "Data Scientist": {
        "skills": ["statistics", "machine learning", "Python", "data visualization"],
        "interests": ["data analysis", "AI", "predictive modeling", "big data"],
        "work_environment": ["remote", "office"],
        "education": ["Mathematics", "Data Science", "Statistics"]
    },
    "Graphic Designer": {
        "skills": ["creativity", "Adobe Photoshop", "visual design", "illustration"],
        "interests": ["art", "branding", "advertising", "UI/UX design"],
        "work_environment": ["freelance", "office"],
        "education": ["Graphic Design", "Fine Arts", "Visual Communication"]
    },
    "Mechanical Engineer": {
        "skills": ["engineering", "design", "problem-solving", "CAD"],
        "interests": ["machines", "mechanics", "innovation", "product design"],
        "work_environment": ["office", "field"],
        "education": ["Mechanical Engineering"]
    },
    "Cybersecurity Analyst": {
        "skills": ["network security", "penetration testing", "ethical hacking", "risk assessment"],
        "interests": ["cybersecurity", "ethical hacking", "forensics"],
        "work_environment": ["remote", "office"],
        "education": ["Cybersecurity", "Computer Science", "IT"]
    },
    "Doctor": {
        "skills": ["patient care", "diagnostics", "surgery", "medical knowledge"],
        "interests": ["medicine", "helping people", "biology", "healthcare"],
        "work_environment": ["hospital", "clinic"],
        "education": ["Medicine", "Biology"]
    },
    "Lawyer": {
        "skills": ["legal research", "public speaking", "critical thinking", "writing"],
        "interests": ["law", "justice", "debating", "advocacy"],
        "work_environment": ["courtroom", "office"],
        "education": ["Law"]
    },
    "Teacher": {
        "skills": ["communication", "lesson planning", "mentorship", "classroom management"],
        "interests": ["education", "mentoring", "helping others"],
        "work_environment": ["school", "online"],
        "education": ["Education", "Teaching"]
    },
    "Civil Engineer": {
        "skills": ["structural design", "project management", "mathematics"],
        "interests": ["construction", "architecture", "urban planning"],
        "work_environment": ["field", "office"],
        "education": ["Civil Engineering"]
    },
    "Marketing Specialist": {
        "skills": ["SEO", "content creation", "advertising", "social media"],
        "interests": ["marketing", "branding", "advertising"],
        "work_environment": ["office", "remote"],
        "education": ["Marketing", "Business"]
    },
    "Psychologist": {
        "skills": ["counseling", "empathy", "research", "mental health assessment"],
        "interests": ["mental health", "human behavior", "therapy"],
        "work_environment": ["clinic", "hospital"],
        "education": ["Psychology"]
    },
    "Accountant": {
        "skills": ["financial analysis", "bookkeeping", "taxation", "problem-solving"],
        "interests": ["finance", "business", "money management"],
        "work_environment": ["office", "remote"],
        "education": ["Accounting", "Finance"]
    },
    "Entrepreneur": {
        "skills": ["business strategy", "leadership", "risk-taking", "sales"],
        "interests": ["business", "startups", "innovation"],
        "work_environment": ["varies"],
        "education": ["Business", "Self-taught"]
    },
    "Architect": {
        "skills": ["design", "3D modeling", "urban planning", "problem-solving"],
        "interests": ["architecture", "construction", "sustainability"],
        "work_environment": ["office", "field"],
        "education": ["Architecture"]
    },
    "Game Developer": {
        "skills": ["game design", "3D modeling", "programming", "creativity"],
        "interests": ["gaming", "animation", "AI"],
        "work_environment": ["office", "remote"],
        "education": ["Game Development", "Computer Science"]
    },
    "Biologist": {
        "skills": ["research", "lab work", "data analysis", "biology"],
        "interests": ["nature", "science", "ecosystems"],
        "work_environment": ["lab", "field"],
        "education": ["Biology", "Environmental Science"]
    }
}

#Inference engine
# Function to match careers based on user input
def match_careers(user_data):
    career_scores = {}

    for career, attributes in career_data.items():
        score = 0
        
        # Match skills
        score += sum(1 for skill in user_data["skills"] if skill in attributes["skills"])
        
        # Match interests
        score += sum(1 for interest in user_data["interests"] if interest in attributes["interests"])
        
        # Match work environment
        if user_data["work_environment"] in attributes["work_environment"]:
            score += 1
        
        # Match education
        if user_data["education"] in attributes["education"]:
            score += 1

        career_scores[career] = score

    # Sort careers by highest score
    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_careers

# Route for home page for the Flask app
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        skills = request.form.get("skills").lower().split(", ")
        interests = request.form.get("interests").lower().split(", ")
        work_environment = request.form.get("work_environment").lower()
        education = request.form.get("education").lower()

        user_data = {
            "skills": skills,
            "interests": interests,
            "work_environment": work_environment,
            "education": education
        }

        sorted_careers = match_careers(user_data)
        return render_template("results.html", careers=sorted_careers[:3], career_data=career_data)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)