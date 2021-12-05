Feature: Login functionality

  @smoke
  Scenario: User is able to login with valid username and password
    Given User is on login page
    When  User enter valid username "kowalski.2021@o2.pl" in username field
    And   User enter valid password "Mar1234!" in password field
    And   User clicks on SignIn button
    Then  User is logged in


  Scenario Outline: User is not able to login using invalid data - multiple credentials
    Given User is on login page
    When  User enter invalid "<username>" and/or invalid "<password>"
    And   User clicks on SignIn button
    Then  User is not logged in

    Examples: Invalid login credentials
    | username             | password  |
    | kowalski.2021@o2.pl  | Mar1234!! |
    | kowalski.20211@o2.pl | Mar1234!  |
    | kowalski.20211@o2.pl | Mar1234!! |
