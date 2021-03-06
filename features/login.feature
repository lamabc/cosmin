Feature: Login
  In order to use the app the user must be able to Login

  Scenario: Login Success
    Given the user has the correct credentials
    When the user enters test@drugdev.com username
    And the user enters supers3cret password
    And clicks Login
    Then the user is presented with a welcome message       Welcome Dr I Test

  Scenario: Login Incorrect credentials
    Given the user has the incorrect credentials
    When the user enters test@drugdev.com3 username
    And the user enters supers3cret2 password
    And clicks Login
    Then the user is presented with a error message Credentials are incorrect