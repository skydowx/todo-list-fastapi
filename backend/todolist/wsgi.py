
"""
Web Server Gateway Interaction
App entry point
"""

from app.__init__ import create_app

app_flask = create_app()

if __name__ == "__main__":
    app_flask.run(host="0.0.0.0", port=5050)