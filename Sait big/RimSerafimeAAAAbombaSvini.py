from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('Logout.html')



@app.route("/Main", endpoint='Main')
def Main_Page():
    return render_template('Main.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
    
    