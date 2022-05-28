# -*- coding: utf-8 -*-

from mvola import Mvola
from mvola.tools import Transaction

api = Mvola("0zL7eTrSEfXf6kkwJ53DSegCbBwa","pd8PIZYmeZaafifZgwHu1BC5ucMa")

# # GENERATE TOKEN
# res = api.generate_token()
# if res.success :
#     api.token = res
#     print(res)
# else :
#     print(f"Status_code[{res.status_code}] - {res.error}")

# INITIATE TRANSACTION
# transaction = Transaction(
#     token="eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjUzNzI5MzAyLCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjUzNzMyOTAyLCJpYXQiOjE2NTM3MjkzMDIsImp0aSI6IjhkZjI1MWU3LWUzZTAtNGNiNy1hNjU0LTc3NmI3NWJlZTM0MiJ9.f6SvY8sS5BVD6eCt5n1jLhZl_cCVRjOciqWkj1bDuC31oJUKAjs9i00dmc4YTwH76ne5FgAzUvItLxenq9qjOHYLGZBrnAG5Z-v3pKh0qNMkyVXmkyn3xzLfyGsKCuy8C_mRFcVtnj3RVqkazREMsXn6tpAWkMEaOjd4HJV6Sbt3Tk29KGH2WqmzLSC9p_2gb1ztgk92xR8WSWCg-rCHOJsISAz5vV0H09auNXLxuDIuqPzSzh85gebGcbfdkrTrHSafSQ_cANxI-TO1VAJgJhGj0kzXo-BgK5AV0WtjynvsJdinzpRf70h4Gnl4YIO8PVc4P_NPKi2acIIFkVeR3w",
#     user_language="FR",
#     user_account_identifier="0343500003",
#     partner_name="Marketbot",
#     x_callback_url="https://2809-102-16-43-64.ngrok.io",  
#     amount="1500",
#     currency="Ar",
#     original_transaction_reference="orgina",
#     requesting_organisation_transaction_reference="ozcbajq",
#     description_text="fevvs",
#     request_date="2022-05-07T12:03:10.567Z",
#     debit="0343500003",
#     credit="0343500004", 
# )
# init = api.init_transaction(transaction)
# if init.success :
#     print(init.value)
# else :
#     print(f"Status_code:[{init.status_code}] - {init.error}")

# # STATUS TRANSACTION
transaction = Transaction(
    token="eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjUzNzI5MzAyLCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjUzNzMyOTAyLCJpYXQiOjE2NTM3MjkzMDIsImp0aSI6IjhkZjI1MWU3LWUzZTAtNGNiNy1hNjU0LTc3NmI3NWJlZTM0MiJ9.f6SvY8sS5BVD6eCt5n1jLhZl_cCVRjOciqWkj1bDuC31oJUKAjs9i00dmc4YTwH76ne5FgAzUvItLxenq9qjOHYLGZBrnAG5Z-v3pKh0qNMkyVXmkyn3xzLfyGsKCuy8C_mRFcVtnj3RVqkazREMsXn6tpAWkMEaOjd4HJV6Sbt3Tk29KGH2WqmzLSC9p_2gb1ztgk92xR8WSWCg-rCHOJsISAz5vV0H09auNXLxuDIuqPzSzh85gebGcbfdkrTrHSafSQ_cANxI-TO1VAJgJhGj0kzXo-BgK5AV0WtjynvsJdinzpRf70h4Gnl4YIO8PVc4P_NPKi2acIIFkVeR3w",
    user_language="FR",
    user_account_identifier="0343500003",
    partner_name="Marketbot",
    server_correlation_id='bf9f849b-c9c4-4d09-921d-953f988179e4'
)
res = api.status_transaction(transaction)
if res.success :
    print(res.value)
else :
    print(f"Status_code [{res.status_code}] \n {res.error}")
