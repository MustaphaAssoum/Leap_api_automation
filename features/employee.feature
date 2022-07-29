Feature: employee resource

  Scenario Outline: Test CREATE operation
     Given I can access the API endpoint
     When I CREATE "<test_data_type>" data with index "<test_data_index>"
     Then I get a "<expected_status_code>" response code
     And schema validation should be "<expected_result>" for the "CREATE" method
     Examples:
     |test_data_type |test_data_index|expected_result|expected_status_code|
     |valid          |0           |successful     |201                 |
     |valid          |1           |successful     |201                 |
     |valid          |2           |successful     |201                 |
     |invalid        |0           |failed         |201                 |
     |invalid        |1           |failed         |201                 |

  Scenario: Test READ operation - multiple entities
     Given I have successfully created "2" entity
     When I READ all the data
     Then I get a "200" response code
     And schema validation should be "successful" for the "READ" method
     And the data must contain the entities I just created

  Scenario: Test using an unsupported method
     Given I can access the API endpoint
     When I use the UPDATE method on the main Resource
     Then I get a "405" response code
