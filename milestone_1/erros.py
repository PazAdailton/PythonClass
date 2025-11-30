class MyCustomError(TypeError):
    """
       Exception raised error an occured in this application

    """
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code

res =  MyCustomError("OUCH! An error happened.", 500)
print(res.__doc__)