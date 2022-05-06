# -*- coding: utf-8 -*-

import re
import uuid
import json

class ResultAction :
    """
    Result Action 

    The object to use for each API action (Generate token, transaction,..)
    """
    def __init__(self) -> None:

        self.success =  False # True if the requests is success
        self.error =  None # Details if error occurs
        self.value = None # Content of the request's response
        self.token = None # The value of token
        self.status_code = None # The status code the requests

    def __str__(self) :
        return  str(self.token)
   
class Transaction :
    """Transaction

    The object to use to facilitate error handling on data constraints
    during transactions.
    """

    def __init__ (self ,**kwargs) :

        #Headers 
        self.correlation_id = str(uuid.uuid1())
        self.token = kwargs.get("token")
        self.UserLanguage = kwargs.get("UserLanguage","MG")
        self.UserAccountIdentifier = kwargs.get("UserAccountIdentifier")
        self.partnerName = kwargs.get("partnerName","partnerName")
        self.X_Callback_URL = kwargs.get("X_Callback_URL")

        # Data Json 
        self.amount = kwargs.get("amount", "0")
        self.currency = kwargs.get("currency", "Ar")
        self.descriptionText = kwargs.get("descriptionText", "Description")
        self.requestingOrganisationTransactionReference = kwargs.get("requestingOrganisationTransactionReference","ref_transaction")
        self.requestDate = kwargs.get("requestDate","2025-05-05T21:14:59.567Z")
        self.originalTransactionReference = kwargs.get("originalTransactionReference","refereence" )
        self.debit = kwargs.get("debit")
        self.credit = kwargs.get("credit")
        self.fc = kwargs.get("fc","USD")
        self.amountFc = kwargs.get("amountFc","1")

        if self.UserLanguage.upper() not in ('FR','MG'):
            raise ValueError("[UserLanguage] FR or MG")

        if not self.token :
            raise ValueError("[Token] Requiered fields | MerchantNumber: the company phone number ex : 0343500004")

        if not self.UserAccountIdentifier :
            raise ValueError("[UserAccountIdentifier] Requiered fields | ")

        if re.match((r'^[0-9]{10}$'), self.UserAccountIdentifier) is  None:
            raise ValueError("[UserAccountIdentifier] MerchantNumber: the company phone number ex : 0343500004") 

        if not str(self.amount).isdigit() :     
            raise ValueError("[Amount] of transaction without decimals ,example : 1000,20,15")

        if str(self.currency).capitalize() != 'Ar' :
            raise ValueError("[Currency] code of the transaction - Possible Values : Ar")

        if re.match((r'^[A-Za-z0-9_\-.,;\']{0,50}$'), self.descriptionText) is  None :
            raise ValueError("[Description] on transaction. At most 50 characters long without special character except : “-”, “.”, “_”, “,”")

        if re.match((r'^[A-Za-z0-9_\-.,;\']{0,50}$'), self.requestingOrganisationTransactionReference) is  None   :
            raise ValueError("Transaction ID of client side. At most 50 characters long without special Character except : “-”, “.”, “_”, “,”")

        if re.match((r'^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{2,3}Z$'), self.requestDate) is  None:
            raise ValueError("[requestDate]Transaction requested date by client - yyyy-MM-ddTHH:mm:ss.SSSZ format ,  example = 2022-05-05T21:14:59.567Z")

        if not self.debit :
            raise ValueError("[Debit] Required fields | Phone number of subscriber .In preprod it’s fixed: 034350003 or 0343500004")

        if not self.credit :
            raise ValueError("[Credit] Required fields | Phone number of merchant. In preprod it’s fixed: 034350003 or 0343500004"  )

        if re.match((r'^[0-9]{10}$'), self.debit) is  None: 
            raise ValueError("[Debit]Phone number of subscriber .In preprod it’s fixed: 034350003 or 0343500004")
  
        if re.match((r'^[0-9]{10}$'), self.credit) is  None: 
            raise ValueError("[Credit]Phone number of merchant. In preprod it’s fixed: 034350003 or 0343500004")

    @property
    def headers(self) :
        return {
            'Authorization': f'Bearer {self.token}',
            'Version': '1.0',
            'UserLanguage': str(self.UserLanguage).upper(),
            'X-CorrelationID': self.correlation_id,
            'UserAccountIdentifier': f'msisdn;{self.UserAccountIdentifier}',
            'partnerName': self.partnerName,
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache'
        }
             
    @property
    def dataJson(self):
        return { 
                "amount": str(self.amount), 
                "currency": str(self.currency).capitalize(), 
                "descriptionText": str(self.descriptionText),
                "requestingOrganisationTransactionReference": self.requestingOrganisationTransactionReference, 
                "requestDate":self.requestDate, 
                "originalTransactionReference": self.originalTransactionReference, 
                "debitParty": [{
                    "key": "msisdn", 
                    "value": str(self.debit)
                } ], 
                "creditParty": [
                    { 
                        "key": "msisdn", 
                        "value":str(self.credit)
                    }
                ],
                "metadata": [
                    {
                            "key": "partnerName", 
                            "value":self.partnerName 
                    }, 
                    { 
                        "key": "fc", 
                        "value": str(self.fc) 
                    }, 
                    { 
                        "key": "amountFc", 
                        "value": str(self.amountFc) 
                    } 
                ]
            }
    
    def __str__(self) :
        return str("Main class for transaction.")

  
        