# -*- coding: utf-8 -*-

# Import the module pymvola
from pymvola import Mvola

# Initiate the api => API(Consummer_key, Consummer_secret)
# api = API("{consummer_key}","{consummer_secret}")
api = Mvola("0zL7eTrSEfXf6kkwJ53DSegCbBwa","pd8PIZYmeZaafifZgwHu1BC5ucMa")

# Generate api's token => Return token if requests success  or error details if requests failed
res = api.generate_token()

if res.success :
    api.token = res
    print(res)
else :
    print(f"[{res.status_code}] - {res.error}")

api.transaction("tes",'bfvd')

