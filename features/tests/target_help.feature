# Created by kita at 2024-09-10
Feature: Tests for Target Help page

  Scenario: Verify that UI elements are shown
    Given Open Target Help page
    Then Verify that Help Title is shown
    And Verify that Help search field is shown
    And Verify that Help search icon is shown
    And Verify that there are 7 boxes in the What would you like to do
    And Verify that there are 2 boxes under
    And Verify that Browse all Help pages title is shown