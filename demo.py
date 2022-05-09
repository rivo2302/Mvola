# -*- coding: utf-8 -*-

from mvola import Mvola
from mvola.tools import Transaction

api = Mvola("0zL7eTrSEfXf6kkwJ53DSegCbBwa","pd8PIZYmeZaafifZgwHu1BC5ucMa")

# GENERATE TOKEN
res = api.generate_token()
if res.success :
    api.token = res
    print(res)
else :
    print(f"Status_code[{res.status_code}] - {res.error}")

# INITIATE TRANSACTION
transaction = Transaction(
    token="eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjUyMDk2Mzc1LCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjUyMDk5OTc1LCJpYXQiOjE2NTIwOTYzNzUsImp0aSI6Ijk0ZWRlZjIyLTFmYzEtNDYxNS05YzZjLWQxZGQ3MDg1NmFjYyJ9.MQ6ew1r7nMWZN3hI8Xvbv0PuZgsi-GY_IjsO-NeXmALh1KnwOOwhgo1cMu9hRGsXWg3XZexqLagLHRcjYNDXJKR6QuYrop6WzZuGMGsNs-PL_1jrjctOLIS2VGBL1utCdDvhvfYgG-oOs2cisBUIQ7TtHF8haTd0w4WdNVkxt66Jz5ZGhEbOBralbym3-Bgjo_2wbuKy9iY0x6xqr2xMuhPXkgTFyZmAqmUv32zIIyvfC6OiEcfcXF2T3Bm_NqJN8BNXXu8ST3sdU_dEp2wYEf5f4d8LxUygNVv5n9kkdlmLrRWpoEeWfpIcfAeMuMdyLaXAgQj-T7BInM5wECMhYg",
    UserLanguage="FR",
    UserAccountIdentifier="0343500003",
    partnerName="Marketbot",
    X_Callback_URL="https://2809-102-16-43-64.ngrok.io",  
    amount="1500",
    currency="Ar",
    originalTransactionReference="orgina",
    requestingOrganisationTransactionReference="ozcbajq",
    descriptionText="fe",
    requestDate="2022-05-07T12:03:10.567Z",
    debit="0343500003",
    credit="0343500004", 
)
init = api.init_transaction(transaction)
if init.success :
    print(init.value)
else :
    print(f"Status_code:[{init.status_code}] - {init.error}")

# STATUS TRANSACTION
transaction = Transaction(
    token="eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjUyMDk2Mzc1LCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjUyMDk5OTc1LCJpYXQiOjE2NTIwOTYzNzUsImp0aSI6Ijk0ZWRlZjIyLTFmYzEtNDYxNS05YzZjLWQxZGQ3MDg1NmFjYyJ9.MQ6ew1r7nMWZN3hI8Xvbv0PuZgsi-GY_IjsO-NeXmALh1KnwOOwhgo1cMu9hRGsXWg3XZexqLagLHRcjYNDXJKR6QuYrop6WzZuGMGsNs-PL_1jrjctOLIS2VGBL1utCdDvhvfYgG-oOs2cisBUIQ7TtHF8haTd0w4WdNVkxt66Jz5ZGhEbOBralbym3-Bgjo_2wbuKy9iY0x6xqr2xMuhPXkgTFyZmAqmUv32zIIyvfC6OiEcfcXF2T3Bm_NqJN8BNXXu8ST3sdU_dEp2wYEf5f4d8LxUygNVv5n9kkdlmLrRWpoEeWfpIcfAeMuMdyLaXAgQj-T7BInM5wECMhYg",
    UserLanguage="FR",
    UserAccountIdentifier="0343500003",
    partnerName="Marketbot",
    serverCorrelationId='821ff7f5-73e2-4e6e-af47-a8c40150f950'
)
res = api.status_transaction(transaction)
if res.success :
    print(res.value)
else :
    print(f"Status_code [{res.status_code}] \n {res.error}")
