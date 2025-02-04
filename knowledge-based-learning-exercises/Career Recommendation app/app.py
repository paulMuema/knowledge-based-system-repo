#Flask used for creating the User Interface
#Render_template used for rendering the HTML templates
#Request used for getting the user input from the form
from flask import Flask, render_template, request

#Initialize the Flask app
app = Flask(__name__)

# Define the knowledge base - store career data
#Career has key features such as skills, interests, work environment and education
career_data = {
    "Software Engineer": {
        "skills": ["programming", "problem-solving", "logical thinking"],
        "interests": ["technology", "software development"],
        "work_environment": ["remote", "office"],
        "education": ["self-taught", "bachelor's", "certification"]
    },
    "Doctor": {
        "skills": ["critical thinking", "empathy", "medical knowledge"],
        "interests": ["healthcare", "helping people"],
        "work_environment": ["hospital", "clinic"],
        "education": ["medical degree"]
    },
    "Graphic Designer": {
        "skills": ["creativity", "visual design", "Adobe Photoshop"],
        "interests": ["art", "design"],
        "work_environment": ["freelance", "office"],
        "education": ["self-taught", "bachelor's", "certification"]
    },
    "Data Scientist": {
        "skills": ["statistics", "machine learning", "data analysis"],
        "interests": ["technology", "AI"],
        "work_environment": ["remote", "office"],
        "education": ["bachelor's", "master's"]
    }
}

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