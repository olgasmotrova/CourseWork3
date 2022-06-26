from project.config import DevelopmentConfig
from project.server import create_app, db
from project.dao.models import GenreModel

app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": GenreModel,
    }
