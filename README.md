# Career Guidance Web App

## 📌 Overview
🔹 The **Career Guidance Web App** is designed to help students and professionals make informed career choices.  
🔹 It uses **AI-powered recommendations**, **Holland Code Career Assessment**, and **real-world data** to guide users toward suitable career paths.  
🔹 The system suggests **career options, college recommendations, skill development resources, and roadmaps** for success.

## 🚀 Features
🔹 **User Authentication** – Secure **Login & Sign-Up**  
🔹 **Career Assessment** – Based on **Holland Code Personality Test**  
🔹 **AI Career Prediction** – Predicts career paths based on user input  
🔹 **Career Roadmap** – Provides structured steps to build a career  
🔹 **College Recommendations** – Lists **top colleges based on user preferences**  
🔹 **Skill Development** – Suggests **learning resources & online courses**  

## 🛠️ Technologies Used
🔹 **Frontend:** HTML5, CSS3, JavaScript  
🔹 **Backend:** Python Django  
🔹 **Database:** SQLite3  
🔹 **AI Integration:** Google Gemini API for career roadmap suggestions  

## Set Up Virtual Environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

 ## Install Dependencies
 pip install -r requirements.txt

## Run Migrations
python manage.py migrate

##  Start the Server
python manage.py runserver
🔹 The app will run on http://127.0.0.1:8000/

## Future Enhancements
🔹 AI Chatbot – Real-time career guidance chatbot
🔹 Industry Mentorship – Connect students with professionals
🔹 Job Market Insights – Salary trends & in-demand skill

### **📌 Explanation of Key Files & Folders**
🔹 **career_app/** → The **main Django app** handling business logic.  
🔹 **templates/** → Contains all **HTML files** for frontend UI.  
🔹 **static/** → Stores **CSS, JS, and images** for styling and functionality.  
🔹 **models.py** → Defines **database tables** using Django ORM.  
🔹 **views.py** → Contains all the **backend logic** and request handling.  
🔹 **forms.py** → Defines Django **forms** for user input handling.  
🔹 **urls.py** → Maps **URLs** to their corresponding views.  
🔹 **settings.py** → Configuration file for **database, security, installed apps, etc.**  
🔹 **db.sqlite3** → The SQLite3 **database file** storing all user and career data.  
🔹 **requirements.txt** → List of **dependencies** required for the project.  


