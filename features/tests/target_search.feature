# Created by kita at 2024-09-06
Feature: Tests for Target Search functionality

  Scenario: User can search for  coffee
    Given Open target main page
    When Search for coffee
    Then Verify that correct search results shown for coffee

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify that correct search results shown for tea

  Scenario Outline: User can search for product
    Given Open target main page
    When Search for <search_word>
    Then Verify that correct search results shown for <search_result>
    Examples:
    |search_word|search_result |
    |coffee     |coffee        |
    |tea        |tea           |

  Scenario: User can search for any product and find results with images
    Given Open target main page
    When Search for tea
    Then Verify that each result has a name and image