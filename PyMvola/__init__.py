# -*- coding: utf-8 -*-
from .core import API

data = { 
    "amount": "2000", 
    "currency": "Ar", 
    "descriptionText": "TesteAPI",
    "requestingOrganisationTransactionReference": "trasactiondereference", 
    "requestDate":"2022-05-05T15:55:00.567Z", 
    "originalTransactionReference": "originatex", 
    "debitParty": [{
        "key": "msisdn", 
        "value": "0340921107"
    } ], 
    "creditParty": [
        { 
            "key": "msisdn", 
            "value":"0341372238"
        }
    ],
    "metadata": [
        {
            "key": "partnerName", 
            "value":"{{companyName}}" 
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