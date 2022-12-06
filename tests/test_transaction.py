from mvola import Mvola
from mvola.tools import Transaction
from os import environ as env
from datetime import datetime

CONSUMER_KEY = env.get("CONSUMER_KEY")
SECRET_KEY = env.get("SECRET_KEY")


class TestMvolaTransaction:
    key = CONSUMER_KEY
    secret = SECRET_KEY
    api = Mvola(key, secret, status="SANDBOX")

    def test_generate_token(self):
        """
        Test generate token method
        """
        res = self.api.generate_token()
        assert (
            res.status_code == 200
        ), f"Status code [{res.status_code}] - {res.error}"

    def test_init_transaction(self):
        """
        Test init transaction method
        """
        # Generate token
        token = self.api.generate_token().response

        # Instance transaction object
        transaction = Transaction(
            token=token,
            user_language="FR",
            user_account_identifier="0343500003",
            partner_name="Marketbot",
            x_callback_url="https://86f5-154-126-121-39.eu.ngrok.io",
            amount="555",
            currency="Ar",
            original_transaction_reference="orgina",
            requesting_organisation_transaction_reference="ozcbajq",
            description_text="fevvs",
            request_date=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.999Z"),
            debit="0343500003",
            credit="0343500004",
        )
        res = self.api.init_transaction(transaction)

        # The status code is 202  because the transaction is not yet completed but just on pending
        assert (
            res.status_code == 202
        ), f"Status code [{res.status_code}] - {res.error}"

    def test_get_transaction_status(self):
        """
        Test get transaction status method
        """
        # Generate token
        token = self.api.generate_token().response

        # Instance transaction object
        transaction = Transaction(
            token=token,
            user_language="FR",
            user_account_identifier="0343500003",
            partner_name="Marketbot",
            x_callback_url="https://86f5-154-126-121-39.eu.ngrok.io",
            amount="555",
            currency="Ar",
            original_transaction_reference="orgina",
            requesting_organisation_transaction_reference="ozcbajq",
            description_text="fevvs",
            request_date=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.999Z"),
            debit="0343500003",
            credit="0343500004",
        )
        res = self.api.init_transaction(transaction)

        transaction_id = res.response["serverCorrelationId"]
        transaction = Transaction(
            token=token,
            user_language="FR",
            user_account_identifier="0343500003",
            partner_name="Marketbot",
            server_correlation_id=transaction_id,
        )
        res = self.api.status_transaction(transaction)
        assert (
            res.status_code == 200
        ), f"Status code [{res.status_code}] - {res.error}"
