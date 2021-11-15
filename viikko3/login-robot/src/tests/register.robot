*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  teppo123!
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  matti  teppo123!
    Output Should Contain  New user registered
    Input New Command
    Input Credentials  matti  matti123!
    Output Should Contain  User with username matti already exists

Register With Too Short Username And Valid Password
    Input Credentials  m  teppo123!
    Output Should Contain  Username or password not meet requirements

Register With Valid Username And Too Short Password
    Input Credentials  matti  teppo
    Output Should Contain  Username or password not meet requirements

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  tepposeppo
    Output Should Contain  Username or password not meet requirements