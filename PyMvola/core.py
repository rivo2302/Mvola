# -*- coding: utf-8 -*-
import json
import requests 

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
    
    def generate_token(self) :

        """
        A function to generate a token for the Mvola API.
        """ 
        
        url = 'https://api.mvola.mg/token' if self.type == "PRODUCTION"  else "https://devapi.mvola.mg/token"
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'no-cache',
            'Authorization': f'Basic Base64({self.key}:{self.secret})'
        }
        data = {
            'grant_type' : 'client_credentials',
            'scope' : 'EXT_INT_MVOLA_SCOPE'
        }

        req = requests.post(
            url ,
            headers=headers ,
            data=data
        )
        status_code = req.status_code
        response = req.json()
        print(response)

        
