# -*- coding: utf-8 -*-

from mvola import Mvola
from mvola.tools import Transaction

api = Mvola("0zL7eTrSEfXf6kkwJ53DSegCbBwa", "pd8PIZYmeZaafifZgwHu1BC5ucMa")

# GENERATE TOKEN
res = api.generate_token()
if res.success:
    api.token = res
    print(res)
else:
    print(f"Status_code[{res.status_code}] - {res.error}")

# INITIATE TRANSACTION
transaction = Transaction(
    token="eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjU0MTA4ODg2LCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjU0MTEyNDg2LCJpYXQiOjE2NTQxMDg4ODYsImp0aSI6IjVlOGY5ZjFhLWUxODItNGZkMS04ZjUyLWU2YTIzMzljYTIzMCJ9.voIBGWbGiI7vFklcmHiufu5fW1UvlE79c7MNOZZisuGD7HQ8P4CFljBhbQQj8lHnd8u48KFdLxHWwg4SozDejPlTFmeDdHaE8UoYhTsVthYgG5eKN3ZSQ0LSyYyeLbxA25vssvVSkQBCX-4EtcrH_vgEnZiJotBqD8PhicuwtvJuiqm3lbkFcGpNNtVGlUD8Q_xxBt31Az044qJ3BYTcmnG1tXmjRzQNyNrGe3rnQxbnndqg1gHrr-st8bulgODHWGZ3vKkmpdXnMxAn6sYjPRZ0YOdfdQwpgYK8HpLh1oI8VtTsw8oqTiVXpk-4F00qXjqihVd66len-BS48DIsig",
    user_language="FR",
    user_account_identifier="0343500003",
    partner_name="Marketbot",
    x_callback_url="https://a978-154-126-10-61.ngrok.io/",
    amount="5555",
    currency="Ar",
    original_transaction_reference="orgina",
    requesting_organisation_transaction_reference="ozcbajq",
    description_text="fevvs",
    request_date="2022-06-01T22:08:10.567Z",
    debit="0343500003",
    credit="0343500004",
)
init = api.init_transaction(transaction)
if init.success:
    print(init.response)
else:
    print(f"Status_code:[{init.status_code}] - {init.error}")

# STATUS OF TRANSACTION
transaction = Transaction(
    token="eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjU0MTA4ODg2LCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjU0MTEyNDg2LCJpYXQiOjE2NTQxMDg4ODYsImp0aSI6IjVlOGY5ZjFhLWUxODItNGZkMS04ZjUyLWU2YTIzMzljYTIzMCJ9.voIBGWbGiI7vFklcmHiufu5fW1UvlE79c7MNOZZisuGD7HQ8P4CFljBhbQQj8lHnd8u48KFdLxHWwg4SozDejPlTFmeDdHaE8UoYhTsVthYgG5eKN3ZSQ0LSyYyeLbxA25vssvVSkQBCX-4EtcrH_vgEnZiJotBqD8PhicuwtvJuiqm3lbkFcGpNNtVGlUD8Q_xxBt31Az044qJ3BYTcmnG1tXmjRzQNyNrGe3rnQxbnndqg1gHrr-st8bulgODHWGZ3vKkmpdXnMxAn6sYjPRZ0YOdfdQwpgYK8HpLh1oI8VtTsw8oqTiVXpk-4F00qXjqihVd66len-BS48DIsig",
    user_language="FR",
    user_account_identifier="0343500003",
    partner_name="Marketbot",
    server_correlation_id="72c5142d-5132-4f66-ac98-af905ba2c9ec",
)
res = api.status_transaction(transaction)
if res.success:
    print(res.response)
else:
    print(f"Status_code [{res.status_code}] \n {res.error}")


# DETAILS OF  TRANSACTION
transaction = Transaction(
    token="eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjU0MTA4ODg2LCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjU0MTEyNDg2LCJpYXQiOjE2NTQxMDg4ODYsImp0aSI6IjVlOGY5ZjFhLWUxODItNGZkMS04ZjUyLWU2YTIzMzljYTIzMCJ9.voIBGWbGiI7vFklcmHiufu5fW1UvlE79c7MNOZZisuGD7HQ8P4CFljBhbQQj8lHnd8u48KFdLxHWwg4SozDejPlTFmeDdHaE8UoYhTsVthYgG5eKN3ZSQ0LSyYyeLbxA25vssvVSkQBCX-4EtcrH_vgEnZiJotBqD8PhicuwtvJuiqm3lbkFcGpNNtVGlUD8Q_xxBt31Az044qJ3BYTcmnG1tXmjRzQNyNrGe3rnQxbnndqg1gHrr-st8bulgODHWGZ3vKkmpdXnMxAn6sYjPRZ0YOdfdQwpgYK8HpLh1oI8VtTsw8oqTiVXpk-4F00qXjqihVd66len-BS48DIsig",
    user_language="FR",
    user_account_identifier="0343500003",
    partner_name="Marketbot",
    transid="636251274",
)
res = api.details_transaction(transaction)
if res.success:
    print(res.response)
else:
    print(f"Status_code [{res.status_code}] \n {res.error}")
