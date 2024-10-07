import os
import unittest
from flask.cli import FlaskGroup
from app import blueprint
from app.main import create_app, db
from app.main.model import product, supplier
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

cli = FlaskGroup(app)


@cli.command()
def run():
    app.run(host='0.0.0.0', port=5000, debug=True)


@cli.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    cli()