</br>
</br>
<p align="center"> 
    <img height="400" src="https://raw.githubusercontent.com/rivo2302/Mvola/master/assets/icon.png">
</p>
<div align="center"> 
    <p>
        A <b>light</b> Python module for your <a href="https://www.mvola.mg/devportal/"> API Mvola </a>.
        <h4>
            <a href="https://pypi.org/project/mvola/">Documentation</a>
            <span> | </span>
            <a href="https://github.com/rivo2302/Mvola/issues">Report bugs</a>
            <span> | </span>
            <a href="https://github.com/rivo2302/Mvola/fork">Contribute</a>
        </h4>
    </p>
    <p>
        <a href='https://pypi.org/project/mvola/'><img src='https://img.shields.io/pypi/v/mvola?style=for-the-badge'/></a>
        <a href='https://github.com/rivo2302/Mvola'> 
            <img src="https://img.shields.io/badge/-python-396E9B?style=for-the-badge&logo=python&logoColor=FFFFFF"/>
        </a>
        <a href='https://pypi.org/project/mvola/'> 
             <img src='https://img.shields.io/pypi/dm/mvola?label=DOWNLOADS&style=for-the-badge'/>
        </a>
        <a href='#'> 
            <img src='https://img.shields.io/badge/Maintained-Yes-darkgreen?style=for-the-badge'/>
        </a>  
    </p>
</div>

## INSTALLATION

You can consult the link on pypi.org <a href="https://pypi.org/project/mvola/">here</a> for mode documentation.

```s
pip install mvola==1.0.5
```

## USAGE 
> Check the demo file <a href="https://github.com/rivo2302/Mvola/blob/master/demo.py">here</a>


### Start the API 
Create your account <a href="https://www.mvola.mg/devportal/">here</a>.
After you create application , you should have Consummer_key and Consummer_secret and add those 
variable in .env file(check the env file example).

```python
# Import the module mvola
from mvola import Mvola

# Import environ module to access environment variables
from os import environ as env


# Initiate the api => API(Consummer_key, Consummer_secret)
api = Mvola(env.get('CONSUMER_KEY'), env.get('SECRET_KEY'))
```

### Generate token
Check the documentation <a href="https://www.mvola.mg/devportal/apis/5fb6b560-ef7e-49ad-b3c7-5335b7ca45f6/documents/89b6b1d0-b3c9-4758-a548-47889825bc68"> here</a>

```python
from mvola import Mvola
from os import environ as env
api = Mvola(env.get('CONSUMER_KEY'), env.get('SECRET_KEY'))

res = api.generate_token()
if res.success :
    api.token = res
    print(res)
else :
    print(f"Status_code[{res.status_code}] \n {res.error}")
```

###### OUTPUT
> Success
```python
    {
        "Success": true,
        "Error": null,
        "Status code": 200,
        "Value": {
            "access_token": "eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjUyMDk2Mzc1LCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjUyMDk5OTc1LCJpYXQiOjE2NTIwOTYzNzUsImp0aSI6Ijk0ZWRlZjIyLTFmYzEtNDYxNS05YzZjLWQxZGQ3MDg1NmFjYyJ9.MQ6ew1r7nMWZN3hI8Xvbv0PuZgsi-GY_IjsO-NeXmALh1KnwOOwhgo1cMu9hRGsXWg3XZexqLagLHRcjYNDXJKR6QuYrop6WzZuGMGsNs-PL_1jrjctOLIS2VGBL1utCdDvhvfYgG-oOs2cisBUIQ7TtHF8haTd0w4WdNVkxt66Jz5ZGhEbOBralbym3-Bgjo_2wbuKy9iY0x6xqr2xMuhPXkgTFyZmAqmUv32zIIyvfC6OiEcfcXF2T3Bm_NqJN8BNXXu8ST3sdU_dEp2wYEf5f4d8LxUygNVv5n9kkdlmLrRWpoEeWfpIcfAeMuMdyLaXAgQj-T7BInM5wECMhYg",
            "scope": "EXT_INT_MVOLA_SCOPE",
            "token_type": "Bearer",
            "expires_in": 3600
        }
    }
```

> Failed [example]
```python
    Status_code[401] 
    {
        'error_description': 'A valid OAuth client could not be found for client_id: 0zL7eTrSEfXf6kwJ53DSegCbBwa', 
        'error': 'invalid_client'
    }
```
The token generated by this function must expire after 3600s by default,to change that go to the dashboard of Mvola API Application in the plaform.

### Initiate Transaction
Check the documentation <a href="https://www.mvola.mg/devportal/apis/5fb6b560-ef7e-49ad-b3c7-5335b7ca45f6/documents/b36ca2a3-f339-43a1-88d3-bbee6c77b06f"> here</a>

```python
from mvola.tools import Transaction

transaction = Transaction(
    token="{{token}}", # [Token] Requiered fields
    user_language="FR", # MG or FR
    user_account_identifier="0343500003", # [UserAccountIdentifier] Requiered fields 
    partner_name="Marketbot", # Name of your application
    amount="1500",
    x_callback_url="https://2809-102-16-43-64.ngrok.io", # Webhook link for client , Mvola sends requests in this links once the transaction is finished 
    currency="Ar", # Possible Values : Ar only
    description_text="Unedescription", # String (len<40Characters)without special character
    request_date="2022-05-06T02:14:59.567Z", # Respect the consraints as in this example
    debit="0343500003", # [Debit] Required fields | Phone number of subscriber .In preprod it’s fixed: 034350003 or 0343500004
    credit="0343500004",  # [Credit] Required fields | Phone number of merchant. In preprod it’s fixed: 034350003 or 0343500004
)

# Init transaction
res = api.init_transaction(transaction)

if res.success :
    print(res.response)
else :
    print(f"Status_code [{res.status_code}] \n {res.error}")
```
###### OUTPUT
> Success :
```python
    {
        'status': 'pending', 
        'serverCorrelationId': '821ff7f5-43e2-4e6e-af47-a8c40150f950', 
        'notificationMethod': 'callback'
    }
```

> Failed [example]:
```python
    Status_code : [401] ,
    {
        'fault': {
            'code': 900901, 
            'message': 'Invalid Credentials', 
            'description': 'Invalid Credentials. Make sure you have given the correct access token'
        }
    }
```

#### Status of Transaction
Check the documentation <a href="https://www.mvola.mg/devportal/apis/5fb6b560-ef7e-49ad-b3c7-5335b7ca45f6/documents/b36ca2a3-f339-43a1-88d3-bbee6c77b06f"> here</a>

```python

from mvola.tools import Transaction

transaction = Transaction(
    token="{{token}}", # [Token] Required fields
    user_language="FR", # MG or FR
    user_account_identifier="0343500003", # [UserAccountIdentifier] Required fields 
    partner_name="Marketbot", # Name of your application
    server_correlation_id='c8e9e922-b965-4515-b390-137b41c9f40b' , # [server_correlation_id] Required fields , The response when you initiate transaction
)

# Status of  transaction
res = api.status_transaction(transaction)

if res.success :
    print(res.response)
else :
    print(f"Status_code [{res.status_code}] \n {res.error}")
```
###### OUTPUT
> Success :
```python
    {
        "status": "success",
        "serverCorrelationId": "821ff7f5-43e2-4e6e-af47-a8c40150f950",
        "notificationMethod": "callback",
        "objectReference": ""
    }
```

> Failed [example]:
```python
    Status_code : [401] ,
    {
        'status': '', 
        'serverCorrelationId': '821ff7f5-73e2-4e6e-af47-a8c40150f950', 
        'notificationMethod': '', 
        'objectReference': ''
    }
```


#### Details of Transaction
Check the documentation <a href="https://www.mvola.mg/devportal/apis/5fb6b560-ef7e-49ad-b3c7-5335b7ca45f6/documents/b36ca2a3-f339-43a1-88d3-bbee6c77b06f"> here</a>

```python
from mvola.tools import Transaction

transaction = Transaction(
    token="eyJ4NXQiOiJPRE5tWkRFMll6UTRNVEkxTVRZME1tSmhaR00yTUdWa1lUZGhOall5TWpnM01XTmpNalJqWWpnMll6bGpNRGRsWWpZd05ERmhZVGd6WkRoa1lUVm1OZyIsImtpZCI6Ik9ETm1aREUyWXpRNE1USTFNVFkwTW1KaFpHTTJNR1ZrWVRkaE5qWXlNamczTVdOak1qUmpZamcyWXpsak1EZGxZall3TkRGaFlUZ3paRGhrWVRWbU5nX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJyaXZvMjMwMkBnbWFpbC5jb21AY2FyYm9uLnN1cGVyIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwibmJmIjoxNjU0MTA4ODg2LCJhenAiOiIwekw3ZVRyU0VmWGY2a2t3SjUzRFNlZ0NiQndhIiwic2NvcGUiOiJFWFRfSU5UX01WT0xBX1NDT1BFIiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ucHJlcC50ZWxtYS5tZzo5NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjU0MTEyNDg2LCJpYXQiOjE2NTQxMDg4ODYsImp0aSI6IjVlOGY5ZjFhLWUxODItNGZkMS04ZjUyLWU2YTIzMzljYTIzMCJ9.voIBGWbGiI7vFklcmHiufu5fW1UvlE79c7MNOZZisuGD7HQ8P4CFljBhbQQj8lHnd8u48KFdLxHWwg4SozDejPlTFmeDdHaE8UoYhTsVthYgG5eKN3ZSQ0LSyYyeLbxA25vssvVSkQBCX-4EtcrH_vgEnZiJotBqD8PhicuwtvJuiqm3lbkFcGpNNtVGlUD8Q_xxBt31Az044qJ3BYTcmnG1tXmjRzQNyNrGe3rnQxbnndqg1gHrr-st8bulgODHWGZ3vKkmpdXnMxAn6sYjPRZ0YOdfdQwpgYK8HpLh1oI8VtTsw8oqTiVXpk-4F00qXjqihVd66len-BS48DIsig",
    user_language="FR",
    user_account_identifier="0343500003",
    partner_name="Marketbot",
    transid="636251274" # Transaction ID [Required] Fields on details transaction   
)
res = api.details_transaction(transaction)
if res.success :
    print(res.response)
else :
    print(f"Status_code [{res.status_code}] \n {res.error}")
```
###### OUTPUT
```python
    {
        'amount': '5555.00', 
        'currency': 'Ar', 
        'requestDate': '2022-06-01T19:15:52.848Z', 
        'debitParty': 
            [
                {
                    'key': 'msisdn', 
                    'value': '0343500003'
                }
            ], 
        'creditParty': 
            [
                {
                    'key': 'msisdn', 
                    'value': '0343500004'
                }
            ], 
        'fees': 
            [
                {'feeAmount': '84'}
            ], 
        'metadata': 
            [
                {
                    'key': 'originalTransactionResult', 
                    'value': '0'
                },
                {
                    'key': 'originalTransactionResultDesc', 
                    'value': '0'
                }
            ], 
        'transactionStatus': 'completed', 
        'creationDate': '2022-06-01T19:07:24.223Z', 
        'transactionReference': '636251282' , #This is the transaction ID
    }

```

## How to contribute ?

- Make a fork of the repository
- TODO List <a href="https://github.com/rivo2302/Mvola/issues/2"> #02 </a>
- Create a Pull Request 

## Contributors

![Image des contributeurs GitHub](https://contrib.rocks/image?repo=rivo2302/Mvola)
