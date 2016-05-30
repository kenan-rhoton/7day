Feature: Home page

    Scenario: View the Home Page as anonymous user
        Given I am not logged in
        And I am on the HomePage
        Then I should see the Latest Posts Block

    Scenario: View the Home Page as logged in user
        Given I am not logged in
        And I am on the HomePage
        Then I should see the Latest Posts Block
