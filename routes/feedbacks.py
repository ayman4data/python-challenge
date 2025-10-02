from flask import Blueprint, jsonify, request

feedbacks_bp = Blueprint("feedbacks", __name__)

feedbacks = []
next_feedback_id = 1

@feedbacks_bp.route("/", methods=["GET"])
def get_feedbacks():
    return jsonify(feedbacks)

@feedbacks_bp.route("/", methods=["POST"])
def add_feedback():
    global next_feedback_id
    data = request.get_json()
    if not data or "name" not in data or "message" not in data:
        return jsonify({"error": "Missing name or message"}), 400
    feedback = {"id": next_feedback_id, **data}
    feedbacks.append(feedback)
    next_feedback_id += 1
    return jsonify(feedback), 201
