from flask import Blueprint, jsonify, request
from collections import Counter
import re

text_bp = Blueprint("text", __name__)

def clean_text(text):
    return re.sub(r"[^A-Za-z0-9\s]", "", text).lower()

@text_bp.route("/analyze", methods=["POST"])
def analyze_text():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400
    raw = data["text"]
    cleaned = clean_text(raw)
    words = cleaned.split()
    freq = Counter(words).most_common(5)
    return jsonify({
        "characters_count": len(raw),
        "words_count": len(words),
        "most_common_words": freq
    })
