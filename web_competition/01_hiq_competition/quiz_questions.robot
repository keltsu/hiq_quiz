*** Settings ***
Resource  ../01_hiq_competition/variables_keywords.robot

Suite Setup     User wants to enter competition
Suite Teardown  Close browser

*** Test Cases ***
Task 1 - Enter HIQ homepage
        Given user goes to HIQ frontpage  ${ANSWER1}

Task 2 - Open careers
        When user opens avoimet tyopaikat page  ${ANSWER2}

Task 3 - Select a career in test automation
        And user selects test automation developer position  ${ANSWER3}

Task 4 - View and scroll down career information
        Then user can see information on automation developer career in HiQ  ${ANSWER4}