*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}=    https://www.google.com
${browser}=    Chrome

*** Test Cases ***
demo
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Sleep    5
