*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Create User

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail  Username too short

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekalle
    Set Password  kallekalle
    Submit Credentials
    Register Should Fail  Password has to contain at least one character that is not a letter

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password  kalle456
    Submit Credentials
    Register Should Fail  Passwords do not match

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed
    Go To Main Page
    Click Button  Logout
    Logout Should Succeed
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  k
    Set Password  k
    Submit Credentials
    Register Should Fail  Password too short
    Go To Login Page
    Set Username  kalle
    Set Password  k
    Click Button  Login
    Login Should Fail  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Fail
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Go To Register Page And Create User
    Create User  mikko  mikko123
    Go To Register Page
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Logout Should Succeed
    Login Page Should Be Open

Login Should Fail
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}