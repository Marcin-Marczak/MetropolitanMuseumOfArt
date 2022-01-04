Feature: Login functionality

  Background:
  Given User is on login page

  @smoke
  Scenario: User is able to login with valid email and password
    When  User enter valid email in email field
    And   User enter valid password in password field
    And   User clicks on SignIn button
    Then  User is logged in


  Scenario Outline: User is not able to login using invalid data - multiple credentials
    When  User enter invalid '<email>' and/or invalid '<password>'
    And   User clicks on SignIn button
    Then  User is not logged in

    Examples: Invalid login credentials
    | email                | password  |
    | kowalski.2021@o2.pl  | Mar1234!! |
    | kowalski.20211@o2.pl | Mar1234!  |
    | kowalski.20211@o2.pl | Mar1234!! |
