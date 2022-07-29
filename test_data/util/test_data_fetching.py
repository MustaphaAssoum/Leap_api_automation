from test_data.data.employee.employee import employee_test_data


def create_test_data(endpoint):
    if endpoint == "employee":
        return employee_test_data
    if endpoint == "employee/id":
        return employee_test_data

