# -*- coding: utf-8 -*-

from mvola import Mvola
from mvola.tools import Transaction
from datetime import datetime
import threading
from time import sleep
from os import environ as env
import sys

if env.get("CONSUMER_KEY") and env.get("SECRET_KEY"):
    api = Mvola(env.get("CONSUMER_KEY"), env.get("SECRET_KEY"), status="SANDBOX")
else:
    print(" Mvola error : Verify if you have .env file <CONSUMER_KEY> and <SECRET_KEY>")
    sys.exit()

# GENERATE TOKEN
res = api.generate_token()
print(res.status_code)
if res.success:
    print(res.response)
    api.token = res.response
else:
    print(f"Status_code[{res.status_code}] - {res.error}")

# INITIATE TRANSACTION
transaction = Transaction(
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

init = api.init_transaction(transaction)
if init.success:
    print(init.response)
else:
    print(f"Status_code:[{init.status_code}] - {init.error}")


def notif_status(correlation_id):
    """
        A thread that will get the return of the transacation request.
    The Mvola api makes a return after 30 seconds. We make a thread here because
    we have no web server but the best way is use webserver.
    """
    transaction = Transaction(
        token=api.token,
        user_language="FR",
        user_account_identifier="0343500003",
        partner_name="Demo",
        server_correlation_id=correlation_id,
    )

    for i in range(15):
        res = api.status_transaction(transaction)
        if res.response["status"] != "pending":
            print(res.response["status"])
            break
        sleep(3)
    print(res.response["status"])


x = threading.Thread(target=notif_status, args=(init.response["serverCorrelationId"],))
x.start()

# DETAILS OF  TRANSACTION
transaction = Transaction(
    token=api.token,
    user_language="FR",
    user_account_identifier="0343500003",
    partner_name="Marketbot",
    transid="<ID OF TRANSACTION>",
)
res = api.details_transaction(transaction)
if res.success:
    print(res.response)
else:
    print(f"Status_code [{res.status_code}] \n {res.error}")
