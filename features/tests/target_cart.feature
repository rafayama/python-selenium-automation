# Created by kita at 2024-09-10
Feature: Tests for Target Cart

  Scenario: Verify that User can add item to cart
    Given Open target main page
    When Search for BARK Super Chewer Cow Dog Toy - Mad Cow
    Then Click on product image
    And Click on Add to Cart button
    And Verify that cart has items

