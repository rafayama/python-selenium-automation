# Created by kita at 2024-09-10
Feature: Test for main page UI

  Scenario: Verify header is shown
    Given Open target main page
    Then Verify that header is shown
    And Verify that header has links

#  Scenario: Verify header has correct amount of links
#    Given Open target main page
#    Then Verify that header has 6 links
