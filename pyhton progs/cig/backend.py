from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    cigars = [
        {'name': 'Cigar 1', 'description': 'Description 1'},
        {'name': 'Cigar 2', 'description': 'Description 2'},
        {'name': 'Cigar 3', 'description': 'Description 3'}
    ]
    return render_template('index.html', cigars=cigars)

if __name__ == '__main__':
    app.run(debug=True)
