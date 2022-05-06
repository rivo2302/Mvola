# -*- coding: utf-8 -*-

# Import the module mvola
from mvola import Mvola
from mvola.tools import Transaction

# Initiate the api
api = API("{consummer_key}","{consummer_secret}")
"""
    GENERATE TOKEN
"""
res = api.generate_token()

if res.success :
    api.token = res
    print(res)
else :
    print(f"Status_code[{res.status_code}] - {res.error}")


"""
    INITIATE TRANSACTION
"""
transaction = Transaction(
    token="eyJ4NXQiOiJPRE5tWkRbFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjUxNzk1NTUyLCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjUxNzk5MTUyLCJpYXQiOjE2NTE3OTU1NTIsImp0aSI6IjFjNWEwNDY3LTk5NWMtNDFiNi05M2I2LWJjNzY2YTA0ZDdiZCJ9.PCijTounfH2y2-LNaRaKQleYFEV-voBb0ES-ayYRSG8NyT8GVt6BOXWFdPh4V7MNN5ArBtErVifx5MastxKRqE1-rYnekt51iynCXknEPM3hxjFepOPHPR3rIDtRrNJ0raa0oEkVcHjn6Gl9wUiai-4zepwFaR7GP3xAr6Rz42szCQo4AjDiuJkGMNEhQqgL17AYpjOHE8mXf_Jeth7VpcgUTXDwRRNAGhCzUEHqwQpW-7TPryeTHFzj8HPySy3RWBI5bUjYfVoXWL_yg__RxM0YlPX7JE3ycs75yANbWyQ4WdSc3vZhPCkKusERajxlQCIwBxmVUmALp9YRn0wjfg",
    UserLanguage="FR",
    UserAccountIdentifier="0343500003",
    partnerName="Marketbot",
    amount="1500",
    currency="Ar",
    descriptionText="Unedescription",
    requestDate="2022-05-06T02:14:59.567Z",
    debit="0343500003",
    credit="0343500004"
)

init = api.init_transaction(transaction.headers,transaction.dataJson)
if init.success :
    print(init.value)
else :
    print(f"Status_code:[{init.status_code}] - {init.error}")