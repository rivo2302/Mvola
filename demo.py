#Import the module PyMvola
from PyMvola import API

#Initiate the api => API(Consummer_key, Consummer _secret)
api = API("FB3XmEdDZMajm4VYh9sfLMLi2HQa","YFTPUch1sgq0lpqf1PCFhwfsR6wa")
# api = API("{Consummer_key}","{YFTPUch1sgq0lpqf1PCFhwfsR6wa}")

#Generate api's token => Return token if requests success  or error details if requests failed
res = api.generate_token()

if get_token.success:
    api.token = res
else :
    print(f"[{res.status_code}] - {res.error}")



