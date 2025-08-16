Feature: Check initial value in first input field
  In order to ensure the app starts correctly
  As a user
  I want the first input field to have a proper initial value

  Scenario: Verify initial text of first input field
    Given the app is running
    When I read the text of the first input field
    Then the text should be 'Enter the first number'
