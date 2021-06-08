Feature: Logout


  Scenario: Successful logout from app
    Given I signed up and I on main page
    When I click to logout button
    Then Site redirect me to login page