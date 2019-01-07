from src import db
from src.app import create_app
from src.config.dev import DevelopmentConfig

dev_config = DevelopmentConfig()


app = create_app(config=dev_config)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    app.run()