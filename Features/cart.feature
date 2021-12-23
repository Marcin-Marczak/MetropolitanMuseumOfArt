Feature: Cart functionality

  @smoke
  Scenario: User adds first item from first category to cart and sees this item in cart
    When User navigates to first category
    And  User goes to first subcategory of first category
    Then User is on first subcategory page
    When User opens product page of first product
    Then User is on product page
    When User adds product to bag
    And  User goes to bag
    Then User sees first product from first category/first subcategory in bag
