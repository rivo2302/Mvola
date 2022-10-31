from mvola import Mvola
from mvola.tools import Transaction
from datetime import datetime
from time import sleep
from os import environ as env
import sys


CONSUMER_KEY = env.get("CONSUMER_KEY")
SECRET_KEY = env.get("SECRET_KEY")
CALLBACK_URL = env.get("CALLBACK_URL")


def test_transaction():
    if CONSUMER_KEY and SECRET_KEY:
        api = Mvola(CONSUMER_KEY, SECRET_KEY, status="SANDBOX")
    else:
        print("Mvola error : Verify if you have .env file <CONSUMER_KEY> and <SECRET_KEY>")
        sys.exit()

    # GENERATE TOKEN
    res = api.generate_token()
    assert (res.status_code == 200)
    assert (res.success)

    api.token = res.response

    # INITIATE TRANSACTION
    transaction = Transaction(
        token=api.token,
        user_language="FR",
        user_account_identifier="0343500003",
        partner_name="Marketbot",
        x_callback_url=CALLBACK_URL,
        amount="555",
        currency="Ar",
        original_transaction_reference="orgina",
        requesting_organisation_transaction_reference="ozcbajq",
        description_text="fevvs",
        request_date=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.999Z"),
        debit="0343500003",
        credit="0343500004",
    )

    init = api.init_transaction(transaction)
    assert (init.success)
    assert (init.status_code == 200)
