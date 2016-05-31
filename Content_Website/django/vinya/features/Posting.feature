Feature: Home page

    Scenario: View the Home Page as logged in user
        Given I am logged in with posting capabilities
        And I am on the HomePage
        And I see a New Post button
        When I create a New Post
        Then it should appear on the HomePage
