# -*- coding: utf-8 -*-

import re
import uuid
import json


class ResultAction:
    """
    Result Action

    The object to use for getting response of each API  action (Generate token, Initiate
    transaction, status transaction,...)
    """

    def __init__(self) -> None:
        self.success = False  # True if the requests is success
        self.error = None  # Details if error occurs
        self.response = None  # Content of the request's response
        self.token = None  # The value of token
        self.status_code = None  # The status code the requests
        self.headers = (None,)
        self.data = (None,)

    def __str__(self):
        return json.dumps(
            {
                "Success": self.success,
                "Error": self.error,
                "Status code": self.status_code,
                "response": self.response,
            },
            indent=4,
        )


class Transaction:
    """
    Transaction

    The object to use to check easier error handling on data constraints
    during each transactions.
    """

    def __init__(self, **kwargs):

        # Headers of the transaction
        self.correlation_id = str(uuid.uuid1())
        self.token = kwargs.get("token")
        self.user_language = kwargs.get("user_language", "FR")
        self.user_account_identifier = kwargs.get("user_account_identifier")
        self.partner_name = kwargs.get("partner_name")
        self.x_callback_url = kwargs.get("x_callback_url")

        # Data
        self.amount = kwargs.get("amount")
        self.currency = kwargs.get("currency", "Ar")
        self.description_text = kwargs.get("description_text")
        self.requesting_organisation_transaction_reference = kwargs.get(
            "requesting_organisation_transaction_reference"
        )
        self.request_date = kwargs.get("request_date")
        self.original_transaction_reference = kwargs.get(
            "original_transaction_reference"
        )
        self.debit = kwargs.get("debit")
        self.credit = kwargs.get("credit")
        self.fc = kwargs.get("fc", "USD")
        self.amount_fc = kwargs.get("amount_fc", "1")
        self.server_correlation_id = kwargs.get("server_correlation_id")
        self.transid = kwargs.get("transid")

        # Check  if the number is really a Telma number
        telma_phone_number_pattern = r"^(034|038)\d{7}$"

        # Patter for generic phone number
        generic_phone_number_pattern = r"^(03)\d{8}$"

        if not self.token:
            raise ValueError(
                " Mvola Error  : [token] Required fields | Generate token"
            )

        if not self.user_account_identifier:
            raise ValueError(
                "  Mvola Error  :  [user_account_identifier] Required field"
            )

        if self.user_language.upper() not in ("FR", "MG"):
            raise ValueError(" Mvola Error  : [user_language] FR or MG")

        if not self.partner_name:
            raise ValueError(" Mvola Error  : [partner_name] Required field")

        if self.amount:
            if not str(self.amount).isdigit():
                raise ValueError(
                    " Mvola Error  : [Amount] of transaction without decimals"
                    " ,example : 1000,20,15"
                )

        if str(self.currency).capitalize() != "Ar":
            raise ValueError(
                " Mvola Error  : [Currency] code of the transaction - Possible"
                " Values : Ar"
            )

        if (
            re.match(
                (telma_phone_number_pattern), self.user_account_identifier
            )
            is None
        ):
            raise ValueError(
                """
                    Mvola Error  : [user_account_identifier] of the transaction check if 
                    it is a valid Telma number , example : 0341234567
                """
            )

        if self.description_text:
            if (
                re.match(r"^[A-Za-z0-9_\-.,;\']{0,50}$", self.description_text)
                is None
            ):
                raise ValueError(
                    " Mvola Error  : [description_text] on transaction. At"
                    " most 50 characters long without special character except"
                    " : “-”, “.”, “_”, “,”"
                )

        if self.requesting_organisation_transaction_reference:
            if (
                re.match(
                    r"^[A-Za-z0-9_\-.,;\']{0,50}$",
                    self.requesting_organisation_transaction_reference,
                )
                is None
            ):
                raise ValueError(
                    " Mvola Error  : Transaction ID of client side. At most 50"
                    " characters long without special Character except : “-”,"
                    " “.”, “_”, “,”"
                )

        if self.original_transaction_reference:
            if (
                re.match(
                    r"^[A-Za-z0-9_\-.,;\']{0,50}$",
                    self.original_transaction_reference,
                )
                is None
            ):
                raise ValueError(
                    """
                    Mvola Error  : Transaction ID of client side. At most 50
                    characters long without special Character except : “-”,
                    " “.”, “_”, “,”
                    """
                )

        if self.request_date:
            if (
                re.match(
                    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{2,3}Z$",
                    self.request_date,
                )
                is None
            ):
                raise ValueError(
                    " Mvola Error  : [request_date]Transaction requested date"
                    " by client - yyyy-MM-ddTHH:mm:ss.SSSZ format ,  example ="
                    " 2022-05-05T21:14:59.567Z"
                )

        if self.debit:
            if re.match((generic_phone_number_pattern), self.debit) is None:
                raise ValueError(
                    """
                    Mvola Error  : [Debit]Phone number of merchant. 
                    Check if it is a valid number , example : 0341234567
                    """
                )

        if self.credit:
            if re.match((telma_phone_number_pattern), self.credit) is None:
                raise ValueError(
                    """
                    Mvola Error  : [Credit]Phone number of merchant. 
                    Check if it is a valid Telma number , example : 0341234567
                    """
                )

    @property
    def headers(self):
        data = {
            "Authorization": f"Bearer {self.token}",
            "Version": "1.0",
            "UserLanguage": str(self.user_language).upper(),
            "X-CorrelationID": self.correlation_id,
            "UserAccountIdentifier": f"msisdn;{self.user_account_identifier}",
            "partnerName": self.partner_name,
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "X-Callback-URL": str(self.x_callback_url)
            if self.x_callback_url
            else None,
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
            "descriptionText": str(self.description_text)
            if self.description_text
            else None,
            "requestingOrganisationTransactionReference": str(
                self.requesting_organisation_transaction_reference
            )
            if self.requesting_organisation_transaction_reference
            else None,
            "requestDate": str(self.request_date)
            if self.request_date
            else None,
            "originalTransactionReference": str(
                self.original_transaction_reference
            )
            if self.original_transaction_reference
            else None,
            "debitParty": [
                {
                    "key": "msisdn",
                    "value": str(self.debit) if self.debit else None,
                }
            ],
            "creditParty": [
                {
                    "key": "msisdn",
                    "value": str(self.credit) if self.credit else None,
                }
            ],
            "metadata": [
                {
                    "key": "partnerName",
                    "value": str(self.partner_name)
                    if self.partner_name
                    else None,
                },
                {"key": "fc", "value": self.fc},
                {"key": "amountFc", "value": self.amount_fc},
            ],
            "serverCorrelationId": str(self.server_correlation_id)
            if self.server_correlation_id
            else None,
            "transid": str(self.transid) if self.transid else None,
        }
        for k, v in dict(data).items():
            if v is None:
                del data[k]

        return data

    def __str__(self):
        return json.dumps({"headers": self.headers, "dataJson": self.dataJson})
