# -*- coding: utf-8 -*-

import re
import uuid
import json

class ResultAction :
    """
    Result Action 

    The object to use for each API action (Generate token, Initiate transaction, status transaction,...)
    """
    def __init__(self) -> None:

        self.success =  False # True if the requests is success
        self.error =  None # Details if error occurs
        self.value = None # Content of the request's response
        self.token = None # The value of token
        self.status_code = None # The status code the requests

    def __str__(self) :
        return  json.dumps({
                "Success" : self.success,
                "Error" : self.error,
                "Status code" : self.status_code,
                "Value" : self.value
            },indent=4)
   
class Transaction :
    """Transaction

        The object to use to check easier error handling on data constraints
        during each transactions.
    """

    def __init__ (self ,**kwargs) :

        #Headers 
        self.correlation_id = str(uuid.uuid1())
        self.token = kwargs.get("token")
        self.UserLanguage = kwargs.get("UserLanguage","FR")
        self.UserAccountIdentifier = kwargs.get("UserAccountIdentifier")
        self.partnerName = kwargs.get("partnerName")
        self.X_Callback_URL = kwargs.get("X_Callback_URL")

        # Data Json 
        self.amount = kwargs.get("amount")
        self.currency = kwargs.get("currency", "Ar")
        self.descriptionText = kwargs.get("descriptionText")
        self.requestingOrganisationTransactionReference = kwargs.get("requestingOrganisationTransactionReference")
        self.requestDate = kwargs.get("requestDate")
        self.originalTransactionReference = kwargs.get("originalTransactionReference")
        self.debit = kwargs.get("debit")
        self.credit = kwargs.get("credit")
        self.fc = kwargs.get("fc","USD")
        self.amountFc = kwargs.get("amountFc","1")
        self.serverCorrelationId = kwargs.get("serverCorrelationId")

        if not self.token :
            raise ValueError("[Token] Required fields | MerchantNumber: the company phone number ex : 0343500004")

        if not self.UserAccountIdentifier :
            raise ValueError("[UserAccountIdentifier] Required fields ")

        if self.UserLanguage.upper() not in ('FR','MG'):
            raise ValueError("[UserLanguage] FR or MG")

        if not self.partnerName :
            raise ValueError("[partnerName] Required fields")

        if self.amount :
            if not str(self.amount).isdigit() :     
                raise ValueError("[Amount] of transaction without decimals ,example : 1000,20,15")

        if str(self.currency).capitalize() != 'Ar' :
            raise ValueError("[Currency] code of the transaction - Possible Values : Ar")
                
        if re.match((r'^[0-9]{10}$'), self.UserAccountIdentifier) is  None:
            raise ValueError("[UserAccountIdentifier] MerchantNumber: the company phone number ex : 0343500004") 

        if self.descriptionText :
            if re.match((r'^[A-Za-z0-9_\-.,;\']{0,50}$'), self.descriptionText) is  None :
                raise ValueError("[Description] on transaction. At most 50 characters long without special character except : “-”, “.”, “_”, “,”")
        
        if self.requestingOrganisationTransactionReference :
            if re.match((r'^[A-Za-z0-9_\-.,;\']{0,50}$'), self.requestingOrganisationTransactionReference) is  None   :
                raise ValueError("Transaction ID of client side. At most 50 characters long without special Character except : “-”, “.”, “_”, “,”")

        if self.originalTransactionReference :
            if re.match((r'^[A-Za-z0-9_\-.,;\']{0,50}$'), self.originalTransactionReference) is  None   :
                raise ValueError("Transaction ID of client side. At most 50 characters long without special Character except : “-”, “.”, “_”, “,”") 

        if self.requestDate :
            if re.match((r'^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{2,3}Z$'), self.requestDate) is  None:
                raise ValueError("[requestDate]Transaction requested date by client - yyyy-MM-ddTHH:mm:ss.SSSZ format ,  example = 2022-05-05T21:14:59.567Z")

        if self.debit :
            if re.match((r'^[0-9]{10}$'), self.debit) is  None: 
                raise   ValueError("[Debit]Phone number of subscriber .In preprod it’s fixed: 034350003 or 0343500004")
        
        if self.credit:
            if re.match((r'^[0-9]{10}$'), self.credit) is  None: 
                raise ValueError("[Credit]Phone number of merchant. In preprod it’s fixed: 034350003 or 0343500004")

    @property
    def headers(self) :
        data = {
            'Authorization': f'Bearer {self.token}',
            'Version': '1.0',
            'UserLanguage': str(self.UserLanguage).upper(),
            'X-CorrelationID': self.correlation_id,
            'UserAccountIdentifier': f'msisdn;{self.UserAccountIdentifier}',
            'partnerName': self.partnerName,
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache',
            'X-Callback-URL': str(self.X_Callback_URL) if self.X_Callback_URL else None
        }
        for k, v in dict(data).items():
            if v is None:
                del data[k]
        return data
             
    @property
    def dataJson(self):
        data = { 
                "amount": str(self.amount) if self.amount else None, 
                "currency": str(self.currency).capitalize(), 
                "descriptionText": str(self.descriptionText) if self.descriptionText else None,
                "requestingOrganisationTransactionReference": str(self.requestingOrganisationTransactionReference) if self.requestingOrganisationTransactionReference else None , 
                "requestDate":str(self.requestDate) if self.requestDate else None, 
                "originalTransactionReference": str(self.originalTransactionReference) if self.originalTransactionReference else None, 
                "debitParty": [{
                    "key": "msisdn", 
                    "value": str(self.debit) if self.debit else None
                } ], 
                "creditParty": [
                    { 
                        "key": "msisdn", 
                        "value": str(self.credit) if self.credit else None
                    }
                ],
                "metadata": [
                    {
                        "key": "partnerName", 
                        "value": str(self.partnerName) if self.partnerName else None
                    }, 
                    { 
                        "key": "fc", 
                        "value": self.fc
                    }, 
                    { 
                        "key": "amountFc", 
                        "value": self.amountFc 
                    } 
                ],
                "serverCorrelationId" : str(self.serverCorrelationId) if self.serverCorrelationId else None
            }
        for k, v in dict(data).items():
            if v is None:
                del data[k]

        return data
    
    def __str__(self) :
        return json.dumps({
            headers : self.headers ,
            dataJson : self.data
        })
