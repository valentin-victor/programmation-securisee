from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    avis = request.form['avis']

    return render_template('avis.html', avis=avis)

if __name__ == '__main__':
    app.run()
