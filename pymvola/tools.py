# -*- coding: utf-8 -*-

class ResultGetToken :

    def __init__(self) -> None:
        self.success =  False 
        self.error =  None
        self.value = None
        self.token = None
        self.status_code = None
    

    def __str__(self) :
        return  str(self.token)

        

class Transaction :

    def __init__ (self ,**kwargs) :

        self.amount = kwargs.get("amount", "0")
        self.currency = kwargs.get("currency", "Ar")
        self.descriptionText = kwargs.get("descriptionText", "Description")
        self.requestingOrganisationTransactionReference = kwargs.get("requestingOrganisationTransactionReference","Referecence de transaction")
        self.requestDate = kwargs.get("requestDate","2022-05-05T21:14:59.567Z")
        self.originalTransactionReference = kwargs.get("originalTransactionReference","Transaciton de reference" )
        self.debitParty = kwargs.get("debitParty" , [{
                "key": "msisdn", 
                "value": "0343500003"
            } 
        ])
        self.creditParty = kwargs.get("creditParty",[
                { 
                    "key": "msisdn", 
                    "value":"0343500004"
                }
            ]) 
        
        self.metadata = kwargs.get("metadata" ,[
                {
                    "key": "partnerName", 
                    "value":"Marketbot" 
                } 
            ]
        )

        if not str(self.amount).isdigit() :     
            raise ValueError("Amount can only be a digit example : 1000,20,15")
        self.amount = str(self.amount)

        


