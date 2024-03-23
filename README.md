# members
InstaWork Team Members coding challenge

## Dependencies
1. Python, at least version: 3.6.3
2. Django, at least version: 3.2.25

## Deployment & Run
To deploy and run the project on your Mac, follow these steps: 

1. Install python
2. Create and activate a venv
3. Install django
4. clone the code-base
5. cd into: /members/mysite
6. run: python manage.py migrate
7. run: python manage.py runserver
8. goto: http://localhost:8000/

## Open Issues
1. On the Edit and Add screens, there are radio buttons for the Role of the Team Member. According to the wire-frame, the buttons should be on the right, and the text on the left. I researched how to achieve this with a radio-button and could not find a straight-forward answer. I did find discussions where it is asserted that the buttons look better on the left, and that's why standard radio buttons are designed that way. So, in the real-world, I would want to hash this out with UX Team, to understand better what is intended, and if it would be worth the effort to make a custom control.

## Test Steps
I decided to test the front-end manually. Here are a list of scenarios and test steps/expectations that I used.

Test Scenarios

Scenario: Empty List
Steps
* go to http://localhost:8000
* Inspect the resulting screen comparing against wire-frame (List View).

Scenario: Add Admin Team Member
Steps
* go to http://localhost:8000
* Click on blue plus sign in top right corner of page
* Inspect the resulting screen comparing against wire-frame (Add View).
* enter the four fields as follows: Jo, Flint, jo.flint@mac.com, 415-555-2345, select Admin. 
* Click Save.
* find Jo Flint and verify that she is an Admin.
* Count the Team Members in the list, and verify the count at the top of the page.

Scenario: Add regular Team Member
Steps
* go to http://localhost:8000
* Click on blue plus sign in top right corner of page
* enter the four fields as follows: Jo2, Flint2, jo2.flint2@mac.com, 415-555-2345, select Regular. 
* Click Save. 
* find Jo2 Flint2 and verify that she is not an Admin

Scenario: Edit Team Member.
Steps
* go to http://localhost:8000
* find Jo Flint (admin) and click on her name.
* Edit the first field from Jo to Jo3
* Click Save
* Check there is an entry for Jo3 Flint (admin)

Scenario: Delete Team Member
Steps
* go to http://localhost:8000
* find Jo3 Flint (admin) and click on her name.
* Verify that the Edit screen appears
* Click Delete
* Verify that Jo3 Flint was removed from the list.



## Screen-shots

![image](https://github.com/andrewbayly/members/assets/99320/47c76184-323d-4694-b6c8-8c4165c7c314)

![image](https://github.com/andrewbayly/members/assets/99320/fde398a9-819a-4a59-8a61-4a296a6b775b)

![image](https://github.com/andrewbayly/members/assets/99320/2e535139-dcab-4466-ab52-b116ffca4aac)




