from flask import Flask
from app.model import db
from app.router.route import routes
from app.config import Config

# Initialize
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(routes)

with app.app_context():
    # db.drop_all()
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
