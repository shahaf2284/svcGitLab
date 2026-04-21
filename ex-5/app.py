from flask import Flask, render_template, jsonify

# Create application
app = Flask(__name__)

# 1. Create the first page (index)
@app.route('/')
def index():
    # Looks for file in templates/index.html
    return render_template('index.html')

# 2. Add Health-Check Route (Task requirement)
@app.route('/health')
def health_check():
    # Returns a JSON response with status 200 and "ok"
    return "ok", 200

if __name__ == '__main__':
    # debug=True restarts automatically when changes are made
    app.run(debug=True)
