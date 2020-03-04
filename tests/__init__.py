from app import create_app

test_app = create_app()
test_app.config['TESTING'] = True
