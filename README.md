# members
InstaWork Team Members coding challenge

## Duration
24 hours

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
7. run: python manage.py runserver --insecure
8. goto: http://localhost:8000/

## Open Issues
1. I have attempted to deal with CSRF properly. However I could not get it to
work for the delete view. Instead, I added @csrf_exempt on this view.

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














