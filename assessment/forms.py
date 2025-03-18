import os
import uuid
import markdown  # ✅ Import Markdown for formatting
import google.generativeai as genai
from django import forms
from django.conf import settings
from .models import Assessment

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = [
            'name', 'age', 'sex', 'stream',
            'subject_1_name', 'subject_1_marks',
            'subject_2_name', 'subject_2_marks',
            'subject_3_name', 'subject_3_marks',
            'subject_4_name', 'subject_4_marks',
            'subject_5_name', 'subject_5_marks',
            'hollandCode1', 'hollandCode2', 'hollandCode3'
        ]

    def save(self, user, commit=True):
        assessment_input = super().save(commit=False)

        # Load Gemini API Key from settings
        gemini_api_key = getattr(settings, "GEMINI_API_KEY", None)
        if not gemini_api_key:
            print("Error: Gemini API Key is not set properly.")
            return None  

        # Configure Gemini AI
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        # 📝 **Prompt for Career Guidance & Recommendations**
        msg = f"""
        Based on the Holland career assessment codes: {assessment_input.hollandCode1}, {assessment_input.hollandCode2}, {assessment_input.hollandCode3}, and my high school marks, suggest **one best career option** for me.
        Ensure the response is concise, well-structured, and highlights only the most essential details. The headings should be colored but not too large, and the points should be listed neatly. Subpoints should be properly formatted for clarity and readability.Based on the subjects or feild like science ,commerce,humanities give the suggestions.i want the page to look neat give the points one after the other  The format should be:
        #### 🎯 Career Suggestion  
        #### ✅ **Career Name**: <career>  
       ---

        ####✅ **Why is this suitable for me?**: 
             #####<explanation>  
        
        ---
        
        #### 📌 Top 3 Colleges in India (with entrance details)  
        
        ##### **1️⃣ [<College Name> - <Place>](<College_Link>)**  
        ✅ **Specialty:** <One-line about the college’s strength>  
        ✅ **Entrance Exam Required?**: <Yes/No>  
        ✅ **Preparation Resources:**  
        - [NTA JEE Official Website](https://jeemain.nta.nic.in/) (if JEE-based)  
        - [BYJU's NEET Prep](https://byjus.com/neet/) (if medical field)  
        
        ##### **2️⃣[<College Name> - <Place>](<College_Link>)**  
        ✅ **Specialty:** <One-line about the college’s strength>  
        ✅ **Entrance Exam Required?**: <Yes/No>  
        ✅ **Preparation Resources:**  
        - [Vedantu JEE Prep](https://www.vedantu.com/iit-jee)  
        - [Unacademy Entrance Prep](https://unacademy.com/)  
        
        ##### **3️⃣ [<College Name> - <Place>](<College_Link>)**   
        ✅ **Specialty:** <One-line about the college’s strength>  
        ✅ **Entrance Exam Required?**: <Yes/No>  
        ✅ **Preparation Resources:**  
        - [Embibe Study Guide](https://www.embibe.com/)  
        
        ---
        
        #### 📌 Structured Career Roadmap  
        
        ##### **1️⃣ Foundational Learning (1st - 2nd Year)**  
        ✅ Learn **Fundamentals:** <Subjects based on career>  
        ✅ Develop **Core Skills:** <Programming/Design/Business Analysis/etc.>  
        ✅ Recommended Courses:  
        - [Beginner Course - Coursera](https://www.coursera.org)  
        - [Introductory Guide - Udemy](https://www.udemy.com)  
        
        ##### **2️⃣ Hands-on Experience (2nd - 3rd Year)**  
        ✅ Build **Projects:** <Practical skills needed>  
        ✅ Participate in **Competitions/Hackathons**  
        ✅ Certifications:  
        - [Certification Program - edX](https://www.edx.org/)  
        
        ##### **3️⃣ Advanced Specialization (3rd - 4th Year)**  
        ✅ Choose a **Niche Specialization:** <Deep learning, Robotics, Finance, etc.>  
        ✅ Learn from industry experts (Master’s programs, internships).  
        ✅ Advanced Resources:  
        - [Masterclass by Industry Experts - LinkedIn Learning](https://www.linkedin.com/learning/)  
        
        ##### **4️⃣ Internships & Industry Exposure (Final Year)**  
        ✅ Gain **Real-World Experience:** Internship/Apprenticeship.  
        ✅ Connect with **Mentors & Alumni**.  
        ✅ Internship Platforms:  
        - [Internshala](https://internshala.com/)  
        - [Naukri Internships](https://www.naukri.com/internships)  
        - [LinkedIn Jobs](https://www.linkedin.com/jobs/)  
        
        ---
        
        #### 📌 Best Websites to Learn & Practice Skills  
        - [Coursera](https://www.coursera.org)  
        - [Udemy](https://www.udemy.com)  
        - [LinkedIn Learning](https://www.linkedin.com/learning/)  
        - [Kaggle](https://www.kaggle.com)  
        - [GeeksforGeeks](https://www.geeksforgeeks.org)  
        
        #### 🔗 Explore LinkedIn Profiles of Industry Experts  
        - [Explore Industry Experts](https://www.linkedin.com/search/results/people/?keywords=<career>)  


        Stream = {assessment_input.stream}  
        {assessment_input.subject_1_name} = {assessment_input.subject_1_marks}  
        {assessment_input.subject_2_name} = {assessment_input.subject_2_marks}  
        {assessment_input.subject_3_name} = {assessment_input.subject_3_marks}  
        {assessment_input.subject_4_name} = {assessment_input.subject_4_marks}  
        {assessment_input.subject_5_name} = {assessment_input.subject_5_marks} 
        
        """
        
        # Send request to Gemini AI
        try:
            response = model.generate_content(msg)
            
            if response and hasattr(response, "text"):
                raw_text = response.text.strip()
                
                # ✅ Convert Markdown to HTML
                formatted_html = markdown.markdown(raw_text)  
                
                # Save result
                assessment_input.result = formatted_html  # Store HTML version
                assessment_input.user = user  
                assessment_input.uuid = uuid.uuid4()  
                assessment_input.save()
                
                if commit:
                    assessment_input.save()
                
                return assessment_input
            
            else:
                print("Error: No valid response from Gemini AI.")
                return None

        except Exception as e:
            print(f"Gemini AI API Error: {e}")
            return None

        
        
'''import os
import openai
import uuid
from django import forms
from .models import Assessment

msg = f"""
        Based on the following Holland career assessment codes: {assessment_input.hollandCode1}, {assessment_input.hollandCode2}, {assessment_input.hollandCode3}, and my high school marks, suggest 25 job profiles with explanations for why each is suitable for me. 
        Provide your answers in this format:

        **Job Title:** <job name>  
        **Reason:** <reason for suitability>

        Stream = {assessment_input.stream}  
        {assessment_input.subject_1_name} = {assessment_input.subject_1_marks}  
        {assessment_input.subject_2_name} = {assessment_input.subject_2_marks}  
        {assessment_input.subject_3_name} = {assessment_input.subject_3_marks}  
        {assessment_input.subject_4_name} = {assessment_input.subject_4_marks}  
        {assessment_input.subject_5_name} = {assessment_input.subject_5_marks}  
        """












class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['name', 'age', 'sex', 'stream',
                  'subject_1_name', 'subject_1_marks',
                  'subject_2_name', 'subject_2_marks',
                  'subject_3_name', 'subject_3_marks',
                  'subject_4_name', 'subject_4_marks',
                  'subject_5_name', 'subject_5_marks',
                  'hollandCode1', 'hollandCode2', 'hollandCode3']

    def save(self, user):
        assessment_input = super().save(commit=False)

        # Create a os environment variable OPENAI_API_KEY to store the api key
        openai.api_key = os.getenv("OPENAI_API_KEY")
        msg = f"""
        https://www.truity.com/career-planning/holland-code
        https://www.onetonline.org/explore/interests/{assessment_input.hollandCode1}/{assessment_input.hollandCode2}/{assessment_input.hollandCode3}/
        https://fyi.extension.wisc.edu/teencourthub/files/2014/05/Holland-Code-Assessment.pdf
        Based on the above links and your own calculation which job profile is better for me according to my holland career assessment result which is {assessment_input.hollandCode1}, {assessment_input.hollandCode2} and {assessment_input.hollandCode3}, and my high school marks along with the stream is as follows:
        Stream = {assessment_input.stream}
        {assessment_input.subject_1_name} = {assessment_input.subject_1_marks}
        {assessment_input.subject_2_name} = {assessment_input.subject_2_marks}
        {assessment_input.subject_3_name} = {assessment_input.subject_3_marks}
        {assessment_input.subject_4_name} = {assessment_input.subject_4_marks}
        {assessment_input.subject_5_name} = {assessment_input.subject_5_marks}

        Give me 25 such job profile that are suitable for me and have career growth. Tell me why each job profile is suitable for me. Give the output inside an html div tag.
        """
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}]
        )
        result = completion.choices[0].message.content

        assessment_input.result = result
        assessment_input.user = user
        assessment_input.uuid = uuid.uuid4()
        assessment_input.save()
        return assessment_input


import os
import uuid
import google.generativeai as genai
from django import forms
from django.conf import settings
from .models import Assessment

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['name', 'age', 'sex', 'stream',
                  'subject_1_name', 'subject_1_marks',
                  'subject_2_name', 'subject_2_marks',
                  'subject_3_name', 'subject_3_marks',
                  'subject_4_name', 'subject_4_marks',
                  'subject_5_name', 'subject_5_marks',
                  'hollandCode1', 'hollandCode2', 'hollandCode3']

    def save(self, user):
        assessment_input = super().save(commit=False)

        # Load Gemini API Key from settings
        gemini_api_key = getattr(settings, "GEMINI_API_KEY", None)
        if not gemini_api_key:
            print("Error: Gemini API Key is not set properly.")
            return None  # Return early if API key is not set

        # Configure Gemini AI
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Prepare the input message for Gemini AI
        msg = f"""
        Based on the following Holland career assessment codes: {assessment_input.hollandCode1}, {assessment_input.hollandCode2}, {assessment_input.hollandCode3}, and my high school marks, suggest 25 job profiles with explanations for why each is suitable for me. 
        Provide your answers in this format: Job Title: <job name>, Reason: <reason for suitability>.

        Stream = {assessment_input.stream}
        {assessment_input.subject_1_name} = {assessment_input.subject_1_marks}
        {assessment_input.subject_2_name} = {assessment_input.subject_2_marks}
        {assessment_input.subject_3_name} = {assessment_input.subject_3_marks}
        {assessment_input.subject_4_name} = {assessment_input.subject_4_marks}
        {assessment_input.subject_5_name} = {assessment_input.subject_5_marks}
        """

        # Send request to Gemini AI
        try:
            response = model.generate_content(msg)

            # Ensure response is valid
            if response and hasattr(response, "text"):
                result = response.text.strip()

                # Save the result in the model and associate it with the user
                assessment_input.result = result
                assessment_input.user = user
                assessment_input.uuid = uuid.uuid4()
                assessment_input.save()

                print("Job Suggestions Saved:", result)  # Debugging purpose
                return assessment_input
            else:
                print("Error: No valid response from Gemini AI.")
                return None

        except Exception as e:
            print(f"Gemini AI API Error: {e}")
            return None
'''

