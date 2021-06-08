Feature: Create post

  Scenario: Open create post page
    Given I signed up and I on main page
    When I click to profile button
    And I see profile page
    And I click to "Новая публикация" button
    Then I see create post page

  Scenario: Unsuccessful create new post with incorrect title and description
    Given I signed up and I on create post page
    When Input text "xx" into field "title"
    And Input text "xx" into field "description"
    And I upload image into field "image"
    And Submit the form
    Then I see message text "Убедитесь, что это значение содержит не менее 3 символов (сейчас 2)."

  Scenario: Unsuccessful Create new post with incorrect filetype
    Given I signed up and I on create post page
    When Input text "xxxx" into field "title"
    And Input text "xxxxx" into field "description"
    And I upload incorrect filetype "file.xxx" into field "image"
    And Submit the form
    Then I see message text "Отправленный файл пуст."


  Scenario: Create new post
    Given I signed up and I on create post page
    When Input text "test_title" into field "title"
    And Input text "test_description" into field "description"
    And I upload image into field "image"
    And Submit the form
    Then I see post with title "test_title" and description "test_description"

  Scenario: Delete post after create
    Given I signed up and I on profile page
    When I click to "delete" icon
    And I see heading "Вы действительно хотите удалить публикацию?"
    And I click "confirm_delete" button
    Then I see that post has been deleted