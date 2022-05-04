import requests 

class PyMvola :

    def __init__(self,consumer_key,consumer_secret,statut="SANDBOX") -> None :

        """
        An API that will make it easier for you to manage 
        your Mvola API.

        Args:
            consumer_key ( str ): Consumer key of the application's API
            consumer_secret (str ): Consumer secret of the application's API
            statut (str, optional): The status of your API (SANDBOX : Developer Mode / PRODUCTION : Api deployé). Defaults to "SANDBOX".
        """

        self.key = consumer_key
        self.secret = consumer_secret
        self.type = statut
    
    def generate_token(self) :

        """
        A function to generate a token for the Mvola API.
        """ 
        
        url = 'https://devapi.mvola.mg/token' if self.type == "SANDBOX"  else "https://api.mvola.mg/token"
        print(url)


        
api = PyMvola("rivofoebg","obvuds")
api.generate_token()