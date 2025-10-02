from flask import Blueprint, jsonify, request

students_bp = Blueprint("students", __name__)

students = []
next_student_id = 1

@students_bp.route("/", methods=["GET"])
def get_students():
    return jsonify(students)

@students_bp.route("/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student)

@students_bp.route("/", methods=["POST"])
def add_student():
    global next_student_id
    data = request.get_json()
    required = ["name", "dob", "country", "city", "skills", "bio"]
    if not data or not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400
    student = {"id": next_student_id, **data}
    students.append(student)
    next_student_id += 1
    return jsonify(student), 201
