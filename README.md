# 💻 IT Asset Management System

A modern and secure **IT Asset Management System** developed using **Python Flask and PostgreSQL** to help organizations efficiently manage IT resources, employees, assets, complaints, maintenance activities, and user operations.

This project provides a complete digital solution for managing the complete lifecycle of IT assets — from asset registration and allocation to complaint handling and maintenance tracking.

Developed as a major full-stack project to demonstrate practical experience in:

- Backend Development
- Database Design
- Authentication & Authorization
- CRUD Operations
- Dashboard Analytics
- Role-Based Access Control
- Modern UI Development


---

# 🚀 Key Features


## 🔐 Authentication & Security

- User Registration
- Secure Login System
- Forgot Password
- Email OTP Verification
- Password Reset
- Password Encryption using bcrypt
- Session Management
- Role-Based Login


### User Roles

The system supports different user roles:

### 👑 Admin

Admin can:

- Manage Employees
- Manage Assets
- Manage Departments
- View Complaints
- Manage Maintenance
- Generate Reports
- Monitor System Dashboard


### 👨‍💻 Employee

Employee can:

- View Assigned Assets
- Raise Complaints
- Track Complaint Status
- View Profile
- Update Profile Details
- Upload Profile Photo
- Change Password



---

# 👨‍💼 Employee Management

Admin Features:

- Add Employee
- View Employee List
- Edit Employee Details
- Delete Employee
- Search Employee
- Assign Department
- Manage Employee Records


Employee Portal:

- Personal Dashboard
- Assigned Asset View
- Complaint History
- Profile Management



---

# 💻 Asset Management


Complete Asset Lifecycle Management:


Features:

- Add New Assets
- Update Asset Details
- Delete Assets
- Assign Assets to Employees
- Track Asset Status
- View Asset History


Asset Status:

- Available
- Assigned
- Under Maintenance
- Damaged
- Retired



---

# 🏢 Department Management


Features:

- Add Departments
- Update Department Details
- Assign Employees
- Department-wise Asset Management



---

# 📢 Complaint Management


Employee:

- Raise Complaint
- Select Assigned Asset
- Describe Issue
- Track Complaint Status


Admin:

- View All Complaints
- Manage Complaint Status
- Resolve Complaints
- Maintain Complaint Records


Complaint Workflow:

```
Pending
   ↓
Assigned
   ↓
In Progress
   ↓
Resolved
   ↓
Closed
```



---

# 🛠 Maintenance Management


Features:

- Create Maintenance Records
- Update Maintenance Status
- View Maintenance History
- Track Asset Maintenance


Maintenance Information:

- Asset Details
- Maintenance Date
- Issue Description
- Status
- Maintenance History



---

# 📊 Dashboard & Analytics


Interactive Dashboard with:


## Admin Dashboard

- Total Employees
- Total Assets
- Total Departments
- Total Complaints
- Total Maintenance Requests


Visualizations:

- Asset Category Chart
- Complaint Status Chart
- Monthly Maintenance Chart


Technology:

- Chart.js



---

## Employee Dashboard


Employee Dashboard Cards:

- 💻 My Assets
- 📢 Complaints
- ⏳ Pending Requests
- ✅ Resolved Complaints


UI Features:

- 3D Animated Cards
- Floating Icons
- Gradient Colors
- Hover Effects
- Responsive Design



---

# ⚙ Settings Module


Available Settings:

- My Profile
- Change Password
- Upload Profile Photo
- System Information
- Logout


System Information Includes:

- Application Name
- Version Details
- Developer Information
- Technology Stack



---

# 🎨 Modern User Interface


UI Features:

- Responsive Layout
- Bootstrap 5 Design
- Modern Sidebar Navigation
- Dark/Light Theme Support
- Animated Dashboard Cards
- 3D Hover Effects
- Glassmorphism Components
- Interactive Icons



---

# 📄 Reports


Available Reports:

- Employee Report
- Asset Report
- Complaint Report
- Maintenance Report


Export Support:

- PDF Reports
- Excel Reports



---

# 🛠 Technology Stack


## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Chart.js


## Backend

- Python
- Flask


## Database

- PostgreSQL


## Python Libraries

- Flask
- Psycopg2
- bcrypt
- Jinja2
- pandas
- openpyxl


## Development Tools

- VS Code
- Git
- GitHub
- pgAdmin



---

# 📁 Project Structure


```
IT_Asset_Management_System/

│
├── app.py
├── config.py
├── requirements.txt
│
├── database/
│
├── models/
│
├── routes/
│
├── templates/
│
├── static/
│
├── utils/
│
└── README.md

```



---

# ⚙ Installation Guide


## Clone Repository


```bash
git clone https://github.com/harshyadav1602/-IT-Asset-Management-System.git
```


## Navigate Project Folder


```bash
cd IT-Asset-Management-System
```


## Create Virtual Environment


```bash
python -m venv venv
```


## Activate Environment


Windows:

```bash
venv\Scripts\activate
```


Linux/macOS:

```bash
source venv/bin/activate
```



## Install Requirements


```bash
pip install -r requirements.txt
```



## Configure Database


Create PostgreSQL database and update credentials in:


```
config.py
```



## Run Application


```bash
python app.py
```



Open:


```
http://127.0.0.1:5000
```



---

# 📸 Application Modules


The system contains:


```
Login System

        ↓

Admin Dashboard

        ↓

Employee Management

        ↓

Asset Management

        ↓

Complaint Management

        ↓

Maintenance Management

        ↓

Reports

        ↓

Employee Portal

```



---

# 🔮 Future Enhancements


Planned Improvements:


- QR Code Based Asset Tracking
- Barcode Scanner Integration
- Email Notification System
- SMS Alerts
- Cloud Deployment
- REST API Development
- Mobile Application
- AI Based Asset Prediction
- Advanced Audit Logs
- Power BI Integration



---

# 📚 Learning Outcomes


Through this project:


- Developed Flask Based Web Application
- Designed PostgreSQL Database Architecture
- Implemented Authentication System
- Implemented Role-Based Access Control
- Developed CRUD Modules
- Created Interactive Dashboards
- Designed Responsive UI
- Implemented Secure Password Handling
- Integrated Email OTP System
- Managed GitHub Version Control



---

# 👨‍💻 Author


## Harsh Yadav


**B.Tech Computer Science Engineering (AI & ML)**


Meerut Institute of Engineering and Technology (MIET)



---

# 📄 License


This project is developed for educational and learning purposes.
