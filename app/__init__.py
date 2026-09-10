import os

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from app.gmail import(
    is_gmail__command,
    extract_email,
    create_gmail_url,
    generate_email_with_gemini
)

from app.youtube import youtube_bp


def create_app():

    app = Flask(__name__)
    CORS(app)

    # Youtube
    app.register_blueprint(
        youtube_bp,
        url_prefix="/youtube"
    )

    # Home
    @app.route("/")
    def home():
        return render_template("index.html")

    # HTML
    @app.route("/html")
    def html():
        return render_template("index.html")

    # Health
    @app.route("/health")
    def health():
        return jsonify({
            "status" : "ok",
           
#Gmail AI Agent
@app.route("/agent", methods=["POST"])
 def agent():
     try: 
            data = request.get_json(silent=True) or {}
            command = data.get("command", "").strip()

            if not command:
            return jsonify({{
            "success":False,
            "message": "Command is required"
            }), 400
         
recipient = extract_email_with gemini_(command)

return jsonify({
    "success": True,
    "type": "email",
    "email_generated": True,
    "reciepiennt": recipient,
    "subject": email["subject"],
    "gmail_url": create_gmail_url(
        email["subject"]
        email["body"]
        recipient 

    )
})

except Exception as e:

return jsonify({
    "successs": False,
    "message": str(e)
}), 500
return app
