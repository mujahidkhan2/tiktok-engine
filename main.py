from flask import Flask, render_template, request, jsonify
from engine import TikTokEngine

app = Flask(__name__)
engine = TikTokEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_engine():
    data = request.json
    action = data.get('action')
    
    if action == 'start':
        # یہاں اکاؤنٹس فائل سے ڈیٹا پڑھ کر چیک کرنے کا لاجک آئے گا
        return jsonify({"status": "success", "message": "Engine started successfully!"})
    
    return jsonify({"status": "error", "message": "Invalid action"})

@app.route('/stats')
def stats():
    return jsonify(engine.get_stats())

if __name__ == '__main__':
    app.run(debug=True)