from flask import Flask, render_template

# the App flask
# and render_template mean to present HTML page

""" Create application  (__name__ -> where the app start) """
app = Flask(__name__)

# create the first page
@app.route('/')
def index():
    return render_template('index.html')    # the html file location templates/index.html

if __name__ == '__main__':
    app.run(debug=True)         # debug=True restart atomaticly when do some change.


