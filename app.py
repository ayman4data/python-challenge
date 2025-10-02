from flask import Flask, jsonify, render_template, request
from routes.students import students_bp
from routes.feedbacks import feedbacks_bp
from routes.text import text_bp

app = Flask(__name__)

# Register blueprints for API
app.register_blueprint(students_bp, url_prefix="/api/students")
app.register_blueprint(feedbacks_bp, url_prefix="/api/feedbacks")
app.register_blueprint(text_bp, url_prefix="/api/text")

# Web pages (HTML interface)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/students")
def students_page():
    return render_template('students.html')

@app.route("/feedbacks")
def feedbacks_page():
    return render_template('feedbacks.html')

@app.route("/text-analyzer")
def text_analyzer_page():
    return render_template('text_analyzer.html')

# API endpoint for checking API status
@app.route("/api")
def api_info():
    return jsonify({
        "message": "Welcome to 30 Days Of Python API",
        "version": "1.0",
        "endpoints": {
            "students": "/api/students",
            "feedbacks": "/api/feedbacks",
            "text_analysis": "/api/text/analyze"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)