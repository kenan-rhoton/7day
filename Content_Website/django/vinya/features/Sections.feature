Feature: Sections

    Scenario: Post with a section
        Given There is a Section "Jackie" assigned to "sidebar"
        And I am logged in with posting capabilities
        And I am on the HomePage
        When I create a New Post on section "Jackie" with title "DA TITLE" and content "DA CONTENT"
        Then I should see a link to "DA TITLE" on the HomePage inside the "sidebar"

    Scenario: Post with section has link
        Given There is a Section "Jackie" assigned to "sidebar"
        And There is a Post assigned to section "Jackie" with title "DA TITLE" and content "DA CONTENT"
        And I am on the HomePage
        When I click on the link to "DA TITLE" inside the "sidebar"
        Then I should see the Post page for "DA TITLE"
