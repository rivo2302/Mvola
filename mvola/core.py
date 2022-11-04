# -*- coding: utf-8 -*-

import json
import requests
import base64
from os import environ as env
from .tools import ResultAction


class Mvola:
    def __init__(
        self,
        consumer_key: str = env.get("CONSUMER_KEY"),
        consumer_secret: str = env.get("SECRET_KEY"),
        status: str = "SANDBOX",
        token: str = None,
    ):
        """
        An API that will make it easier for you to manage
        your Mvola API.

        Args:
            consumer_key ( str ): Consumer key of the application's API
            consumer_secret (str ): Consumer secret of the application's API
            status (str, optional): The status of your API
            (SANDBOX : Developer Mode / PRODUCTION : Api deployé)
        """

        if not consumer_key:
            raise Exception("Missing CONSUMER_KEY in env")
        if not consumer_secret:
            raise Exception("Missing SECRET_KEY in env")

        self.key = consumer_key
        self.secret = consumer_secret
        self.type = status
        self.token = token

        self.url = (
            "https://api.mvola.mg"
            if self.type == "PRODUCTION"
            else "https://devapi.mvola.mg"
        )

    def generate_token(self):
        """
        A function to generate a token for the Mvola API.
        """
        url = f"{self.url}/token"
        keys = f"{self.key}:{self.secret}"
        keys_bytes = keys.encode("ascii")
        encoded = base64.b64encode(keys_bytes).decode("utf-8")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
            "Authorization": f"Basic {encoded}",
        }
        data = {
            "grant_type": "client_credentials",
            "scope": "EXT_INT_MVOLA_SCOPE",
        }
        res = ResultAction()
        try:
            req = requests.post(url, headers=headers, data=data)
        except Exception as e:
            res.error = e
            return res
        status_code = req.status_code
        if status_code == 200:
            res.success = True
            response = req.json()
            res.response = response
            res.response = response["access_token"]
        elif status_code in range(500, 504):
            res.error = {
                "description": "Internal Server error",
                "detail": req.text,
            }
        else:
            res.error = req.json()
        res.status_code = status_code
        return res

    def init_transaction(self, transaction):

        """
        A method to calculate initiate a transaction with your Mvola API.
        Args:
            transaction ( object : Transaction ): An instance of Transaction class.
        """
        url = f"{self.url}/mvola/mm/transactions/type/merchantpay/1.0.0/"
        res = ResultAction()
        data = transaction.dataJson
        if not data.get("amount"):
            raise ValueError(
                " Mvola Error  : [amount] Required fields on action :"
                " init_transaction"
            )

        if not data.get("descriptionText"):
            raise ValueError(
                " Mvola Error  : [description_text] Required fields on action"
                " : init_transaction"
            )

        if not data.get("requestDate"):
            raise ValueError(
                " Mvola Error  : [description_text] Required fields on action"
                " : init_transaction"
            )

        if not data["debitParty"][0].get("value"):
            raise ValueError(
                " Mvola Error  : [debit] Required fields on action :"
                " init_transaction"
            )

        if not data["creditParty"][0].get("value"):
            raise ValueError(
                " Mvola Error  : [credit] Required fields on action :"
                " init_transaction"
            )

        if not data.get("originalTransactionReference"):
            raise ValueError(
                " Mvola Error  : [original_transaction_reference] Required"
                " fields on action : init_transaction"
            )

        if not data.get("requestingOrganisationTransactionReference"):
            raise ValueError(
                " Mvola Error  :"
                " [requesting_organisation_transaction_reference] Required"
                " fields on acion : init_transaction"
            )

        for k, v in dict(data).items():
            if k not in [
                "amount",
                "currency",
                "descriptionText",
                "requestDate",
                "originalTransactionReference",
                "debitParty",
                "creditParty",
                "metadata",
                "requestingOrganisationTransactionReference",
            ]:
                del data[k]
        try:
            req = requests.post(
                url, headers=transaction.headers, data=json.dumps(data)
            )
        except Exception as e:
            res.error = e
            return res
        status_code = req.status_code
        if status_code in [200, 202]:
            res.success = True
            response = req.json()
            res.response = response
        elif status_code in range(500, 504):
            res.error = {
                "error_description": "Internal server errors.",
                "error": "server errors",
            }
        else:
            res.error = req.json()
        res.status_code = req.status_code
        return res

    def status_transaction(self, transaction):

        """
        Status of transaction

        Args:
            transaction ( object : Transaction ): An instance of Transaction class.
        """

        url = (
            f"{self.url}/mvola/mm/transactions/type/merchantpay/1.0.0/status/"
        )
        res = ResultAction()

        data = transaction.dataJson
        if not data.get("serverCorrelationId"):
            raise ValueError(
                " Mvola Error  : [server_correlation_id] Required fields on"
                " action : status_transaction"
            )

        url = f"{url}/{data.get('serverCorrelationId')}"
        try:
            req = requests.get(url, headers=transaction.headers)
        except Exception as e:
            res.error = e
            return res

        status_code = req.status_code
        if status_code in [200, 202]:
            res.success = True
            response = req.json()
            res.response = response

        elif status_code in range(500, 504):
            res.error = {
                "error_description": "Internal server errors.",
                "error": "server errors",
            }

        else:
            res.error = req.json()

        res.status_code = req.status_code
        return res

    def details_transaction(self, transaction):

        """
        details of transaction

        Args:
            transaction ( object : Transaction ): An instance of Transaction class.
        """
        url = f"{self.url}/mvola/mm/transactions/type/merchantpay/1.0.0"
        res = ResultAction()
        data = transaction.dataJson

        if not data.get("transid"):
            raise ValueError(
                " Mvola Error  : [transid] Required fields on acion : details"
                " of transaction"
            )

        try:
            req = requests.get(
                f'{url}/{data.get("transid")}', headers=transaction.headers
            )
        except Exception as e:
            res.error = e
            return res

        status_code = req.status_code
        if status_code in [200, 202]:
            res.success = True
            response = req.json()
            res.response = response

        elif status_code in range(500, 504):
            res.error = {
                "error_description": "Internal server errors.",
                "error": "server errors",
            }

        else:
            res.error = req.json()

        res.status_code = req.status_code
        return res
