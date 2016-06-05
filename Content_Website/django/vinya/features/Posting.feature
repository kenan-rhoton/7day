Feature: Posting

    Scenario: Post as a user
        Given I am logged in with posting capabilities
        And I am on the HomePage
        And I see a New Post button
        When I create a New Post with title "DA TITLE" and content "DA CONTENT"
        Then I should see "DA TITLE" on the HomePage

    Scenario: Post as a user
        Given There is a Post with title "DA TITLE" and content "DA CONTENT"
        And I am logged in with posting capabilities
        And I am on the HomePage
        Then I should see "DA TITLE" on the HomePage
        And I should be able to delete the first Post with title "DA TITLE"

    Scenario: Post page
        Given There is a Post with title "DA TITLE" and content "DA CONTENT"
        And I am on the HomePage
        When I click on the Post title "DA TITLE"
        Then I should see the Post page for "DA TITLE"
