from endpoints.employee.employee import Employee
from endpoints.employee.id.id import EmployeeId


def create_resource(resource_name):
    if resource_name == "employee":
        return Employee()
    if resource_name == "employee/id":
        return EmployeeId()
