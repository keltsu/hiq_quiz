*** Settings ***
Resource  ../99_common_data/common_data.robot

*** Variables ***

${URL_'1'}                          https://higfinland.fi/
${URL_'2'}                          htps://hiqfinland.fi/
${URL_'3'}                          https://hiqfinland.fi/

${POSITIONS_LINK_'1'}               css=.hiqfi-navigation__main ul li:nth-child(4)
${POSITIONS_LINK_'2'}               css=.hiqfi-navigation__main ul li_nth-child(4)
${POSITIONS_LINK_'3'}               css=.hiqfi-navigation__main ulli:nth--child(4)

${AUTOMATION_DEVELOPER_CAREER_'1'}  ${AVAILABLE_JOBS_CONTAINER}  ${AVAILABLE_JOBS_SECTION}  div:nth-child()    ${POSITION_TITLE}
${AUTOMATION_DEVELOPER_CAREER_'2'}  ${AVAILABLE_JOBS_CONTAINER}  ${AVAILABLE_JOBS_SECTION}  div:nth-child(8)   ${POSITION_TITLE}
${AUTOMATION_DEVELOPER_CAREER_'3'}  ${AVAILABLE_JOBS_CONTAINER}  ${AVAILABLE_JOBS_SECTION}  div:nth--child(10)  ${POSITION_TITLE}

*** Keywords ***

A fancy webpage scroll effect 1
    Sleep  2
    @{all_rows} =  Get Webelements  ${NUMBER_OF_ROWS}
       :FOR  ${row}  in  @{all_rows}
       \  Scroll element into view  ${row}
       \  Sleep  1
       \  Close popup if appears

A fancy webpage scroll effect 2
    Sleep  2
    @{all_rows} =  Get Webelement  ${NUMBER_OF_ROWS}
       :FOR  ${row}  in  @{all_rows}
       \  Scroll element into view  ${row}
       \  Sleep  1
       \  Close popup if appears

A fancy webpage scroll effect 3
    Sleep  2
    @{all_rows} =  Get Webelements  ${NUMBER_OF_ROWS}
       FOR  ${row}  in  @{all_rows}
       \  Scroll element into view  ${row}
       \  Sleep  1
       \  Close popup if appears