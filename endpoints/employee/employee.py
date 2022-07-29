from endpoints.resource import Resource


class Employee(Resource):

    def __init__(self):
        schema = {
            "CREATE": {
                "type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "FirstName": {"type": "string"},
                    "LastName": {"type": "string"},
                    "DateOfBirth": {"type": "string"},
                    "StartDate": {"type": "string"},
                    "Department": {"type": "string"},
                    "JobTitle": {"type": "string"},
                    "Email": {"type": "string"},
                    "Mobile": {"type": "number"},
                    "Address": {"type": "string"},
                    "BaseSalary": {"type": "number"},
                },
                "required": [
                    "FirstName", "LastName", "DateOfBirth", "StartDate", "Department",
                    "JobTitle", "Email", "Mobile", "Address", "BaseSalary"
                ]
            },
            "READ": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "FirstName": {"type": "string"},
                    "LastName": {"type": "string"},
                    "DateOfBirth": {"type": "string"},
                    "StartDate": {"type": "string"},
                    "Department": {"type": "string"},
                    "JobTitle": {"type": "string"},
                    "Email": {"type": "string"},
                    "Mobile": {"type": "number"},
                    "Address": {"type": "string"},
                    "BaseSalary": {"type": "number"},
                },
                "required": [
                    "FirstName", "LastName", "DateOfBirth", "StartDate", "Department",
                    "JobTitle", "Email", "Mobile", "Address", "BaseSalary"
                ]
              }
            },
            "DELETE": None,
            "UPDATE": None
        }
        post_headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        resource_name = "employee"

        super().__init__(schema, resource_name, post_headers)

    def get_full_resource(self):
        return "employee"






