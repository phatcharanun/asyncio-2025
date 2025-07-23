from flask import Flask, render_template, request

# Create a Flask application instance
app = Flask(__name__)

# Define the home route (root URL "/")
@app.route("/")
def home():
    # Render the HTML template and pass the default name "World"
    return render_template("index.html", name="World")

# Define the /hello route, which accepts GET requests from the form
@app.route("/hello", methods=["GET"])
def hello():
    # Get the 'name' parameter from the URL query string (e.g., ?name=Alice)
    # If no name is provided, default to "World"
    name = request.args.get("name", "World")
    # Render the same template with the name provided by the user
    return render_template("index.html", name=name)

# Run the app if this file is executed directly
if __name__ == "__main__":
    # Start the development server on port 50000 with debug mode enabled
    app.run(debug=True, port=50000)
