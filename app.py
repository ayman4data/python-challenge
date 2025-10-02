from flask import Flask, jsonify, request
import json
import os
from datetime import datetime

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
        "posts": "/api/posts"
    }
}

# Sample students data
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

# Sample courses data
courses = [
    {
        "id": 1,
        "name": "Python Programming",
        "description": "Learn Python from scratch",
        "duration": "30 days",
        "price": "Free"
    },
    {
        "id": 2,
        "name": "Web Development",
        "description": "Build web applications with Python",
        "duration": "45 days",
        "price": "Free"
    },
    {
        "id": 3,
        "name": "Data Science",
        "description": "Data analysis and visualization",
        "duration": "60 days",
        "price": "Free"
    }
]

# Sample posts data
posts = [
    {
        "id": 1,
        "title": "Getting Started with Python",
        "content": "Python is a powerful programming language...",
        "author": "John Doe",
        "date": "2024-01-15",
        "tags": ["python", "beginners", "programming"]
    },
    {
        "id": 2,
        "title": "Flask Web Development",
        "content": "Flask is a micro web framework for Python...",
        "author": "Jane Smith",
        "date": "2024-01-20",
        "tags": ["flask", "web", "python"]
    }
]

@app.route('/')
def home():
    """Home endpoint with API information"""
    return jsonify({
        "message": "Welcome to Thirty Days of Python API",
        "version": sample_data["version"],
        "description": sample_data["description"],
        "endpoints": sample_data["endpoints"],
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api')
def api_info():
    """API information endpoint"""
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
    """Get all students or filter by query parameters"""
    # Filtering capability
    filtered_students = students.copy()
    
    # Filter by country if provided
    country = request.args.get('country')
    if country:
        filtered_students = [s for s in filtered_students if s['country'].lower() == country.lower()]
    
    # Filter by city if provided
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
    """Get a specific student by ID"""
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
    """Get all courses"""
    return jsonify({
        "courses": courses,
        "count": len(courses),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Get a specific course by ID"""
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
    """Get all blog posts"""
    return jsonify({
        "posts": posts,
        "count": len(posts),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """Get a specific post by ID"""
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

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get API statistics"""
    return jsonify({
        "statistics": {
            "total_students": len(students),
            "total_courses": len(courses),
            "total_posts": len(posts),
            "countries": list(set(student['country'] for student in students)),
            "cities": list(set(student['city'] for student in students))
        },
        "timestamp": datetime.now().isoformat()
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint not found",
        "message": "The requested endpoint does not exist",
        "timestamp": datetime.now().isoformat()
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Internal server error",
        "message": "Something went wrong on our side",
        "timestamp": datetime.now().isoformat()
    }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)