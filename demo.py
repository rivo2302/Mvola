# -*- coding: utf-8 -*-

from mvola import Mvola
from mvola.tools import Transaction
api = Mvola("0zL7eTrSEfXf6kkwJ53DSegCbBwa","pd8PIZYmeZaafifZgwHu1BC5ucMa")

# ## GENERATE TOKEN
# res = api.generate_token()
# if res.success :
#     api.token = res
#     print(res)
# else :
#     print(f"Status_code[{res.status_code}] - {res.error}")

# # INITIATE TRANSACTION
# transaction = Transaction(
#     token="eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjUyMDM1NzYwLCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjUyMDM5MzYwLCJpYXQiOjE2NTIwMzU3NjAsImp0aSI6IjMzMGNjMjQwLWNjY2EtNGE4Yi1iZTNmLTU0OWYyZmM1M2UxMCJ9.IH-4K_AydReq9S8jyhqh4tGtdys1Mm9HB_6IphCo3asW9rdXMJFrETtV3EV0OAdPGyfoPKGVN-ge8zCn6IjiPxB5TosHp3WaEjpAhMWqFwbuOciG5SISeHAKHQ2FYvMOa3Utrroymimqavxfpxpi3fm3dZs1Od8os8363bXrDaGvEGg7p25Ykozs0dYZrt_-5H-LHOEFH9Oih-t5HYr-QDDTLcRhADVJZ_4W-lpzgLlffIEhEUW0ZBjO8BnqReXL7a9BW9ex2kUSjH9fkt9sSCC04UM1-H17V0R1c-xxcnPaJCpt4COJVN17xRb-hWJLg5KsFedv7Ex_yk9CDQbi6A",
#     UserLanguage="FR",
#     UserAccountIdentifier="0343500003",
#     partnerName="Marketbot",
#     X_Callback_URL="https://2809-102-16-43-64.ngrok.io",  
#     amount="1500",
#     currency="Ar",
#     originalTransactionReference="orgina",
#     requestingOrganisationTransactionReference="ozcbajq",
#     descriptionText="fe",
#     requestDate="2022-05-07T12:03:10.567Z",
#     debit="0343500003",
#     credit="0343500004", 
# )
# init = api.init_transaction(transaction)
# if init.success :
#     print(init.value)
# else :
#     print(f"Status_code:[{init.status_code}] - {init.error}")

transaction = Transaction(
    token="eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjUyMDM1NzYwLCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjUyMDM5MzYwLCJpYXQiOjE2NTIwMzU3NjAsImp0aSI6IjMzMGNjMjQwLWNjY2EtNGE4Yi1iZTNmLTU0OWYyZmM1M2UxMCJ9.IH-4K_AydReq9S8jyhqh4tGtdys1Mm9HB_6IphCo3asW9rdXMJFrETtV3EV0OAdPGyfoPKGVN-ge8zCn6IjiPxB5TosHp3WaEjpAhMWqFwbuOciG5SISeHAKHQ2FYvMOa3Utrroymimqavxfpxpi3fm3dZs1Od8os8363bXrDaGvEGg7p25Ykozs0dYZrt_-5H-LHOEFH9Oih-t5HYr-QDDTLcRhADVJZ_4W-lpzgLlffIEhEUW0ZBjO8BnqReXL7a9BW9ex2kUSjH9fkt9sSCC04UM1-H17V0R1c-xxcnPaJCpt4COJVN17xRb-hWJLg5KsFedv7Ex_yk9CDQbi6A",
    UserLanguage="FR",
    UserAccountIdentifier="0343500003",
    partnerName="Marketbot",
    serverCorrelationId='c8e9e922-b965-4515-b390-137b41c9f40b'
)

status = api.status_transaction(transaction)
