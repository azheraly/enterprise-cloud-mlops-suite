from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        print("Form submitted", request.form)
        name = request.form.get("name")
        message = f"Hello {name}, Welcome to the Kubernetes test application!!!"
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)