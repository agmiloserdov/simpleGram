Feature: like

  Scenario: Like when signed in
    Given I signed up and I on main page
    When I see a post list
    Then I click to like button
    And I see that the counter has changed
