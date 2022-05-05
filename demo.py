# Import the module PyMvola
from PyMvola import API

# Initiate the api => API(Consummer_key, Consummer_secret)
# api = API("{consummer_key}","{consummer_secret}")
api = API("FB3XmEdDZMajm4VYh9sfLMLi2HQa","YFTPUch1sgq0lpqf1PCFhwfsR6wa")

# Generate api's token => Return token if requests success  or error details if requests failed
res = api.generate_token()

if res.success :
    api.token = res
    print(res)
else :
    print(f"[{res.status_code}] - {res.error}")



