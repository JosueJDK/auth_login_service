from typing import Type
from httpx import Request, Response
from auth_service.infrastructure.driven_adapter.api_requests import RequestService

class AuthController:

    def __init__(self):
        pass

    async def route(self, http_request: Type[Request]) -> Response:
        try:
            body_params = http_request.json.keys()
            
            _apiUrl = http_request.json['apiUrl'] if 'apiUrl' in body_params else False
            _soapAction = http_request.json['soapAction'] if 'soapAction' in body_params else False
            _body = http_request.json['body'] if 'body' in body_params else False
            _params  = http_request.json['params'] if 'params' in body_params else False

            if (_apiUrl and
                _soapAction and
                _body and
                _params
            ):
                requestService = RequestService(
                    apiUrl=_apiUrl,
                    soapAction=_soapAction,
                    body=_body,
                    params=_params,
                )
                responseService = requestService.authenticate()
                if (not responseService["DATOS_USUARIO"] == None and not  responseService["TOKEN"] == None):
                    return self.success_response("AUTH_SUCCESS", responseService["DATOS_USUARIO"][0])
                return self.bad_request("Credenciales Incorrectas")
                
            else:
                return self.bad_request("Todos los campos son requeridos.")
                
            
        except Exception as e:
            return self.server_error(str(e))

    @staticmethod
    def bad_request(message):
        return Response(status_code=400, json={"status" : "error", "message": message, "data": None})

    @staticmethod
    def success_response(message, data=None):
        return Response(status_code=200, json={"status" : "success", "message": message, "data": data})

    @staticmethod
    def server_error(message):
        return Response(status_code=500, json={"status" : "error", "message": message, "data": None})
