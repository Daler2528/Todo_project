class BedRequestException(Exception):
    def __init__(self,massage,*args):
        super().__init__(*args)

