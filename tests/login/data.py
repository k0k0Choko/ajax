login = 'qa.ajax.app.automation@gmail.com'
password = 'qa_automation_password'

negative_cases = [
    ('', '', 'Please fill all required fields.'),
    (login, '', 'Please fill all required fields.'),
    ('', password, 'Please fill all required fields.'),
    ('q'*400, password, 'Wrong login or password')
]
