# 30 Days of Python Challenge API

A comprehensive Flask web application that combines both a RESTful API and interactive web pages for the Thirty Days of Python Challenge. This project demonstrates Python web development skills including API design, template rendering, form handling, and deployment.

## 🚀 Live Demo

- **Main Application**: [https://python-challenge-a0qs.onrender.com/](https://python-challenge-a0qs.onrender.com/)
- **API Documentation**: [https://python-challenge-a0qs.onrender.com/api](https://python-challenge-a0qs.onrender.com/api)

## 📋 Features

### 🌐 Web Pages
- **Home** - Overview of the API and challenge
- **API Documentation** - Complete API reference
- **Students** - Display student information
- **Courses** - Show available courses
- **Blog Posts** - Technical articles and tutorials
- **Text Analyzer** - Interactive text analysis tool
- **Feedback Form** - User feedback collection

### 🔗 REST API Endpoints
- `GET /api/info` - API metadata and information
- `GET /api/students` - List all students (with filtering)
- `GET /api/students/{id}` - Get specific student
- `GET /api/courses` - List all courses
- `GET /api/courses/{id}` - Get specific course
- `GET /api/posts` - List all blog posts
- `GET /api/posts/{id}` - Get specific post
- `GET /api/feedbacks` - Get all feedbacks
- `POST /api/feedbacks` - Submit new feedback
- `GET /api/stats` - API statistics

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Templates**: Jinja2
- **Deployment**: Render
- **WSGI Server**: Gunicorn

## 📁 Project Structure

```
python-challenge/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment configuration
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── api.html          # API documentation
│   ├── students.html     # Students page
│   ├── courses.html      # Courses page
│   ├── posts.html        # Blog posts page
│   ├── text_analyzer.html # Text analysis tool
│   ├── feedbacks.html    # Feedback form
│   ├── 404.html          # Not found page
│   └── 500.html          # Server error page
└── README.md             # This file
```

## 🚀 Installation & Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayman4data/python-challenge.git
   cd python-challenge
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Visit the application**
   - Open http://localhost:5000 in your browser

## 🌐 API Usage Examples

### Get All Students
```bash
curl https://python-challenge-a0qs.onrender.com/api/students
```

### Filter Students by Country
```bash
curl "https://python-challenge-a0qs.onrender.com/api/students?country=Finland"
```

### Get API Information
```bash
curl https://python-challenge-a0qs.onrender.com/api/info
```

### Submit Feedback via API
```bash
curl -X POST https://python-challenge-a0qs.onrender.com/api/feedbacks \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com", "message": "Great API!"}'
```

## 🎯 Challenge Objectives

This project completes the API building challenge from [Asabeneh's 30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python), demonstrating:

- ✅ RESTful API design with Flask
- ✅ JSON response formatting
- ✅ Error handling and status codes
- ✅ Query parameter filtering
- ✅ Template rendering
- ✅ Form handling
- ✅ Deployment to cloud platform

## 🔧 Dependencies

- Flask==2.3.3
- gunicorn==21.2.0

## 📝 License

This project is part of the Thirty Days of Python Challenge and is open source.

## 👨‍💻 Author

**Ayman**  
- LinkedIn: [@Ayman Djemoui](https://www.linkedin.com/in/ayman-djemoui-249286126)
- GitHub: [@ayman4data](https://github.com/ayman4data)
- Project: [Python Challenge](https://github.com/ayman4data/python-challenge)

## 🙏 Acknowledgments

- [Asabeneh Yetayeh](https://github.com/Asabeneh) for the 30 Days of Python Challenge
- [Render](https://render.com) for free hosting services

---

<div align="center">

**Built using Flask and Python**

</div>
