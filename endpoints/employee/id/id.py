from endpoints.resource import Resource


class EmployeeId(Resource):

    def __init__(self):
        schema = {
            "READ": {
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
            "CREATE": None,
            "UPDATE": None,
            "DELETE": None
        }
        post_headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        resource_name = "employee/id"

        super().__init__(schema, resource_name, post_headers)

    def get_full_resource(self, employee_id):
        return f'employee/{employee_id}'




