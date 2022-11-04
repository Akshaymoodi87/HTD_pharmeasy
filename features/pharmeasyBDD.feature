Feature: Medicine_module

  Background: User should be able to search for a medicine and add item to cart in pharmeasy application
    Given User should be able to launch the browser
    Then User should be able to enter homepage of pharmeasy application
    When User should be able to click on medicine module
    And User should be able to click on pincode

  Scenario Outline:
    Then User should be able to enter "<pincode>"
    And User should be able to click on submit
    Then User should be able to search for "<medicine>"
    And User is able to click on search button
    And User should be able to select the product
    Then User should be able to select quantity
    And User is able to click on view cart
    And User is able to add delivery address
    Then User is able to login with "<mobile_number>"
    And User is able to click on send otp
    And User should be able to click on continue


    Examples:
      | pincode  |      medicine     |  mobile_number  |
      | 577301   |      dolo         |   9008240114    |
#      | 572222   |       dolo         |   8217374794    |
      | 560001   |       dolo         |   9008240114`   |
      | 577      |       dolo         |   9008240114    |
      | 1111     |       dolo         |   8217374794    |