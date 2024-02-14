from flask import jsonify, Blueprint, request

from shared.adapter import flask_adapter
from auth_service.infrastructure.driving_adapter.api_rest.composer import auth_controller
api_routes_bp = Blueprint("api_routes_auth", __name__)

@api_routes_bp.route("/api/v1/auth", methods=["POST"])
async def auth():
    
    response = await flask_adapter(request=request, api_route=auth_controller())

    return jsonify({
                "status" : response.json().get("status"),
                "code" : response.status_code,
                "message" : response.json().get('message'),
                "data" : response.json().get("data")
            }), response.status_code
