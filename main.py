from flask import Flask, request, jsonify
from modules.sheets import save_memory, get_recent_memories_for_prompt

app = Flask(__name__)

@app.route("/")
def index():
    return "🧠 API Memory – Thiên Cơ & Tiểu Thiên"

@app.route("/memories", methods=["GET", "POST"])
def memories():
    if request.method == "GET":
        user_id = request.args.get("user_id")
        limit = int(request.args.get("limit", 3))
        mems = get_recent_memories_for_prompt(user_id, limit=limit)
        return jsonify({"memories_text": mems})
    else:
        data = request.json
        save_memory(data["user_id"], data["content"], data.get("note_type", "khác"))
        return jsonify({"status": "saved"})

if __name__ == "__main__":
    app.run()
