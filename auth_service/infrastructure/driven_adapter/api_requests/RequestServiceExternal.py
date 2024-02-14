import json
import requests
import xml.etree.ElementTree as ET

from auth_service.domain.services import AESCipher

class RequestService:
    def __init__(self, apiUrl, body, params, soapAction):
        self.apiUrl = apiUrl
        self.soapAction = soapAction
        self.body = body
        self.params = params
    
    def authenticate(self):
        headers = {
            "Content-Type": "text/xml",
            "SOAPAction": self.soapAction,
        }
        response = requests.post(self.apiUrl, data=self.parse_body().encode("utf-8"), headers=headers)
        soap_response = response.text
        root = ET.fromstring(soap_response)
        result_element = root.find(".//{http://tempuri.org/}ValidarUsuarioTokenResult")
        json_response = json.loads(result_element.text)        
        return json_response
        
    
    def parse_body(self):
        parse_body = self.body
        aes_cipher = AESCipher()
        self.params["user"] = aes_cipher.encrypt(self.params["user"])
        self.params["password"] = aes_cipher.encrypt(self.params["password"])
        parse_body = parse_body.replace("{apiKey}", self.params["apiKey"])
        parse_body = parse_body.replace("{appId}", self.params["appId"])
        parse_body = parse_body.replace("{appName}", self.params["appName"])
        parse_body = parse_body.replace("{user}", self.params["user"])
        parse_body = parse_body.replace("{password}", self.params["password"])
        return parse_body


