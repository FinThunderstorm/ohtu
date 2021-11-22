*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  teppo
    Set Password  teppo123!
    Set Password Confirmation  teppo123!
    Submit Form
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  t
    Set Password  teppo123!
    Set Password Confirmation  teppo123!
    Submit Form
    Register Should Fail With Message  Username too short or contains unallowed characters

Register With Valid Username And Too Short Password
    Set Username  teppo
    Set Password  t
    Set Password Confirmation  t
    Submit Form
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  teppo
    Set Password  teppo123!
    Set Password Confirmation  matti123!
    Submit Form
    Register Should Fail With Message  Both passwords needs to be same

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Form
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
