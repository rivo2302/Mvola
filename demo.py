from PyMvola import API

api = API("FB3XmEdDZMajm4VYh9sfLMLi2HQa","YFTPUch1sgq0lpqf1PCFhwfsR6wa")

get_token = api.generate_token()

if get_token.success:
    print(get_token.token)
else :
    print(get_token.error, get_token.status_code)