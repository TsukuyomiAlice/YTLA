# encode = utf-8

class Response:
    """
    response property
    """
    def __init__(self, success=True, data=None, code=200, msg=None):
        self.success = success
        if data is None:
            data = {}
        self.data = data
        self.code = code
        if msg is None:
            msg = 'success'
        self.msg = msg


    def success(self, data: dict):
        if data is None:
            self.data = {}
        else:
            self.data = data

    def fail(self, code, msg, data: dict= None):
        self.success = False
        self.code = code
        self.msg = msg
        if data is None:
            self.data = {}
        else:
            self.data = data
