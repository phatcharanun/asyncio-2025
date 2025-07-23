from flask import Flask, render_template, request
import asyncio  # Used for async operations like sleeping or async I/O

# Create the Flask application
app = Flask(__name__)

# Define the root route ("/") as an asynchronous function
@app.route("/")
async def index():
    # Render the HTML template with default name "World"
    # Note: render_template is synchronous and should NOT be awaited
    return render_template("index.html", name="World")

# Define the /hello route to handle GET requests asynchronously
@app.route("/hello")
async def hello():
    # Retrieve the 'name' value from the URL query string (?name=YourName)
    # Default to "World" if no name is provided
    name = request.args.get("name", "World")
    
    # Simulate an async I/O task (e.g., waiting for a database or API)
    await asyncio.sleep(1)  # จำลองงาน async
    # Return the template with the provided name
    return render_template("index.html", name=name)

# Run the app when this script is executed directly
if __name__ == "__main__":
    # Start the Flask development server with debug mode on, using port 50000
    app.run(debug=True, port=50000)
