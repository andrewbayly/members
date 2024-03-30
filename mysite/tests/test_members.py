"""
Pre-requisite: 

To make the tests work, there needs to be a single team member in the database ( with id=1 )
This member cannot be edited.

The following Test data is fine: 

  Andrew Bayly (admin)
  415-640-2710
  andrew.bayly@mac.com

"""

def test_add_invalid_phone(py):   
    # visit the main page:
    py.visit('http://localhost:8000')

    # click the Add Button:
    py.get("#addButton").click()

    py.get("#id_FirstName").type("Andrew")
    py.get("#id_LastName").type("Smith")
    py.get("#id_Email").type("bogus")
    py.get("#id_Phone").type("bogus")
    
    py.get("#saveButton").click()
    
    #assert that we are coming back to the right page ( Add not Edit )
    assert py.contains('Add a team member')
    
    assert py.contains('Phone number format required: 000-000-0000')

    
def test_add_invalid_email(py):   
    # visit the main page:
    py.visit('http://localhost:8000')

    # click the Add Button:
    py.get("#addButton").click()

    py.get("#id_FirstName").type("Andrew")
    py.get("#id_LastName").type("Smith")
    py.get("#id_Email").type("bogus")
    py.get("#id_Phone").type("999-999-9999")
    
    py.get("#saveButton").click()
    
    assert py.contains('Add a team member')
    
    assert py.contains('The email address is not valid. It must have exactly one @-sign.')
    
    
def test_add_invalid_email_invalid_domain_name(py):   
    # visit the main page:
    py.visit('http://localhost:8000')

    # click the Add Button:
    py.get("#addButton").click()

    py.get("#id_FirstName").type("Andrew")
    py.get("#id_LastName").type("Smith")
    py.get("#id_Email").type("bogus@b.com")
    py.get("#id_Phone").type("999-999-9999")
    
    py.get("#saveButton").click()
    
    assert py.contains('Add a team member')
    
    assert py.contains('The domain name b.com does not exist.')
    
   
    
def test_add_duplicate_email(py):   
    #first, setup a member
    
    # visit the main page:
    py.visit('http://localhost:8000')

    # click the Add Button:
    py.get("#addButton").click()

    py.get("#id_FirstName").type("A")
    py.get("#id_LastName").type("B")
    py.get("#id_Email").type("a.b@mac.com")
    py.get("#id_Phone").type("415-555-1234")
    
    py.get("#saveButton").click()
    
    #now, try to create another member with the same email

    py.visit('http://localhost:8000')

    # click the Add Button:
    py.get("#addButton").click()

    py.get("#id_FirstName").type("C")
    py.get("#id_LastName").type("D")
    py.get("#id_Email").type("a.b@mac.com")
    py.get("#id_Phone").type("415-555-5678")
    
    py.get("#saveButton").click()
    
    assert py.contains('Another Team Member has the same Email Address')
    
  
  