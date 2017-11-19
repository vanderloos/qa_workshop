Feature: Success page on completion
    User sees a success message when completed the order with order #

Scenario: Success message with order no
    Given there is item: http://dockerized-magento.local/leather-tablet-sleeve.html
    And Add To Cart button is available

    When I put 2 of it to cart
    And complete checkout

    Then I am at Success Page
    And order no. is shown
    And order no. is numerical
