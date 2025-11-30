# api/index.py
from flask import Flask, render_template_string

app = Flask(__name__)




HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask on Vercel</title>              
</head>
<body>
    <h1>Flask is running on Vercel!</h1>
</body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# Necessário para a Vercel
if __name__ == '__main__':
    app.run()