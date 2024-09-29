# Created by kita at 2024-09-24
Feature: Tests login

  Scenario: User can sign in
    Given Open target main page
    When Click Sign in
    And From right side navigation menu, click Sign In
    And Input email and password on SignIn page
    And Click Sign in with password
    Then Verify that user is logged in

  Scenario: User can't sign in
    Given Open target main page
    When Click Sign in
    And From right side navigation menu, click Sign In
    And Input wrong email and password on SignIn page
    And Click Sign in with password
    Then Verify that user is not logged in