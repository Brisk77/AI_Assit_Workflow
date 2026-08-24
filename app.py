from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def validate_settings(data):
    errors = {}
    display_name = data.get("displayName")
    if not display_name:
        errors["displayName"] = "Display name is required"
    return errors

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/settings", methods=["POST"])
def update_settings():
    data = request.get_json() or {}
    errors = validate_settings(data)
    if errors:
        return jsonify({"errors": errors}), 400
    return jsonify({"status": "saved"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)