LOGIN = 'qa.ajax.app.automation@gmail.com'
PASSWORD = 'qa_automation_password'

NEGATIVE_CASES = [
    ('', '', 'Please fill all required fields.'),
    (LOGIN, '', 'Please fill all required fields.'),
    ('', PASSWORD, 'Please fill all required fields.'),
    ('q'*400, PASSWORD, 'Wrong login or password')
]

SIDE_BAR_BUTTONS_CASES = [
    ('press_add_hub', 'com.ajaxsystems:id/toolbarTitle', 'Add hub'),
    ('press_app_settings', 'com.ajaxsystems:id/toolbarTitle', 'Account'),
    ('press_help', 'com.ajaxsystems:id/toolbarTitle', 'Installation Manuals'),
    ('press_report_a_problem', 'com.ajaxsystems:id/title', 'Report a problem'),
    ('press_video_surveillance', 'com.ajaxsystems:id/toolbarTitle', 'Video Surveillance')
]
