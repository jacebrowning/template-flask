import os

from flask_script import Manager, Server

from {{cookiecutter.project_name}}.settings import get_config
from {{cookiecutter.project_name}}.factory import create_app


def find_assets():
    """Yield paths for all static files and templates."""
    for name in ['static', 'templates']:
        directory = os.path.join(app.config['PATH'], name)
        for entry in os.scandir(directory):
            if entry.is_file():
                yield entry.path


config = get_config(os.getenv('FLASK_ENV'))

app = create_app(config)

server = Server(extra_files=find_assets())

manager = Manager(app)
manager.add_command('run', server)


if __name__ == '__main__':
    manager.run()
