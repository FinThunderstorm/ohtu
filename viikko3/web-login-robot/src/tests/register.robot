*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Clean Users

*** Test Cases ***
Register With Valid Username And Password
    Create User  teppo  teppo123!  teppo123!
    Register Should Succeed

Register With Too Short Username And Valid Password
    Create User  t3  teppo123!  teppo123!
    Register Should Fail With Message  Username too short or contains unallowed characters

Register With Valid Username And Too Short Password
    Create User  teppo  t  t
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Create User  teppo  teppo123!  matti123!
    Register Should Fail With Message  Both passwords needs to be same

Login After Successful Registration
    Create User  teppo  teppo123!  teppo123!
    Register Should Succeed
    Go To Login Page
    Login User  teppo  teppo123!
    Login Should Succeed

Login After Failed Registration
    Create User  t3  teppo123!  teppo123!
    Register Should Fail With Message  Username too short or contains unallowed characters
    Go To Login Page
    Login User  t3  teppo123!
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Go To Register Page And Clean Users
    Go To Register Page
    Reset Application

Create User
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password_confirmation}
    Submit Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}