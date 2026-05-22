# Build a User Configuration Manager

# Description :
'''
Build a User Configuration Manager
In this lab, you will build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications. You will implement functions to add, update, delete, and view user settings.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair

add_setting function should:

Convert the key and value to lowercase.
If the key setting exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return Setting '[key]' added with value '[value]' successfully!.
The messages returned should have the key and value in lowercase.
You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

update_setting function should:

Convert the key and value to lowercase.
If the key setting exists, update its value in the given dictionary of settings and return: Setting '[key]' updated to '[value]' successfully!
If the key setting doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
The messages returned should have the key and value in lowercase.
You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.

delete_setting function should:

Convert the key passed to lowercase.
If the key setting exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]' deleted successfully!
If the key setting does not exist, return Setting not found!
The messages returned should have the key in lowercase.
You should define a function named view_settings with one parameter representing a dictionary of settings.

view_settings function should:

Return No settings available. if the given dictionary of settings is empty.
If the dictionary contains any settings, return a string displaying the settings. The string should start with Current User Settings: followed by the key-value pairs, each on a new line and with the key capitalized. For example, view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) should return:
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high

For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.

Tests:
Passed:1. You should create a dictionary named test_settings and add some values to it.
Passed:2. You should define a function named add_setting.
Passed:3. The add_setting function should have two parameters.
Passed:4. add_setting should convert the key to lowercase.
Passed:5. add_setting should convert the value to lowercase.
Passed:6. add_setting({'theme': 'light'}, ('THEME', 'dark')) should return the error message Setting 'theme' already exists! Cannot add a new setting with this name..
Passed:7. add_setting({'theme': 'light'}, ('volume', 'high')) should add a new key-value pair and return the success message Setting 'volume' added with value 'high' successfully!.
Passed:8. add_setting should correctly add the given key-value pair to the dictionary.
Passed:9. You should define a function named update_setting.
Passed:10. The update_setting function should have two parameters.
Passed:11. The update_setting function should convert key to lowercase.
Passed:12. The update_setting function should convert value to lowercase.
Passed:13. update_setting({'theme': 'light'}, ('theme', 'dark')) should update an existing key and return the success message Setting 'theme' updated to 'dark' successfully!.
Passed:14. update_setting({'theme': 'light'}, ('volume', 'high')) should return the error message Setting 'volume' does not exist! Cannot update a non-existing setting. when the key doesn't exist.
Passed:15. update_setting should correctly update the given key-value pair in the dictionary.
Passed:16. You should define a function named delete_setting.
Passed:17. The delete_setting function should have two parameters.
Passed:18. delete_setting should convert the key to lowercase.
Passed:19. delete_setting({'theme': 'light'}, 'theme') should remove the existing key and return the success message Setting 'theme' deleted successfully!.
Passed:20. delete_setting should return the error message Setting not found! when the key doesn't exist.
Passed:21. delete_setting should correctly remove the given key from the dictionary.
Passed:22. You should define a function named view_settings.
Passed:23. The view_settings function should have one parameter.
Passed:24. view_settings should return the message No settings available. if the given dictionary is empty.
Passed:25. view_settings should return formatted settings for non-empty dictionary.
Passed:26. view_settings should capitalize the first letter of each setting name.
Passed:27. view_settings should display the correct results and end with a newline character.

[
        You are building a settings manager (like in a mobile app or website).
        It stores user settings like:
        theme → dark/light
        language → english/hindi
        notifications → on/off
        All settings are stored in a dictionary.
]
'''
# Source Code:
def add_setting(settings,item):
    key,value=item
    key=key.lower()
    value=value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings,item):
    key,value=item
    key=key.lower()
    value=value.lower()
    if key in settings:
        settings[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings,key):
    key=key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    result="Current User Settings:\n"
    for key,value in settings.items():
        result+=f"{key.capitalize()}: {value}\n"
    return result


test_settings={
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
}