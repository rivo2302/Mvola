# -*- coding: utf-8 -*-

from mvola import Mvola
from mvola.tools import Transaction
from datetime import datetime
import threading
from time import sleep
from dotenv import load_dotenv
from os import environ

load_dotenv()

api = Mvola(environ['CONSUMER_KEY'], environ['SECRET_KEY'])

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
    amount="5555",
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
    # STATUS OF TRANSACTION
    transaction = Transaction(
        token=api.token,
        user_language="FR",
        user_account_identifier="0343500003",
        partner_name="Marketbot",
        server_correlation_id=correlation_id,
    )
    for i in range(15):
        res = api.status_transaction(transaction)
        if res.response["status"] != "pending":
            print(res.response["status"])
            break
        sleep(3)


x = threading.Thread(target=notif_status, args=(init.response["serverCorrelationId"],))
x.start()
# DETAILS OF  TRANSACTION
# transaction = Transaction(
#     token=api.token,
#     user_language="FR",
#     user_account_identifier="0343500003",
#     partner_name="Marketbot",
#     transid="636251274",
# )
# res = api.details_transaction(transaction)
# if res.success:
#     print(res.response)
# else:
#     print(f"Status_code [{res.status_code}] \n {res.error}")
