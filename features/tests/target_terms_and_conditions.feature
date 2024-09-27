Feature: Tests for Target terms and conditions page

  Scenario: User is able to open Terms and conditions from sign in page
    Given Open sign in page
    And Store original window
    When Click Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page opened
    And Close current page
    And Return to original window