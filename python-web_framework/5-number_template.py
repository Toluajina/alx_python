"""
Flask web application with six routes.
"""

from flask import Flask, render_template_string

app = Flask(__name__)

# ... other routes ...

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    html_content = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Number: {{ n }}</title>\n</head>\n<body>\n<h1>Number: {{ n }}</h1>\n</body>\n</html>'
    return render_template_string(html_content, n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
