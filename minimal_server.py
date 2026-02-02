#!/usr/bin/env python3
"""
Minimal Flask test server
"""
import sys
import os

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf-8', errors='replace')

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'AML System Online!\n'


@app.route('/api/status')
def status():
    return {'status': 'OK', 'version': 'v10.0'}


if __name__ == '__main__':
    print("Starting minimal Flask server on 0.0.0.0:5001...")
    print("Visit: http://127.0.0.1:5001")
    print("")
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=False,
        use_reloader=False,
        threaded=False  # Try without threading
    )
