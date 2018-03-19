from flask import Blueprint, url_for
from flask_api import status


blueprint = Blueprint('root_api', __name__)


@blueprint.route("/api")
def index():
    content = dict(
        links=dict(
            self=url_for('.index', _external=True),
        ),
    )

    return content, status.HTTP_200_OK
