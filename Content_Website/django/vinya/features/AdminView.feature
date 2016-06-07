Feature: Admin capabilities
    
    Scenario: Login as an Admin User
        Given I am logged in on the Admin Site
        Then I should see the Admin Panel

    Scenario: Add Section
        Given I am logged in on the Admin Site
        When I add a new Section "Charles" with block "sidebar"
        Then I should see a Section "Charles" on the Section List

    Scenario: Delete Section
        Given I am logged in on the Admin Site
        And There is a Section "Jackie" assigned to "sidebar"
        When I delete the Section "Jackie"
        Then I should not see a Section "Jackie" on the Section List
