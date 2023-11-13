*** Settings ***
Resource  resource.robot
Test Setup  Create User and Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  mikko  kalle123
    Output Should Contain  User with username mikko already exists

Register With Too Short Username And Valid Password
    Input Credentials  mi  kalle123
    Output Should Contain  Username too short

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  """"kalle  kalle123
    Output Should Contain  Username contains invalid symbols

Register With Valid Username And Too Short Password
    Input Credentials  kalle  j
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password has to contain at least one letter and one number

*** Keywords ***
Create User and Input Register Command
    Create User  mikko  mikko123
    Input Register Command