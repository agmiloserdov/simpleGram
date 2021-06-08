
Feature: Search

  Scenario: Successful search
    Given I on main page
    When I input text "root" into field "search-field" by id
    Then I see link with "root" username in "root"


  Scenario: Unsuccessful search
    Given I on main page
    When I input text "gh8o7an98p89" into field "search-field" by id
    Then I see empty window with "Поиск не дал результатов"