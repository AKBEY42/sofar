from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "OK",
        "message": "SÖFAR Lojistik Yönetim Sistemi Çalışıyor"
    })

if __name__ == "__main__":
    app.run()
