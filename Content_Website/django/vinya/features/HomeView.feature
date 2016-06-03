Feature: Home page

    Scenario: View the Home Page as anonymous user
        Given I am not logged in
        And I am on the HomePage
        Then I should see the Latest Posts Block
        And I should see the Login Form
        And I should not see the New Form Button

    Scenario: View the Home Page as logged in user
        Given I am not logged in
        And I am on the HomePage
        When I log in
        Then I should see the Latest Posts Block
        And I should see the Logout Button

    Scenario: Logout as a logged in user
        Given I am not logged in
        And I am on the HomePage
        When I log in
        Then I should be able to logout
        And I should see the Login Form
