from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    text = ""

    if request.method == "POST":
        text = request.form.get("text")
        mode = request.form.get("mode")

        prompt = f"""
Improve the following text:
Instruction: {mode}

Text:
{text}
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        output = response.json()["response"]
        text = ""

    return render_template("index.html", output=output, text=text)
import os
if __name__ == "__main__":
    port =int(os.environ.get("PORT") or 10000)
    app.run(host="0.0.0.0",port=port)