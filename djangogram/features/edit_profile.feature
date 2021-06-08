Feature: Edit profile

  Scenario: Open edit profile form
    Given I signed up and I on profile page
    When I click to "Изменить" button
    Then I see edit profile page with "edit-form" form
    And I see "first_name" field
    And I see "last_name" field
    And I see "email" field
    And I see "birth_date" field
    And I see "avatar" field

  Scenario: Edit profile
    Given I signed up and I on profile page
    When I click to "Изменить" button
    And Input text "Test Name" into field "first_name"
    And Input text "Test Last Name" into field "last_name"
    And Input text "test@testmail.com" into field "email"
    And Input text "01/01/1999" into field "birth_date"
    And I upload image into field "avatar"
    And Submit the form
    Then I see profile page
    And I see "Test Name Test Last Name" in "full-name"