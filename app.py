from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from auth_service.infrastructure.driving_adapter.api_rest.routes import api_routes_bp as api_auth
load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(api_auth)


if '__main__' == __name__:
    app.run(host=os.getenv("HOST_PY"), port=int(os.getenv("PORT_PY")), debug=False)
