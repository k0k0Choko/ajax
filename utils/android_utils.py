def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
