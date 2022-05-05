# -*- coding: utf-8 -*-
import json
import requests 
import base64

from .utils import ResultGetToken

class API :

    def __init__(self,consumer_key,consumer_secret,statut="SANDBOX") -> None :

        """
        An API that will make it easier for you to manage 
        your Mvola API.

        Args:
            consumer_key ( str ): Consumer key of the application's API
            consumer_secret (str ): Consumer secret of the application's API
            statut (str, optional): The status of your API (SANDBOX : Developer Mode / PRODUCTION : Api deployé). Defaults to "SANDBOX".
        """

        self.key = consumer_key
        self.secret = consumer_secret
        self.type = statut
        self.token = None
    
    def generate_token(self) :

        """
        A function to generate a token for the Mvola API.
        """    
        url = 'https://api.mvola.mg/token' if self.type == "PRODUCTION"  else "https://devapi.mvola.mg/token"
        
        keys = f"{self.key}:{self.secret}"
        keys_bytes = keys.encode("ascii")
        encoded = base64.b64encode(keys_bytes).decode("utf-8") 

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'no-cache',
            'Authorization': f'Basic {encoded}'
        }
        data = {
            'grant_type' : 'client_credentials',
            'scope' : 'EXT_INT_MVOLA_SCOPE'
        }
        res = ResultGetToken()
        try :
            req = requests.post(
                url ,
                headers=headers ,
                data=data
            )
        except Exception as e :
            res.error = e
            return res
        status_code = req.status_code
        if status_code == 200:
            res.success = True
            response = req.json()
            res.value = response
            res.token = response["access_token"]

        elif status_code in range (500,504) :
            res.error = {'error_description': 'Internal server errors.', 'error': 'server errors'}

        else :
            res.error = req.json()

        res.status_code = req.status_code
        return res
        
    
