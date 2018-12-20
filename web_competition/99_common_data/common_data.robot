*** Settings ***
Library   SeleniumLibrary
Library   OperatingSystem

*** Variables ***
${WINDOW_WIDTH}                       1820
${WINDOW_HEIGHT}                      980
${CHROMEBROWSER}                      chrome
${BLANK_PAGE}                         about:blank

${HIQ_LOGO}                           css=.hiqfi-navigation__logo svg
${COOKIE_OK_BUTTON}                   css=#accept-cookie
${NEWSLETTER_POPUP}                   css=.leadinModal-content .leadin-preview-wrapper
${NEWSLETTER_POPUP_CLOSE}             css=.leadinModal-content .leadinModal-close
${NEWSLETTER_POPUP_TEXT}              css=div:nth-child(2) .hiqfi-blackbox > div.container

${AVAILABLE_JOBS_CONTAINER}           css=#root div:nth-child(2) section.hiqfi-featuredEntryBlock.hiqfi-white
${AVAILABLE_JOBS_SECTION}             .hiqfi-featuredEntrySection
${POSITION_TITLE}                     .hiqfi-featuredEntry__title
${POSITION_HEADER}                    css=.hiqfi-image-header .hiqfi-image-header__textTitlegroup h1

${NUMBER_OF_ROWS}                     css=#root div:nth-child(2) .hiqfi-markupBox.hiqfi-white p

*** Keywords ***

user goes to HIQ frontpage
    [arguments]  ${direction}
    Run keyword if  '${direction}' == '${direction}'  Go to  ${URL_\'${direction}'}
    Wait until element is visible  ${HIQ_LOGO}
    Accept cookies

user opens avoimet tyopaikat page
    [Arguments]  ${open_jobs}
    Run keyword if  '${open_jobs}' == '${open_jobs}'  Hover on element and click  ${POSITIONS_LINK_\'${open_jobs}'}
    Wait until element is visible  ${AVAILABLE_JOBS_CONTAINER}

user selects test automation developer position
    [Arguments]  ${selected_career}
    Run keyword if  '${selected_career}' == '${selected_career}'  Hover on element and click  ${AUTOMATION_DEVELOPER_CAREER_\'${selected_career}'}
    Wait until element is visible  ${POSITION_HEADER}

user can see information on automation developer career in HiQ
    [Arguments]  ${selected_scroll}
    Run keyword if  '${selected_scroll}' == '${selected_scroll}'  A fancy webpage scroll effect ${selected_scroll}

Hover on element and click
    [Arguments]  ${element}
    Scroll element into view          ${element}
    Wait until element is visible     ${element}
    Mouse Over                        ${element}
    Click element                     ${element}

Close popup if appears
    ${popup}=  Run keyword and return status  Element should not be visible  ${NEWSLETTER_POPUP}
        Run keyword if  ${popup} == True  No operation  ELSE  Click element  ${NEWSLETTER_POPUP_CLOSE}

Accept cookies
    ${status}=  Run keyword and return status  Page should not contain element  ${COOKIE_OK_BUTTON}
       Run keyword if  ${status} == False  Click element  ${COOKIE_OK_BUTTON}
         Wait until element is not visible  ${COOKIE_OK_BUTTON}

User wants to enter competition
    Empty output directory if needed
    Open Browser                      ${BLANK_PAGE}  ${CHROMEBROWSER}
    Set Window Size                   ${WINDOW_WIDTH}  ${WINDOW_HEIGHT}

Empty output directory if needed
    Run keyword if  '${OUTPUT_DIR_EMPTY}' == 'FALSE'  Remove output data

Remove output data
    Remove files  ${OUTPUT_DIR}/*.png  ${OUTPUT_DIR}/*.html
    Set global variable  ${OUTPUT_DIR_EMPTY}  TRUE

Close browser
    Close all browsers
    Run Keyword If All Tests Passed  Conguratulations
    Run Keyword If Any Tests Failed  Better luck next time

Conguratulations
    Add scores to list
    Log to console  ..
    Log to console  ..
    Log to console  ----------------YOU DID IT ${PLAYER} !!!!---------------
    Log to console  ----------------!!!CONGRATULATIONS!!!-----------------
    Log to console  ..
    Log to console  ..
    Log to console  ............You answered all questions correctly in ${TOTAL} seconds !!
    Log to console  ..
    Log to console  ............This quiz was coded using Robot Framework and Python (C) K 2019
    Log to console  ..
    Log to console  ..
    Sleep  3

Add scores to list
    Append To File  web_competition/competitionresults.js  __
    Append To File  web_competition/competitionresults.js  '${PLAYER}'
    Append To File  web_competition/competitionresults.js  '${TOTAL}'
    Copy File       web_competition/competitionresults.js  web_competition/scores/competitionresults.js
    Append To file  web_competition/scores/competitionresults.js  "

Better luck next time
    Log to console  ..
    Log to console  ..
    Log to console  --------------- Some fails occurred ------------------
    Log to console  ---------------BETTER LUCK NEXT TIME!----------------
    Log to console  ..
    Log to console  ..
    Log to console  ............It took ${TOTAL} seconds for you to answer all four questions. :)
    Log to console  ..
    Log to console  ............This quiz was coded using Robot Framework and Python (C) K 2019
    Log to console  ..
    Log to console  ..
    Sleep  3