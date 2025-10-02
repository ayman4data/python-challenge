from flask import Flask, jsonify, request, render_template
import json
import os
import re
from datetime import datetime
from collections import Counter

app = Flask(__name__)

# Sample data
sample_data = {
    "name": "Thirty Days of Python Challenge",
    "description": "A 30-day programming challenge to learn Python",
    "version": "1.0.0",
    "author": "Asabeneh Yetayeh",
    "github": "https://github.com/Asabeneh/30-Days-Of-Python",
    "endpoints": {
        "home": "/",
        "api_info": "/api",
        "students": "/api/students",
        "courses": "/api/courses",
        "posts": "/api/posts",
        "text_analyzer": "/text-analyzer",
        "feedback": "/feedbacks"
    }
}

students = [
    {
        "id": 1,
        "name": "John Doe",
        "country": "Finland",
        "city": "Helsinki",
        "skills": ["HTML", "CSS", "JavaScript", "Python"]
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "country": "Sweden",
        "city": "Stockholm",
        "skills": ["Python", "Django", "Flask", "SQL"]
    },
    {
        "id": 3,
        "name": "Mike Johnson",
        "country": "Norway",
        "city": "Oslo",
        "skills": ["Java", "Spring", "React", "AWS"]
    }
]

courses = [
    {
        "id": 1,
        "name": "Python Programming",
        "description": "Learn Python from scratch with hands-on projects and real-world examples",
        "duration": "30 days",
        "price": "Free",
        "instructor": "Asabeneh Yetayeh",
        "level": "Beginner",
        "topics": ["Variables", "Data Types", "Functions", "OOP", "File Handling"]
    },
    {
        "id": 2,
        "name": "Web Development with Flask",
        "description": "Build modern web applications using Flask framework",
        "duration": "45 days",
        "price": "Free",
        "instructor": "Asabeneh Yetayeh",
        "level": "Intermediate",
        "topics": ["Flask Basics", "Templates", "Forms", "Database", "Deployment"]
    },
    {
        "id": 3,
        "name": "Data Science Fundamentals",
        "description": "Learn data analysis, visualization and machine learning with Python",
        "duration": "60 days",
        "price": "Free",
        "instructor": "Asabeneh Yetayeh",
        "level": "Intermediate",
        "topics": ["Pandas", "NumPy", "Matplotlib", "Scikit-learn", "Data Cleaning"]
    }
]

posts = [
    {
        "id": 1,
        "title": "Getting Started with Python",
        "content": "Python is a powerful, versatile programming language that's perfect for beginners and experts alike. In this post, we'll explore the basics of Python syntax and how to set up your development environment.",
        "excerpt": "Learn the fundamentals of Python programming and set up your development environment.",
        "author": "Asabeneh Yetayeh",
        "date": "2024-01-15",
        "tags": ["python", "beginners", "programming"],
        "read_time": "5 min",
        "category": "Tutorial"
    },
    {
        "id": 2,
        "title": "Building Your First Flask Application",
        "content": "Flask is a lightweight web framework that makes it easy to build web applications in Python. We'll walk through creating a simple web app from scratch.",
        "excerpt": "Step-by-step guide to creating your first web application with Flask.",
        "author": "Asabeneh Yetayeh",
        "date": "2024-01-20",
        "tags": ["flask", "web", "python", "tutorial"],
        "read_time": "8 min",
        "category": "Web Development"
    },
    {
        "id": 3,
        "title": "Data Analysis with Pandas",
        "content": "Pandas is the most popular data manipulation library in Python. Learn how to load, clean, and analyze data efficiently.",
        "excerpt": "Master data manipulation and analysis using the Pandas library.",
        "author": "Asabeneh Yetayeh",
        "date": "2024-01-25",
        "tags": ["pandas", "data analysis", "python"],
        "read_time": "10 min",
        "category": "Data Science"
    }
]

# Store feedbacks in memory (in production, use a database)
feedbacks = []

# Template Routes
@app.route('/')
def home():
    """Home page with HTML template"""
    return render_template('index.html', 
                         title='30 Days of Python Challenge',
                         data=sample_data,
                         timestamp=datetime.now())

@app.route('/api')
def api_docs():
    """API documentation page"""
    return render_template('api.html',
                         title='API Documentation',
                         data=sample_data,
                         endpoints=sample_data['endpoints'],
                         timestamp=datetime.now())

@app.route('/students')
def students_page():
    """Students page with HTML template"""
    return render_template('students.html',
                         title='Students',
                         students=students,
                         count=len(students),
                         timestamp=datetime.now())

@app.route('/courses')
def courses_page():
    """Courses page with HTML template"""
    return render_template('courses.html',
                         title='Courses',
                         courses=courses,
                         count=len(courses),
                         timestamp=datetime.now())

@app.route('/posts')
def posts_page():
    """Posts page with HTML template"""
    return render_template('posts.html',
                         title='Blog Posts',
                         posts=posts,
                         count=len(posts),
                         timestamp=datetime.now())

# Text Analyzer with actual functionality
@app.route('/text-analyzer', methods=['GET', 'POST'])
def text_analyzer():
    """Text analyzer page with actual analysis functionality"""
    analysis_result = None
    
    if request.method == 'POST':
        text = request.form.get('text', '')
        if text:
            # Perform text analysis
            analysis_result = analyze_text(text)
    
    return render_template('text_analyzer.html',
                         title='Text Analyzer',
                         analysis_result=analysis_result,
                         timestamp=datetime.now())

def analyze_text(text):
    """Analyze text and return statistics"""
    # Remove extra whitespace
    text = text.strip()
    
    # Basic statistics
    char_count = len(text)
    word_count = len(text.split())
    line_count = len(text.splitlines())
    
    # Remove punctuation for word analysis
    clean_text = re.sub(r'[^\w\s]', '', text)
    words = clean_text.lower().split()
    
    # Word frequency
    word_freq = Counter(words)
    most_common_words = word_freq.most_common(5)
    
    # Sentence count (rough estimate)
    sentence_count = len(re.split(r'[.!?]+', text))
    
    # Average word length
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    
    # Reading time estimate (200 words per minute)
    reading_time = word_count / 200 if word_count > 0 else 0
    
    return {
        'char_count': char_count,
        'word_count': word_count,
        'line_count': line_count,
        'sentence_count': sentence_count,
        'most_common_words': most_common_words,
        'avg_word_length': round(avg_word_length, 2),
        'reading_time': round(reading_time, 1),
        'unique_words': len(set(words))
    }

# Feedback system with actual functionality
@app.route('/feedbacks', methods=['GET', 'POST'])
def feedbacks_page():
    """Feedbacks page with actual form processing"""
    message = None
    message_type = None
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message_text = request.form.get('message', '').strip()
        
        if name and email and message_text:
            # Basic email validation
            if '@' in email and '.' in email:
                feedback = {
                    'id': len(feedbacks) + 1,
                    'name': name,
                    'email': email,
                    'message': message_text,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                feedbacks.append(feedback)
                message = "Thank you for your feedback! It has been submitted successfully."
                message_type = "success"
            else:
                message = "Please enter a valid email address."
                message_type = "error"
        else:
            message = "Please fill in all required fields."
            message_type = "error"
    
    return render_template('feedbacks.html',
                         title='Feedback',
                         feedbacks=feedbacks,
                         message=message,
                         message_type=message_type,
                         timestamp=datetime.now())

# API Routes (JSON endpoints)
@app.route('/api/info')
def api_info():
    """API information endpoint (JSON)"""
    return jsonify({
        "name": sample_data["name"],
        "version": sample_data["version"],
        "description": sample_data["description"],
        "author": sample_data["author"],
        "github": sample_data["github"],
        "endpoints": sample_data["endpoints"],
        "status": "active",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/students', methods=['GET'])
def get_students():
    """Get all students (JSON)"""
    filtered_students = students.copy()
    
    country = request.args.get('country')
    if country:
        filtered_students = [s for s in filtered_students if s['country'].lower() == country.lower()]
    
    city = request.args.get('city')
    if city:
        filtered_students = [s for s in filtered_students if s['city'].lower() == city.lower()]
    
    return jsonify({
        "students": filtered_students,
        "count": len(filtered_students),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get a specific student by ID (JSON)"""
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify({
            "student": student,
            "timestamp": datetime.now().isoformat()
        })
    else:
        return jsonify({
            "error": "Student not found",
            "timestamp": datetime.now().isoformat()
        }), 404

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """Get all courses (JSON)"""
    return jsonify({
        "courses": courses,
        "count": len(courses),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Get a specific course by ID (JSON)"""
    course = next((c for c in courses if c['id'] == course_id), None)
    if course:
        return jsonify({
            "course": course,
            "timestamp": datetime.now().isoformat()
        })
    else:
        return jsonify({
            "error": "Course not found",
            "timestamp": datetime.now().isoformat()
        }), 404

@app.route('/api/posts', methods=['GET'])
def get_posts():
    """Get all blog posts (JSON)"""
    return jsonify({
        "posts": posts,
        "count": len(posts),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """Get a specific post by ID (JSON)"""
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return jsonify({
            "post": post,
            "timestamp": datetime.now().isoformat()
        })
    else:
        return jsonify({
            "error": "Post not found",
            "timestamp": datetime.now().isoformat()
        }), 404

@app.route('/api/feedbacks', methods=['GET', 'POST'])
def api_feedbacks():
    """API endpoint for feedbacks"""
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({
                "error": "No JSON data provided",
                "timestamp": datetime.now().isoformat()
            }), 400
        
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        if not all([name, email, message]):
            return jsonify({
                "error": "Missing required fields: name, email, message",
                "timestamp": datetime.now().isoformat()
            }), 400
        
        feedback = {
            'id': len(feedbacks) + 1,
            'name': name,
            'email': email,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        feedbacks.append(feedback)
        
        return jsonify({
            "message": "Feedback submitted successfully",
            "feedback": feedback,
            "timestamp": datetime.now().isoformat()
        }), 201
    
    # GET request
    return jsonify({
        "feedbacks": feedbacks,
        "count": len(feedbacks),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get API statistics (JSON)"""
    return jsonify({
        "statistics": {
            "total_students": len(students),
            "total_courses": len(courses),
            "total_posts": len(posts),
            "total_feedbacks": len(feedbacks),
            "countries": list(set(student['country'] for student in students)),
            "cities": list(set(student['city'] for student in students))
        },
        "timestamp": datetime.now().isoformat()
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    if request.path.startswith('/api/'):
        return jsonify({
            "error": "Endpoint not found",
            "message": "The requested API endpoint does not exist",
            "timestamp": datetime.now().isoformat()
        }), 404
    return render_template('404.html', title='Page Not Found'), 404

@app.errorhandler(500)
def internal_error(error):
    if request.path.startswith('/api/'):
        return jsonify({
            "error": "Internal server error",
            "message": "Something went wrong on our side",
            "timestamp": datetime.now().isoformat()
        }), 500
    return render_template('500.html', title='Server Error'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)