import time
import timeit
import sys
import random
from colorama import init
init()
from colorama import Fore, Back, Style
##os.chmod(hiq_pipo\temp\reports\, 777)
##os.chmod("\hiq_pipo\competitionresults.txt", 777)

OUTPUT_DIR_EMPTY = "FALSE"

def loader_demo (s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)

def delay_printloading (s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
        print (Fore.RED),

delay_printloading ("""  LOADING... """)

print ("")
print ("")
print (Style.RESET_ALL)
print (Fore.WHITE + '  ')
loader_demo ("""                                                            .#"
                                                          '##"
                           .in stereo.                 .###+"
                                                      +++##.
                                                    `#@####`
                                                  ` @#########`
                                                   @#+#########
      ,,                                          #############;`
      +@           `                +            ###############
      @#`        :,`               `#          `################;
      ##+        ;@                ##.         #######@+`   '####
      ###        @##               ##@        @#####'        ,###
      ##@        @##              :###       ,#####           ###:
     `###        ###,             '##@       ##@##            ###+
     ,###        ###@             +##+      ,####             ###@
     :###       `###@             ;##`      ####,             ###@
     '###       '###@              .       `###@              ###@
     @###`      @####                      ####`              ###@
    ####+;;;:.:#####@,                     ###@               ###'
  #####+#######################@:         .###.              ;###,
 :################################;       @###               @###
 ################################@@       ##+##              ####
 #######################@@@@''@#+##@`     ####+#'           ;###@
 `###################           ####'    '##@.'@##@`        ###+:
  ,'#######+`  #####             ####    @##:    `###@,    `####
    +####' `   #####             ####`   ###         ;###@'####@
    ,####,     ####'             ####:   ###           :#######.
    ,####:     ####.             ####:   ###           ` #########,
    `####;     ####              ####`   ##+            '############@:
     ####;     ####              ####    ##+          `@#@##``+###########`
     @###:     ###'              ###@    ###        ,######.   `############+`
     .###,     ###               ###;    ######+##########       ++###########@
      '++      ##@               ###     `###############         ,#############:
               ##                 :`      +############.          ` @+###########;
               :`                          ,#########`               `@###########;
                                                        `              `@##########
                                                                          +########+
                                                                           .#######
                                                                              .+@#'

                                                                               """)
print ("")
print (Fore.BLUE + '                     ----- HIQ RoboCon Quiz 2D  (v. 0.9) -----  ')
print (Style.RESET_ALL)


def ask_value(question):
    allowed_values = ['1', '2', '3']
    while True:
        try:
            value_from_user = str(input(question + " "))
            if value_from_user in allowed_values:
                break
        except:
            print("Not an applicable answer. Give a numerical value between 1-3 ")
    return value_from_user

def task_selector(number):
    y=0
    if number == 1:
        y= task1()
    if number == 2:
        y =task2()
    if number == 3:
        y=task3()
    if number == 4:
        y=task4()
    return y

def answer():
    value = ask_value("Your answer to this question is (1, 2, or 3) ? ")
    ANSWER = str(value)
    return ANSWER


def task1():
    print (" Task - Enter HiQ homepage (step 1) ")
    print ("")
    print (" Robot step is: 'Given user goes to HIQ frontpage' ")
    print ("")
    print (Fore.WHITE + 'Question: ')
    print (" Which is the correct URL for 'Go To' -keyword? ")
    print ("")
    print ("")
    print (" 1 - Go to  https://higfinland.fi/")
    print (" 2 - Go to  htps://hiqfinland.fi/")
    print (" 3 - Go to  https://hiqfinland.fi/")
    print (Style.RESET_ALL)
    print (" ---- ")
    print ("")
    ANSWER= answer()
    print ("")
    for i in range(3):
        print ("")
    return ANSWER


def task2():
    print (" Task - Open avoimet tyopaikat page ")
    print ("")
    print (" Robot step is: 'When user opens avoimet tyopaikat page' (step 2) ")
    print ("")
    #print (" Question: ")
    print (Fore.WHITE + 'Question: ')
    print (" Which of these is a possible correct way to write robot for a click event? ")
    print ("")
    print ("")
    print (" 1 - Click element  css=.hiqfi-navigation__main ul li:nth-child(4) ")
    print (" 2 - Click element  css:.hiqfi-navigation__main ul li:nth-child(4) ")
    print (" 3 - Click element  css=.hiqfi-navigation__main ulli:nth--child(4) ")
    print (Style.RESET_ALL)
    print (" ---- ")
    print ("")
    ANSWER = answer()
    print ("")
    for i in range(3):
        print ("")
    return ANSWER

def task3():
    print (" Task - Select test automation developer career from available positions ")
    print ("")
    print (" Robot step is: 'And user selects test automation developer position' (step 3) ")
    print ("")
    #print (" Question: ")
    print (Fore.WHITE + 'Question: ')
    print (" There is some CSS in the code along with some variables! Which line is written correctly? ")
    print ("")
    print ("")
    print (
        " 1 - Click element  ${AVAILABLE_JOBS_CONTAINER}  ${AUTOMATION_DEVELOPER_CAREER_'1'}  ${AVAILABLE_JOBS_CONTAINER}  ${AVAILABLE_JOBS_SECTION}  div:nth-child()  ${POSITION_TITLE} ")
    print (
        " 2 - Click element  ${AVAILABLE_JOBS_CONTAINER}  ${AUTOMATION_DEVELOPER_CAREER_'2'}  ${AVAILABLE_JOBS_CONTAINER}  ${AVAILABLE_JOBS_SECTION}  div:nth-child(8)  ${POSITION_TITLE} ")
    print (
        " 3 - Click element  $[AVAILABLE_JOBS_CONTAINER]  ${AUTOMATION_DEVELOPER_CAREER_'3'}  ${AVAILABLE_JOBS_CONTAINER}  ${AVAILABLE_JOBS_SECTION}  div_nth--child(8)  ${POSITION_TITLE} ")
    print (Style.RESET_ALL)
    print (" ---- ")
    print ("")
    ANSWER = answer()
    print ("")
    for i in range(3):
        print ("")
    return ANSWER

def task4():
    print (" Task - View and scroll selected career information ")
    print ("")
    print (" Robot step is: 'Then user can see information on automation developer career in HiQ' (step 4) ")
    print ("")
    print (" Question: ")
    print (
        " Let's use robot framework for a fancy web page scrolling. Which one of the given FOR loops can actually do the scroll? ")
    print ("")
    for i in range(3):
        print ("")
    print (Fore.WHITE + 'Question: ')
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
    print (Style.RESET_ALL)
    print (" ---- ")
    ANSWER = answer()
    print ("")
    for i in range(3):
        print ("")
    return ANSWER


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

time.sleep(1)
print ("")
print (Fore.WHITE + ' GAME INFO')
print (Style.RESET_ALL)
print (" This is a program which gives you options to fill out missing ")
print (" commands from a robot test with the options you choose.")
print (" Then robot tries to run the tests using given values. ")
print ("")
time.sleep(1)
print (" You will be asked four questions. ")
print (Fore.WHITE + ' Try to be as fast as you can!')
print (Style.RESET_ALL)
time.sleep(1)
print ("")
PLAYER = raw_input(' Enter your name: ')
print ""
raw_input(" Pressing [ENTER] will start the timer. ")
print ""
print (Fore.WHITE + ' ------Ready?------')
print (Style.RESET_ALL)
print ""
print ""
print (Fore.GREEN + ' Timer starts NOW! ')
print ""
print (Style.RESET_ALL)

start = timeit.default_timer()

x=[1, 2, 3, 4]

while len(x)>0:
    value = random.choice(x)
    x.remove(value)
    returned_value = task_selector(value)
    exec('ANSWER'+str(value)+'='+returned_value)


stop = timeit.default_timer()
print (Fore.GREEN + ' Timer -STOP- ')
print (Style.RESET_ALL)
TOTAL =float("{0:.2f}".format(stop - start))
for i in range(3):
    print ("")
time.sleep(1)
print (".....")
print ("...")
print ("..")
print (".")
for i in range(3):
    print ("")
time.sleep(1)
print (" Let's try your robot code now in action !")
print ("")
delay_printloading ("  ...STARTING ROBOT FRAMEWORK")
print (Style.RESET_ALL)
print ("")