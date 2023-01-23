import subprocess


def get_device_udid():
    output = subprocess.check_output(['adb', 'devices']).decode('ascii')
    device = output.split('\n')[1]
    udid = device.split('\t')[0]
    return udid


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'udid': get_device_udid(),
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
