from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('read_marks.html')

@app.route('/result', methods = ['POST', 'GET'])
def resulr():
    if request.method == 'POST':
        phy = int(request.form['phy'])
        che = int(request.form['chem'])
        mat = int(request.form['math'])
        avg = (phy+che+mat)/3
        return render_template('result.html', result = avg)

if __name__ == '__main__':
    app.run(debug=True)