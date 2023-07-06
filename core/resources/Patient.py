from core.Resource import Resource


class Patient(Resource):

    def __init__(self, resource):
        print("From ===> class Patient")
        super().__init__(resource)
