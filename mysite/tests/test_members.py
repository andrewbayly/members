
def test_members(py):
    # visit the main page:
    py.visit('http://localhost:8000')

    # click the Add Button:
    py.get("[id='addButton']").click()

    # assert that resulting page contains text: "Add a team member" :
    assert py.contains('Add a team member')
    
    assert py.contains('Add a team member')