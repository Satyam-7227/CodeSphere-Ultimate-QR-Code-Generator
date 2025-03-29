# CodeSphere: Ultimate QR Code Generator


## Project Overview
CodeSphere is a **Full Stack Development (FSD) Project** created for **Semester 3** as part of the FSD subject. This project is designed for exam purposes and demonstrates a complete web-based **QR Code Generator** using **HTML, CSS, JavaScript, and Django** as the backend.

## Features 🚀
- ✅ **User Authentication**: Sign up, log in, and manage user accounts.
- 🔗 **QR Code Generation**: Create QR codes for URLs, text, images, and videos.
- 🎨 **Static QR Codes Only**: Initially planned for **dynamic QR codes**, but currently only supports static QR codes that store data at the time of creation.
- 📂 **Local Database**: The project uses a **local XAMPP MySQL database**, but it is not fully implemented for remote usage. Users must configure their database.
- 📱 **Responsive UI**: Works on both desktop and mobile devices.
- 📊 **Analytics (Planned)**: Potential for tracking QR code usage in future updates.

## Tech Stack 🛠️
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Database**: MySQL (XAMPP)
- **Libraries Used**:
  - `qrcode` library (Python) for QR code generation
  - `Django` for backend framework

## Setup Instructions 🏗️
### 1. Clone the Repository
```sh
git clone https://github.com/Satyam-7227/CodeSphere-Ultimate-QR-Code-Generator.git
cd CodeSphere
```

### 2. Install Dependencies 📦
```sh
pip install -r requirements.txt
```

### 3. Setup the Database 🗄️ (Optional - Not Implemented by Default)
- Start **XAMPP** and enable **MySQL** and **Apache**.
- Open `phpMyAdmin` and create a new database named `codesphere`.
- Update `settings.py` with the correct database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'codesphere',
        'USER': 'root',
        'PASSWORD': '',  # Set your MySQL password if applicable
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Run the Development Server 🚀
```sh
python manage.py runserver
```
Then open **http://localhost:8000/** in your browser.

## Folder Structure 📁
```
CodeSphere/
│── static/        # Static files (HTML, CSS, JS)
│── templates/     # HTML templates
│── codesphere/    # Django app
│── db.sqlite3     # Local database (if using SQLite)
│── manage.py      # Django project manager
│── settings.py    # Database & project settings
│── README.md      # Project documentation
```

## Future Improvements 🔮
- Implementing **dynamic QR codes** with URL redirection 🌍
- Adding support for PDF and document QR codes 📄
- Enhancing the analytics dashboard 📊
- Allowing users to download QR codes in multiple formats (PNG, SVG, etc.) 🖼️

## Notes ⚠️
- This project was built during a learning phase and is **not a fully deployed system**.
- It uses a **local database** for saving QR codes instead of a cloud-based solution.
- Users who wish to extend this project must integrate a **fully configured database and backend storage** for full functionality.

## License 📜
This project is for educational purposes as part of **Semester 3 Full Stack Development (FSD) coursework**.


