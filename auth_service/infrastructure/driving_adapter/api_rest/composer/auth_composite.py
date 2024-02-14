from auth_service.infrastructure.driving_adapter.api_rest.controllers import AuthController

def auth_controller() -> AuthController:
    auth_controller = AuthController()
    return auth_controller