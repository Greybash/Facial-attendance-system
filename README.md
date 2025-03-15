🎭 Facial Attendance System 📊
This project is a Facial Recognition-based Attendance System that uses OpenCV for face detection and recognition, and Django to display attendance records on a web-based dashboard.

🚀 Features
🏷️ Face Recognition with OpenCV – Detects and recognizes faces in real time.
📄 Automated Attendance Marking – Recognized faces are logged into an attendance CSV file.
🌐 Web-Based Attendance Viewer – Uses Django to display attendance records.
📂 Multiple CSV Support – Attendance data is stored in separate CSV files for easy tracking.
🎛️ User-Friendly Dashboard – A main page with buttons to view different attendance records.
🛠️ Tech Stack
Python – Core programming language
OpenCV – Face detection and recognition
Django – Web framework for displaying attendance data
SQLite – Database for storing registered faces (optional)
HTML, CSS, Bootstrap – Frontend for a clean UI
🏗️ How It Works
Face Detection & Recognition: OpenCV captures faces via a webcam and compares them against a trained dataset.
Attendance Logging: Recognized faces are recorded with timestamps in a CSV file.
Web-Based Viewing: Django reads the CSV files and displays attendance data in a structured table.
📌 Future Enhancements
🔄 Live Web Streaming of Attendance
🔒 Secure Authentication for Admins
📈 Data Analytics & Reports
🖥️ Mobile-Friendly Dashboard
📂 Project Structure
bash
Copy
Edit
/face_recognition/   # OpenCV-based facial recognition system
/csvdata/            # Django app for displaying attendance data
  ├── templates/
  │   ├── main.html  # Dashboard with buttons
  │   ├── table.html # Attendance records table
  ├── views.py       # Logic for loading CSV data
  ├── urls.py        # URL routing
/myproject/          # Django project files
  ├── settings.py    # Django settings
  ├── urls.py        # Project-level URL configuration
attendance.csv       # CSV file storing attendance data
🏃 How to Run
Clone the repository:
bash
Copy
Edit
git clone https://github.com/yourusername/facial-attendance.git
cd facial-attendance
Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Train the face recognition model (if required).
Apply migrations:
bash
Copy
Edit
python manage.py migrate
Start the Django server:
bash
Copy
Edit
python manage.py runserver
Open http://127.0.0.1:8000/ to view attendance records.
