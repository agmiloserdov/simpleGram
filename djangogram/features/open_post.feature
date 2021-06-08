Feature: Open post page

  Scenario: Open post page from profile
    Given I signed up and I on profile page
    When I click to "details" icon link
    Then I see post page