Feature: Cart functionality

  @smoke
  Scenario: User adds 1 item to cart
    Given User is on product page
    When  User adds product to cart
    And   User goes to cart via mini cart
    Then  This product in cart
    And   There's only 1 item in cart
