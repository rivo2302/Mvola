# -*- coding: utf-8 -*-

import json
import requests 
import base64

from .tools import ResultAction

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
        res = ResultAction()
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
        
    def init_transaction (self,transaction) :

        """
        A method to calculate initiate a transaction with your Mvola API.   

        Args:
            transaction ( object : Transaction ): An instance of Transaction class.
        """

        url = "https://devapi.mvola.mg/mvola/mm/transactions/type/merchantpay/1.0.0/"
        res = ResultAction()
        data = transaction.dataJson

        if not data.get("amount") :
            raise ValueError("[amount] Required fields on action : init_transaction")

        if not data.get("descriptionText") :
            raise ValueError("[descriptionText] Required fields on action : init_transaction")
        
        if not data.get("requestDate") :
            raise ValueError("[requestDate] Required fields on action : init_transaction")

        if not data["debitParty"][0].get("value") :
            raise ValueError("[debit] Required fields on action : init_transaction")

        if not data["creditParty"][0].get("value") :
            raise ValueError("[credit] Required fields on action : init_transaction")

        if not data.get("originalTransactionReference") :
            raise ValueError("[originalTransactionReference] Required fields on action : init_transaction")

        if not data.get("requestingOrganisationTransactionReference"):
            raise ValueError("[requestingOrganisationTransactionReference] Required fields on acion : init_transaction")

        for k, v in dict(data).items():
            if k not in ["amount","currency","descriptionText","requestDate","originalTransactionReference","debitParty","creditParty","metadata","requestingOrganisationTransactionReference"]:
                del data[k]
        try :
            req = requests.post(
                url ,
                headers=transaction.headers,
                data=json.dumps(data)
            )
        except Exception as e :
            res.error = e
            return res
        status_code = req.status_code
        if status_code in [200 , 202]:
            res.success = True
            response = req.json()
            res.value = response
        elif status_code in range (500,504) :
            res.error = {'error_description': 'Internal server errors.', 'error': 'server errors'}
        else :
            res.error = req.json()
        res.status_code = req.status_code
        return res
        
    def status_transaction(self,transaction) :

        """
        Status of transaction

        Args:
            transaction ( object : Transaction ): An instance of Transaction class.
        """

        url = "https://devapi.mvola.mg/mvola/mm/transactions/type/merchantpay/1.0.0/status/"
        res = ResultAction()

        data = transaction.dataJson
        if not data.get("serverCorrelationId") :
            raise ValueError("[serverCorrelationId] Required fields on action : status_transaction")
        
        url = f"{url}/{data.get('serverCorrelationId')}"
        try :
            req = requests.get(
                url ,
                headers=transaction.headers
            )
        except Exception as e :
            res.error = e
            return res

        status_code = req.status_code
        if status_code in [200 , 202]:
            res.success = True
            response = req.json()
            res.value = response

        elif status_code in range (500,504) :
            res.error = {'error_description': 'Internal server errors.', 'error': 'server errors'}

        else :
            res.error = req.json()
            
        res.status_code = req.status_code
        return res