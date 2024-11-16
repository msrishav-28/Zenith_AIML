import sys
import os

# Print Python's module search paths for debugging (optional, can be removed after testing)
print("Python module search paths:", sys.path)

# Add the "app" directory to the Python module search path
app_path = os.path.join(os.path.dirname(__file__), "app")
if app_path not in sys.path:
    sys.path.append(app_path)

# Import create_app from the app_setup module inside the app folder
try:
    from app.app_setup import create_app
except ModuleNotFoundError as e:
    print("Error: Could not find 'app_setup' module. Make sure 'app/app_setup.py' exists.")
    raise e

# Create the Flask app instance
app = create_app()

# Run the Flask application
if __name__ == '__main__':
    # Ensure the app runs in debug mode for development
    app.run(debug=True)
