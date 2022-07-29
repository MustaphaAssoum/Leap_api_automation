Feature: employee/id resource

  Scenario: test READ operation - single entity
     Given I have successfully created 1 entity using the "employee" resource
     When I READ the data using its id
     Then I get a "200" response code
     And the received data matches what I created

  Scenario: test UPDATE operation
     Given I have successfully created 1 entity using the "employee" resource
     When I UPDATE one of its properties "FirstName" to a new value "Bob"
     Then I get a "200" response code
     And I can READ the data using its id
     And the received data matches what I updated

  Scenario: test DELETE operation status
     Given I have successfully created 1 entity using the "employee" resource
     When I DELETE this entity using its id
     Then I get a "200" response code
     And I can READ the data using its id
     And I get a "404" response code

  Scenario: test DELETE operation
     Given I have successfully created 1 entity using the "employee" resource
     When I DELETE this entity using its id
     And I READ the data using its id
     Then I get a "404" response code