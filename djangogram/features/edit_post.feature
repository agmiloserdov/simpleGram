Feature: Edit post

  Scenario: Edit users post
    Given I signed up and I on profile page
    When I click to "edit" icon
    Then I see edit post page with heading "Редактирование"
    And I see edit form

  Scenario: Unsuccessful edit post with incorrect title and description
    Given I signed up and I on profile page
    When I click to "edit" icon
    And Input text "xx" into field "title"
    And Input text "xx" into field "description"
    And I upload image into field "image"
    And Submit the form
    Then I see message text "Убедитесь, что это значение содержит не менее 3 символов (сейчас 2)."

  Scenario: Unsuccessful edit post with incorrect filetype
    Given I signed up and I on profile page
    When I click to "edit" icon
    And Input text "xxxx" into field "title"
    And Input text "xxxxx" into field "description"
    And I upload incorrect filetype "file.xxx" into field "image"
    And Submit the form
    Then I see message text "Отправленный файл пуст."

  Scenario: Successful edit post
    Given I signed up and I on profile page
    When I click to "edit" icon
    And Input text "test_title" into field "title"
    And Input text "test_description" into field "description"
    And I upload image into field "image"
    And Submit the form
    Then I see post with title "test_title" and description "test_description"