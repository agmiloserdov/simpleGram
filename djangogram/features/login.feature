Feature: Login

  Scenario: Successful login into app
    Given Open "login" page
    When Input text "root" into field "username"
    And Input text "root" into field "password"
    And Submit the form
    Then I see main page

  Scenario: Unsuccessful login into app
    Given Open "login" page
    When Submit the form
    Then I see login page
    And I see message text "Логин или пароль некорректны"
