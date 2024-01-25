from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route to display 'Hello HBNB!'

    Returns:
        str: Hello HBNB!
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Route to display 'HBNB'

    Returns:
        str: HBNB
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Route to display 'C ' followed by the value of the text variable.

    Args:
        text (str): The text variable.

    Returns:
        str: Formatted string
    """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """
    Route to display 'Python ' followed by the value of the text variable.

    Args:
        text (str): The text variable.

    Returns:
        str: Formatted string
    """
    return 'Python {}'.format(text.replace('_', ' ') or 'is cool')

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Route to display 'n is a number' only if n is an integer.

    Args:
        n (int): The number.

    Returns:
        str: Formatted string
    """
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route to display an HTML page only if n is an integer.

    Args:
        n (int): The number.

    Returns:
        render_template: HTML page with H1 tag
    """
    return render_template('5-number_template.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
