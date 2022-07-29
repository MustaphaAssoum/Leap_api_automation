# The data below was manually created in order to simulate as many variations of valid and invalid data as needed
employee_test_data = {
    "valid":
        {
            "CREATE": [
                {
                    "FirstName": "John",
                    "LastName": "Smith",
                    "DateOfBirth": "05/10/1985",
                    "StartDate": "01/01/2020",
                    "Department": "Engineering",
                    "JobTitle": "Software Engineer",
                    "Email": "john.smith@yahoo.com",
                    "Mobile": 412341234,
                    "Address": "1 George St, Sydney 2000",
                    "BaseSalary": 200000
                },
                {
                    "FirstName": "Peter",
                    "LastName": "William",
                    "DateOfBirth": "27/10/1999",
                    "StartDate": "01/01/2021",
                    "Department": "Art",
                    "JobTitle": "Musician",
                    "Email": "Peter.William@yahoo.com",
                    "Mobile": 412342222,
                    "Address": "1 George St, Sydney 2000",
                    "BaseSalary": 150000
                },
                # Creating this data should be successful but the API returns an error
                # because the phone number seems to exceed the maximum integer value
                {
                    "FirstName": "Whitney",
                    "LastName": "Davies",
                    "DateOfBirth": "11/02/1990",
                    "StartDate": "05/07/2021",
                    "Department": "HR",
                    "JobTitle": "Recruiter",
                    "Email": "Whitney.Davies@company.com",
                    "Mobile": 61412341234,
                    "Address": "17 pitt St, Perth 6000",
                    "BaseSalary": 210000
                },
            ]

        },
    "invalid":
        {
            "CREATE": [
                # Missing property (LastName)
                {
                    "FirstName": "John",
                    "DateOfBirth": "05/10/1985",
                    "StartDate": "01/01/2020",
                    "Department": "Engineering",
                    "JobTitle": "Software Engineer",
                    "Email": "john.smith@yahoo.com",
                    "Mobile": 412341234,
                    "Address": "1 George St, Sydney 2000",
                    "BaseSalary": 200000
                },
                # Incorrect property type (Mobile str instead of num)
                {
                    "FirstName": "John",
                    "LastName": "Smith",
                    "DateOfBirth": "05/10/1985",
                    "StartDate": "01/01/2020",
                    "Department": "Engineering",
                    "JobTitle": "Software Engineer",
                    "Email": "john.smith@yahoo.com",
                    "Mobile": "123abc",
                    "Address": "1 George St, Sydney 2000",
                    "BaseSalary": 200000
                },
            ],
        }
}