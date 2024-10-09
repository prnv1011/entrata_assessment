Note: As the Entrata page was unavailable for the entire afternoon, I was unable to run the test cases. 
However, I had prepared the XPaths prior to the site going down and worked on the login functionality in the meantime. Therefore, the test cases have not yet been run on my laptop.

Test Descriptions
test_homepage_validation()
This test case navigates to the Entrata homepage and validates the page title to ensure it matches the expected value.

test_accept_cookies()
This test checks for any cookie consent pop-ups and automatically accepts them.

test_schedule_your_demo_navigation()
This test clicks on the "Schedule Your Demo" button and validates the new tab's URL and title. It also checks if the form fields for scheduling a demo are present.

test_watch_demo()
This test clicks the "Watch Demo" button and fills in the required fields in the demo request form. It also ensures that all the input fields and dropdowns are functional but does not submit the form.
