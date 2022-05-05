# -*- coding: utf-8 -*-

from .core import API

data = { 
    "amount": "2000", 
    "currency": "Ar", 
    "descriptionText": "TesteAPI",
    "requestingOrganisationTransactionReference": "trasactiondereference", 
    "requestDate":"2022-05-05T18:55:00.567Z", 
    "originalTransactionReference": "originatex", 
    "debitParty": [
        {
            "key": "msisdn", 
            "value": "0343500003"
        } 
    ], 
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