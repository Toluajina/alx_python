"""
Flask web application with six routes.
"""

from flask import Flask, render_template_string

app = Flask(__name__)

# ... other routes ...

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('templates/5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
