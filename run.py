import os

from waitress import serve

from app import create_app


app = create_app()
port = os.getenv('PORT', 5000)

# listen on ipv4 and ipv6
serve(app, listen=f'*:{port}')
