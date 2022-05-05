# -*- coding: utf-8 -*-
import json
import requests 
import base64

from .tools import ResultGetToken

class Mvola :

    def __init__(self,consumer_key :str, consumer_secret :str, status:str="SANDBOX") :

        """
        An API that will make it easier for you to manage 
        your Mvola API.

        Args:
            consumer_key ( str ): Consumer key of the application's API
            consumer_secret (str ): Consumer secret of the application's API
            status (str, optional): The status of your API (SANDBOX : Developer Mode / PRODUCTION : Api deployé). Defaults to "SANDBOX".
        """

        self.key = consumer_key
        self.secret = consumer_secret
        self.type = status
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
        
    
    def transaction (self,token:str,payment) :
        """
        
        A method to calculate initiate a transaction with your Mvola API.   

        Args:
            token ( str ): A validate token of your application.
        """

        headers = {
            'Authorization': 'Bearer eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhICIsIm5iZiI6MTY1MTc2OTE5NywiYXpwIjoiMHpMN2VUclNFZlhmNmtrd0o1M0RTZWdDYkJ3YSAiLCJzY29wZSI6IkVYVF9JTlRfTVZPTEFfU0NPUEUiLCJpc3MiOiJodHRwczpcL1wvYXBpbS5wcmVwLnRlbG1hLm1nOjk0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjE2NTE3NzI3OTcsImlhdCI6MTY1MTc2OTE5NywianRpIjoiOGJjN2IyODQtNTE2NC00YWM2LThiNzktZjg4MjZmYzU1ZjI1In0.BUdPFVYwTQFW2Ehhmp45AGYdFu8pYFkinGz9ZATmP0keNnDvbCJOzzxEUum7WK5kNig4vgTtN6Ec4BuC7FMao5MFCJtBLdp_UAKASkKwd3H-lEAEy5PMPc07WOXZwFlkyiCcuzOJOWOqgM5dwZ0QvSF60G8qJrv4oQ79JoLbYoCAs3MqtNPoYO8L-J4vUmiNMMmN5Qy4GqIFNmttEvUy3sRGsPkavCFCwvyscOZgo5TjL-fDSRC8Zk3AzO8UeBezGxNVRxhZ43sWkjU1avVu8HqF0F9KKJow_YGLnZ56mhlKhUIUm9-5J0MkvPY69nAZR8pOU2RmVEn__Rd9qQaMZw',
            'Version': '1.0',
            'UserLanguage': 'FR',
            'X-CorrelationID': 'cbb4e263-9c8c-4470-ba36-7901bab68214',
            'UserAccountIdentifier': 'msisdn;0343500003',
            'partnerName': 'Marketbot',
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache'
        }
    
        data = { 
            "amount": "2000", 
            "currency": "Ar", 
            "descriptionText": "TesteAPI",
            "requestingOrganisationTransactionReference": "trasactiondereference", 
            "requestDate":"2022-05-05T21:14:59.567Z", 
            "originalTransactionReference": "originatex", 
            "debitParty": [{
                "key": "msisdn", 
                "value": "0343500003"
            } ], 
            "creditParty": [
                { 
                    "key": "msisdn", 
                    "value":"0343500004"
                }
            ],
            "metadata": [
                {
                        "key": "partnerName", 
                        "value":"Marketbot" 
                }, 
                { 
                    "key": "fc", 
                    "value": "USD" 
                }, 
                { 
                    "key": "amountFc", 
                    "value": "1" 
                } 
            ]
        }
        url = "https://devapi.mvola.mg/mvola/mm/transactions/type/merchantpay/1.0.0/"
        req = requests.post(
            url ,
            headers=headers,
            data=json.dumps(data)
        )
        print(req.status_code)
        print(req.json())
        
