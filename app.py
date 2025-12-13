from flask import Flask

# 1. Create the web application
app = Flask(__name__)

# 2. Keep our logic function (So our unit tests don't break!)
def add(a, b):
    return a + b

# 3. Create the "Home Page" route
@app.route("/")
def home():
    return """
    <html>
        <head>
            <style>
                body { font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #f0f0f0; }
                h1 { color: #333; }
                .box { border: 2px solid #333; padding: 20px; display: inline-block; background-color: white; }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>Hello from Jenkins! 🎩</h1>
                <p>This website was deployed automatically.</p>
                <p>By the way, 2 + 2 is still <b>""" + str(add(2, 2)) + """</b></p>
            </div>
        </body>
    </html>
    """

# 4. Run the web server if this file is executed
if __name__ == "__main__":
    # host='0.0.0.0' is vital for Docker to let us see it from outside
    app.run(host='0.0.0.0', port=5000)
