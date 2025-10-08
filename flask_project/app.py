from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaofcircle', methods=['GET', 'POST'])
def areaofcircle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            result = 3.1416 * (radius ** 2)
        except ValueError:
            result = "Invalid input"
    return render_template('areaofcircle.html', result=result)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def areaoftriangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            result = 0.5 * base * height
        except ValueError:
            result = "Invalid input"
    return render_template('areaoftriangle.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
