#import random


#def ask_value(question):
#    allowed_values = ['1', '2', '3']
#    while True:
#        try:
#            value_from_user = str(input(question + " "))
#            if value_from_user in allowed_values:
#                break
#        except:
#            print("Not an applicable answer. Give a numerical value between 1-3 ")
#    return value_from_user



def task_selector(number):
    y=0
    if number == 1:
        print ("nonnii ykkonen")
        y= task1()
    if number == 2:
        print ("nonnii kakkonen")
        y =task2()
    if number == 3:
        print ("nonnii kolomone")
        y=task3()
    if number == 4:
        print ("nonnii nelone")
        y=task4()
    print("value of y= " + str(y))
    return y

def answer():
    value = ask_value("Answer to this question is (1, 2, or 3) ? ")
    ANSWER = str(value)
    return ANSWER


def task1():
    print (" Task  - Enter HiQ homepage (step 1) ")
    print ("")
    print (" Robot step is: 'Given user goes to HIQ frontpage' ")
    print ("")
    print (" Question: ")
    print (" Which is the correct URL for 'Go To' -keyword? ")
    print ("")
    print ("")
    print (" 1 - Go to  https://higfinland.fi/")
    print (" 2 - Go to  htps://hiqfinland.fi/")
    print (" 3 - Go to  https://hiqfinland.fi/")
    print (" ---- ")
    print ("")
    ANSWER= answer()
    print ("")
    for i in range(3):
        print ("")
    print("TASK1 RETURNS " + ANSWER)
    return ANSWER

def task2():
    print (" Task  - Open avoimet tyopaikat page (step 2) ")
    print ("")
    print (" Robot step is: 'When user opens avoimet tyopaikat page' ")
    print ("")
    print (" Question: ")
    print (" Which of these is a possible way to write robot for a click event? ")
    print ("")
    print ("")
    print (" 1 - Click element  css=.hiqfi-navigation__main ul li:nth-child(4) ")
    print (" 2 - Click element  css:.hiqfi-navigation__main ul li:nth-child(4) ")
    print (" 3 - Click element  css=.hiqfi-navigation__main ul li:nth-child(4) ")
    print (" ---- ")
    print ("")
    ANSWER = answer()
    print ("")
    for i in range(3):
        print ("")
    return ANSWER

def task3():
    print (" Task  - Select test automation developer career from all available positions (step3) ")
    print ("")
    print (" Robot step is: 'And user selects test automation developer position' ")
    print ("")
    print (" Question: ")
    print (" There is some CSS in the line along with some variables! Which line is written correctly? ")
    print ("")
    print ("")
    print (
        " 1 - Click element  ${AVAILABLE_JOBS_CONTAINER}  ${AUTOMATION_DEVELOPER_CAREER_'1'}  ${AVAILABLE_JOBS_CONTAINER}  ${AVAILABLE_JOBS_SECTION}  div:nth-child()  ${POSITION_TITLE} ")
    print (
        " 2 - Click element  ${AVAILABLE_JOBS_CONTAINER}  ${AUTOMATION_DEVELOPER_CAREER_'2'}  ${AVAILABLE_JOBS_CONTAINER}  ${AVAILABLE_JOBS_SECTION}  div:nth-child(7)  ${POSITION_TITLE} ")
    print (
        " 3 - Click element  $[AVAILABLE_JOBS_CONTAINER]  ${AUTOMATION_DEVELOPER_CAREER_'3'}  ${AVAILABLE_JOBS_CONTAINER}  ${AVAILABLE_JOBS_SECTION}  div_nth--child(7)  ${POSITION_TITLE} ")
    print (" ---- ")
    print ("")
    ANSWER = answer()
    print ("")
    for i in range(3):
        print ("")
    return ANSWER

def task4():
    print (" Task  - View and scroll selected career information (step 4) ")
    print ("")
    print (" Robot step is: 'Then user can see information on automation developer career in HiQ' ")
    print ("")
    print (" Question: ")
    print (
        " Let's use robot for a fancy web page scrolling. Which one of the given FOR loops can actually do the scroll? ")
    print ("")
    for i in range(3):
        print ("")
    print (" 1 -         ---Scroll effect 1--- ")
    print ("    @{all_rows} =  Get Webelements  ${NUMBER_OF_ROWS} ")
    print ("       :FOR  ${row}  in  @{all_rows} ")
    print ("       \  Scroll element into view  ${row} ")
    print ("       \  Sleep  1 ")
    print ("       \  Close popup if appears ")
    for i in range(3):
        print ("")
    print ("  2 -       ---Scroll effect 2--- ")
    print ("    @{all_rows} =  Get Webelement  ${NUMBER_OF_ROWS} ")
    print ("       :FOR  ${row}  in  @{all_rows} ")
    print ("       \  Scroll element into view  ${row} ")
    print ("       \  Sleep  1 ")
    print ("       \  Close popup if appears ")
    for i in range(3):
        print ("")
    print ("  3 -       ---Scroll effect 3--- ")
    print ("    @{all_rows} =  Get Webelements  ${NUMBER_OF_ROWS} ")
    print ("       FOR  ${row}  in  @{all_rows} ")
    print ("       \  Scroll element into view  ${row} ")
    print ("       \  Sleep  1 ")
    print ("       \  Close popup if appears ")
    print ("")
    print (" ---- ")
    ANSWER = answer()
    print ("")
    for i in range(3):
        print ("")
    return ANSWER


x=[1, 2, 3, 4]

while len(x)>0:
    value = random.choice(x)
    x.remove(value)
    print("QUESTION IS " + str(value))
    returned_value = task_selector(value)
    exec('yyy=6')

    exec('ANSWER'+str(value)+'='+returned_value)
    print(yyy)
    print("RETURNED VALUE: "+str(returned_value))


print("1: " +str(ANSWER1))
print("2: " +str(ANSWER2))
print("3: " +str(ANSWER3))
print("4: " +str(ANSWER4))