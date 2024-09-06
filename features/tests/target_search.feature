# Created by kita at 2024-09-06
Feature: Tests for Target Search functionality

  Scenario: User can search for a product
    Given Open target main page
    When Search for a product
    Then Verify that correct search results shown