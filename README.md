# **🌟 AI Chatbot Project**
# to create a basic ai ChatBot
## 📌 Project Description 
- This is an AI-powered chatbot web application that interacts with users and provides intelligent responses based on user queries. It also maintains a chat history feature, allowing users to view their past inputs. The chatbot integrates a backend for processing responses and handling user interactions dynamically.
## 🛠️ Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Database (For History):** SQLite or JSON storage
- **AI Model:** Gemini API (Google AI)
## 🚀 Features
- ✅ User-friendly chatbot interface
- ✅ Interactive and responsive UI
- ✅ Stores and displays chat history
- ✅ Option to delete chat history entries
- ✅ AI-generated responses using Gemini API
## 📌 How to Run Your Project

-execute the command as follow:
### **step 1**
- **1.1 Create a Project Folder**
  ```sh
  mkdir AI_Agent
  cd AI_Agent
- **1.2 Create a Virtual Environment(optional)**
   ```sh
   python -m venv venv
 - **activate**
    ```sh
    venv\Scripts\activate
### **step 2**

- **2.1 📌 Install Dependencies**
    ```sh
     pip install flask google-generativeai requests python-dotenv flask-cors
- **2.2** create a python file with Name **app.py** ,update the code provided.
### **step3**
- **3.1**create a html file with name **index.html**  , update the code provided.
-  **NOTE:** app.py and index.html should be created in the same file.
- then open the cmd in that directory.
- **3.2 to intialize the database**
  - Type  **python** in cmd .
     ```sh
        python
  - then paste the below code in the cmd
     ```sh
        from app import db, app
        with app.app_context():
        db.create_all()
  - then write a command **exit** in the cmd.
     ```sh
      exit()
  
### **step 4**
-in these step to intialize your **API_kEY ( gemini API KEY)** , execute the following by replacing **YOUR_API_KEY** with your key.
    ```sh
       set GEMINI_API_KEY = YOUR_API_KEY
- **execute the python file**
- execute the python file given with name **app.py**
   ```sh
     python app.py
- If everything is set up correctly, you should see:
  ```sh
     Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
- now open the **html file (index.html)** in any browser
- then you can see the interface and you can chat with that Bot , it will gives response and stores the history of your chat.

 

   
 
