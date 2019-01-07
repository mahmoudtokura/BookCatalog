from src.app import create_app
from src.config.dev import DevelopmentConfig

dev_config = DevelopmentConfig()


app = create_app(config=dev_config)

if __name__ == "__main__":
    app.run(debug=True)