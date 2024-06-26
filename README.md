# members
InstaWork Team Members coding challenge

## Duration
24 hours

## Updates

| Issue | Resolution | 
|-------|------------|
| Navigation: not mapped urls give me an a hard 404 server error, e.g.: http://127.0.0.1:8000/bogus. | FIXED by setting DEBUG flag in settings to False, and adding custom 404 error page. Also add the --insecure option when using runserver. |
| System integrity: I was able to delete all users. Let's assume that only admins would be able to add users, how we could setup the app to prevent a dead-end situation? | Approach: Stop user from editing himself. Note that I have successfully used exactly this approach at Domino Data Lab, where we had this exact problem. Method: Add a method in the back-end that gets the "current" user. The idea here is that if we added authentication, then this method would communicate with the Authentication module to bring back the current user id. In the demo, this is hard-coded to 1. The form checks the current_user field, and disables the link for the current user. I also added a tool-tip so you can see the difference. Possible Improvement: The above guards the user from editing himself in the front-end only. A malicious user could still disable the system by typing in the edit URL, and changing the role to Regular, so protecting the back-end would be a natural next step. |
| System integrity: I was able to create members with the same email / phone number, ending up with duplicate records | Added validation for Email and Phone fields, first on database, then in the back-end, transforming the db error messages into friendly ones, and then on the front-end in the template.|
| Input Validation: I was able to enter bogus for both email and phone number. | Add placeholders for Input fields. Add server-side validation for email address and phone number. Note: I used a new module - email_validator which needs to be installed - see Deployment instructions. | 
| Accessibility: Could we apply some best practices for accessibility, e.g. title for actionable elements. | Added Title for Input Fields and Buttons |
| Data model: The member model has field called Admin, which is a boolean field. This may be limiting consider that already support 2 roles, which could be expanded in the future. | Modify Model - Replace Admin(True/False) with Role(Integer, default=1, where 1=Regular, 2=Admin) |
| Tests: As you outlined the testing has been done manually, it would great to validate some of the functionality via tests | Created a Pylenium Test Suite. Note that this requires not only Pylenium, but also upgrade to the python and django versions. Pylenium Tests can be found in members/mysite/tests | 
| UX: Significant non-reversible actions should be confirmed by users before executing. E.g. delete a user. | Add Confirm message when deleting a user | 




## Dependencies
1. Python, at least version: 3.12.2
2. Django, at least version: 5.0.3

## Deployment & Run
To deploy and run the project on your Mac, follow these steps: 

1. Install python
2. Create and activate a venv
3. pip install email_validator
4. pip install pyleniumio
5. pip install setuptools
6. Install django
7. clone the code-base
8. cd into: /members/mysite
9. run: python3.12 manage.py migrate
10. run: python3.12 manage.py runserver --insecure
11. goto: http://localhost:8000/

### Automated Test with Pylenium

#### Pre-reqs

To make the tests work, there needs to be a single team member in the database ( with id=1 )
This member cannot be edited.

Enter the following record before running the tests: 

  Andrew Bayly (admin)
  415-640-2710
  andrew.bayly@mac.com

#### Steps

1. run the server in a separate terminal window: python3.12 manage.py runserver --insecure 
2. cd into /members/mysite
3. run: python3.12 -m pytest tests

## Open Issues
1. I have attempted to deal with CSRF properly. However I could not get it to
work for the delete view. Instead, I added @csrf_exempt on this view.

## (Manual) Test Steps
I decided to test the front-end manually AND use Pylenium. Here are a list of scenarios and test steps/expectations that I used for manual testing.

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

![image](https://github.com/andrewbayly/members/assets/99320/94cf1ea9-c67f-44c0-b00e-834f2834b1a7)

![image](https://github.com/andrewbayly/members/assets/99320/517b6c93-12eb-4512-8c59-05eb8abccff0)

![image](https://github.com/andrewbayly/members/assets/99320/725db74d-0e3d-4b4d-9f3d-2f805dc796f2)


## Approach
I took an iterative approach. First iteration, I just wanted to get something working, and to do this, I used HTML elements, but no HTML form. I also did not use the Django Form class. Second iteration, I used Django form class, created
a MemberForm subclass, and utilized this to create an HTML form. In my first iteration, I spent some time trying to get the radio button to work, and curiosly, this problem was easily solved when I switched to using Django form.

## Overview (of the code)
This may be helpful - a breakdown of the main code in the repo, and what does what: 

| File        | Description |
| ----------- | ----------- |
| mysite/members/views.py  | Views       |
| mysite/members/urls.py  |  URL patterns      |
| mysite/members/models.py | Models        |
| mysite/members/forms.py      |  Forms      |
| mysite/members/templates/members/edit.html | Edit Template       |
| mysite/members/templates/members/index.html | Main Screen Template       |
| mysite/members/static/members/style.css   | Styles (CSS)       |
| mysite/tests   | Automated Tests (Pylenium) |















