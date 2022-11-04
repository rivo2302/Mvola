from mvola import Mvola
from os import environ as env
import sys
from datetime import datetime

CONSUMER_KEY = env.get("CONSUMER_KEY")
SECRET_KEY = env.get("SECRET_KEY")


def test_env():
    if not CONSUMER_KEY or not SECRET_KEY:
        print(
            """
            Mvola error : Verify if you have .env file <CONSUMER_KEY> and
            <SECRET_KEY>
            """
        )
        sys.exit()


def test_token():
    api = Mvola(CONSUMER_KEY, SECRET_KEY, status="SANDBOX")
    res = api.generate_token()
    assert (
        res.status_code == 200
    ), f"Status code [{res.status_code}] - {res.error}"


def test_init_transaction():
    api = Mvola(CONSUMER_KEY, SECRET_KEY, status="SANDBOX")
    res = api.generate_token()
    api.token = res.token
    res = api.init_transaction(
        token=api.token,
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
    assert (
        res.status_code == 200
    ), f"Status code [{res.status_code}] - {res.error}"
