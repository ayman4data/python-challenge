from flask import Flask, jsonify
from routes.students import students_bp
from routes.feedbacks import feedbacks_bp
from routes.text import text_bp

app = Flask(__name__)

# Config for MongoDB (replace with your Mongo URI if using Atlas)
app.config["MONGO_URI"] = "mongodb://localhost:27017/thirtyday_api"

# Register blueprints (modular routes)
app.register_blueprint(students_bp, url_prefix="/api/students")
app.register_blueprint(feedbacks_bp, url_prefix="/api/feedbacks")
app.register_blueprint(text_bp, url_prefix="/api/text")

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the 30 Days of Python API",
        "endpoints": ["/api/students", "/api/feedbacks", "/api/text/analyze"]
    })

if __name__ == "__main__":
    app.run(debug=True)

