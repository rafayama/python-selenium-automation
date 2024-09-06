# Created by kita at 2024-09-06
Feature: Tests Target website for first time visitors

  Scenario: User can verify that cart is empty
    Given Open target main page
    When Click on Cart icon
    Then Verify that your cart is empty message is shown


  Scenario: Logged out user can Sign in
    Given Open target main page
    When Click Sign in
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened
