# Created by kita at 2024-09-10
Feature: Tests for Target Cart

#  Scenario: Verify that User can add item to cart
#    Given Open target main page
#    When Search for BARK Classic Fuzzy Farm Rooster Plush Rope Dog Toy - 9.5"
#    And Click on product image
#    And Click on Add to Cart button
#    Then Verify that cart has items

  Scenario: Verify that cart is empty
    Given Open target main page
    When Click on Cart icon
    Then Verify that "Your cart is empty" is shown