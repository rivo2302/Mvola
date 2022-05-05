
class ResultGetToken :

    def __init__(self) -> None:
        self.success =  False 
        self.error =  None
        self.value = None
        self.token = None
        self.status_code = None
    
    def __str__(self) :
        return  str(self.token)