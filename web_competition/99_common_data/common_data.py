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
        time.sleep(0.0001)

def delay_printloading (s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
        print (Fore.RED),

delay_printloading ("""    LOADING... """)
print ("")
print ("")
print (Style.RESET_ALL)
print (Fore.WHITE + '  ')

loader_demo ("""         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy:`   /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/`      hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy-        .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs.           ...-+hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMd/NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmo`                   +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMo /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmNMMMMMMMMMMMMMMMMMMMm+`                      sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMN-  oMMMMMMMMMMMMMMNohMMMMMMMMMMMMMMMMMMMMMMMMMMMMs :MMMMMMMMMMMMMMMMMd/                          oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMd   `mMMMMMMMMMMMMMm` /NMMMMMMMMMMMMMMMMMMMMMMMMMy   hMMMMMMMMMMMMMMN/           `.:+syhhhy+-      sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMo    sMMMMMMMMMMMMMh   -NMMMMMMMMMMMMMMMMMMMMMMMm`   `mMMMMMMMMMMMMh.        -ohmNMMMMMMMMMMMy`    .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMM/    +MMMMMMMMMMMMM/    /MMMMMMMMMMMMMMMMMMMMMMM/     mMMMMMMMMMMMs       `+mMMMMMMMMMMMMMMMMMs     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMN.    :MMMMMMMMMMMMN`     dMMMMMMMMMMMMMMMMMMMMMN-    .NMMMMMMMMMMs       /mMMMMMMMMMMMMMMMMMMMd     /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMN`    .NMMMMMMMMMMMy      sMMMMMMMMMMMMMMMMMMMMMM:   `yMMMMMMMMMMy      `hMMMMMMMMMMMMMMMMMMMMMd     :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMd     `mMMMMMMMMMMM-      +MMMMMMMMMMMMMMMMMMMMMMdoohNMMMMMMMMMMd`     -mMMMMMMMMMMMMMMMMMMMMMMs     -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMs      yMMMMMMMMMMh       -mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.     :NMMMMMMMMMMMMMMMMMMMMMMM-     /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMy...:+sh-      `------::::`         .:/+++oosyhdmNMMMMMMMMMMMMMMMMMMMMM+     -NMMMMMMMMMMMMMMMMMMMMMMMd      sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMM/                                                 `.:/sdMMMMMMMMMMMMMMh      dMMMMMMMMMMMMMMMMMMMMMMMM:     `mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMm.                                                      `+mMMMMMMMMMMN-      -hMMMMMMMMMMMMMMMMMMMMMMy      :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMd`                                   ``..--:::///:.       +NMMMMMMMMs         ./ymMMMMMMMMMMMMMMMMMm`     `dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMs                   ``         .ohmNNMMMMMMMMMMMMMNs`     .dMMMMMMm`    :ys+/-.  `-+sdNMMMMMMMMMMN-      +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMdhy/         .+shmNMMh`       dMMMMMMMMMMMMMMMMMMMMh      .NMMMMMo    `mMMMMMMNmhs+:.``-/oyhmNNm:      .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMM-       :MMMMMMMMd       -MMMMMMMMMMMMMMMMMMMMMN.      sMMMMN.    sMMMMMMMMMMMMMMNds:`    `       `dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMM/       :MMMMMMMMo       sMMMMMMMMMMMMMMMMMMMMMm`      oMMMMd    `mMMMMMMMMMMMMMMMMMMMdo`         ./+oyhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMs       -MMMMMMMM+      .NMMMMMMMMMMMMMMMMMMMMMy       hMMMMd    -MMMMMMMMMMMMMMMMMMMMh/`                 `.:+oydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMm`      -MMMMMMMM/      yMMMMMMMMMMMMMMMMMMMMMMo      -NMMMMN.   -MMMMMMMMMMMMMMMMmy/.      `+mmy/`               `-/shmMMMMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMs      :MMMMMMMM+     /MMMMMMMMMMMMMMMMMMMMMMMo      yMMMMMM+    /dmmNNNNmmdhs+:`        `+mMMMMMNy/`                  `:ohNMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMy`   .hMMMMMMMMs    -NMMMMMMMMMMMMMMMMMMMMMMMy     +MMMMMMMN.                         -yNMMMMMMMMMMNy:                    `:yNMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMNhydMMMMMMMMMMd   -mMMMMMMMMMMMMMMMMMMMMMMMMMy:-:yMMMMMMMMMm:                    `:smMMMMMMMMMMMMMMMMms-                    `/mMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo/sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh/.            `-/sdNMMMMMMMMMMMMMMMMMMMMMMmy/.                   +NMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhhhhhhddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy+-                -mMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds/-`           -MMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmyo/-`     .MMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMNdyssmMMMMMMMMMM
         MMMMMMN` `````:yMMMMMMMMMMMMMo sMMMMMMMMMMMMMMMMMMMm/.```-sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy:````:yMMMMMMMMMMMMMMy`+MMMMMMMMMMMMMMMMMMN+````:dMMh `````-oNMMMMMMMMM
         MMMMMMN `MMMMm. hMMMMMNNMMMMMo oMNNMMMMMMMMNNMMMMMm``hMMNo :MMMMMNNNMMMMMMMMMNNMMMMMMMMo :mMMm: oMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMM+.yMMd `MMy /MMMNs .NMMMMMMMM
         MMMMMMN `MMMMm. hMMy.`.``/NMMo ---``oMMMh-`.``/mMMo +MMMMMMMMMN+``.`.sMMM` /.. -dMMMMMM. dMMMMd .MMh :MMMy /MMy +MM/...`  dMMMMMMMMMMMMMo /MMy /MMMMM: hMMMMMMMM
         MMMMMMN  ```` :yMMd -NMMs /MMo +MMN- dMm .NMMh -MMo +MMMMMMMMM+ +MMN: yMM  mMMh .MMMMMM. dMMMMm .MMh :MMMy /MMy +MMMMMd-`hMMMMMMMMMMMMm- oMMMy /MMMMM: hMMMMMMMM
         MMMMMMN `MMM: oMMMy /MMMd -MMo oMMM/ yMd :MMMN `MMs +MMMMMNNMM/ hMMMo oMM  MMMN `MMMMMM. dMMyoh .MMh :MMMy /MMy +MMMMo /NMMMMMMMMMMMMs`.dMMMMy /MMMMM: hMMMMMMMM
         MMMMMMN `MMMM: +MMd .mMN+ +MMo /NMN. dMN``dMMs :MMm``yNMm+ :MMo /NMm- hMM  MMMN `MMMMMMs -dNd-  /MMm .mMN+ /MMy +MMd.`yMMMMMMMMMMMMm- +NNNNMMy /NNNmo .NMMMMMMMM
         MMMMMMN..MMMMM/`oMMh:```-oMMMs`/-.`-yMMMd/.``.+NMMMm+.``.:yMMMMs-```:yMMM..MMMN..MMMMMMMh/.``./s-/MMy-``-/`+MMy`oMM-`.....sMMMMMMMM/``.....NMh``....:sNMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM """)
print ("")
print (Fore.BLUE + '         (C) HiQ/Keltsu 2019                                        ----- HIQ RoboCon Quiz 2D  (v. 1.1) -----                                   http://www.hiqfinland.fi/')
print (Style.RESET_ALL)


def ask_value(question):
    allowed_values = ['1', '2', '3']
    while True:
        try:
            value_from_user = str(input(question + " "))
            if value_from_user in allowed_values:
                break
        except:
            print(" A.I>    Not an applicable answer. Give a numerical value between 1-3 ")
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
    value = ask_value(" A.I>    Your answer to this question is ? (1, 2, or 3) ")
    ANSWER = str(value)
    return ANSWER


def task1():
    print (Fore.BLUE + ' Task - Enter HiQ homepage ')
    print ("")
    print (Fore.BLUE + ' Robot step is: Given user goes to HIQ frontpage (step 1)')
    print (Style.RESET_ALL)
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
    print (Fore.BLUE + ' Task - Open avoimet tyopaikat page ')
    print ("")
    print (" Robot step is: When user opens avoimet tyopaikat page (step 2) ")
    print ("")
    print (Style.RESET_ALL)
    print (Fore.WHITE + 'Question: ')
    print (" Select a correct way to write robot for a click event? ")
    print ("")
    print ("")
    print (" 1 - Click element  css=.hiqfi-navigation__main ul li:nth-child(4) ")
    print (" 2 - Click element  css_.hiqfi-navigation__main ul li:nth-child(4) ")
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
    print (Fore.BLUE + ' Task - Select test automation developer career from available positions ')
    print ("")
    print (" Robot step is: And user selects test automation developer position (step 3) ")
    print ("")
    print (Style.RESET_ALL)
    print (Fore.WHITE + 'Question: ')
    print (" There is some CSS in the code along with some variables! Which line is written correctly? ")
    print ("")
    print ("")
    print (
        " 1 - Click element  ${AVAILABLE_JOBS_CONTAINER}  ${AUTOMATION_DEVELOPER_CAREER_'1'}  ${AVAILABLE_JOBS_CONTAINER}  ${AVAILABLE_JOBS_SECTION}  xiv:nth-child(X)  ${POSITION_TITLE} ")
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
    print (Fore.BLUE + ' Task - View and scroll selected career information ')
    print ("")
    print (" Robot step is: Then user can see information on automation developer career in HiQ (step 4) ")
    print ("")
    print (Style.RESET_ALL)
    print (" Question: ")
    print (
        " Let's use robot framework for a fancy web page scrolling. Which one of the given FOR loops can actually do the scroll? ")
    print ("")
    print ("")
    print (" ---SUPER !!---  A.I wants to provide a hint for this problem: Wrong selections are missing characters. Look carefully!")
    for i in range(3):
        print ("")
    print (Fore.WHITE + 'Question: ')
    print (" 1 -         ---Scroll effect 1--- ")
    print ("    @{all_rows} =  Get Webelements  ${NUMBER_OF_ROWS} ")
    print ("       :FOR  ${row}  IN  @{all_rows} ")
    print ("       \  Scroll element into view  ${row} ")
    print ("       \  Sleep  1 ")
    print ("       \  Close popup if appears ")
    for i in range(3):
        print ("")
    print ("  2 -       ---Scroll effect 2--- ")
    print ("    @{all_rows} =  Get Webelements  {NUMBER_OF_ROWS} ")
    print ("       :FOR  ${row}  IN  {all_rows} ")
    print ("       \  Scroll element into view  ${row} ")
    print ("       \  Sleep  1 ")
    print ("       \  Close popup if appears ")
    for i in range(3):
        print ("")
    print ("  3 -       ---Scroll effect 3--- ")
    print ("    @{all_rows} =  Get Webelements  ${NUMBER_OF_ROWS} ")
    print ("       FO  ${row}  IN  @{all_rows} ")
    print ("       \  Scroll element into view  ${row} ")
    print ("       \  Sleep  1 ")
    print ("       \  Close popup if appears ")
    print ("")
    print (Style.RESET_ALL)
    print (" ---- ")
    ANSWER = answer()
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
print (Fore.WHITE + ' ROBOT>  GAME INFO')
print (Style.RESET_ALL)
print (" A.I>    This is a program which gives you options to fill out missing ")
print ("         commands from a robot test with the options you choose.")
print ("         Then robot tries to run the tests using the given values. ")
print ("")
time.sleep(1)
print ("         You will be asked four questions. ")
print ("")
print (Fore.WHITE + ' ROBOT>  Try to be as fast as you can!')
print (Style.RESET_ALL)
time.sleep(1)
PLAYER = raw_input(' A.I>    Enter your name: ')
print ""
time.sleep(1)
raw_input(Fore.WHITE + ' ROBOT>  Pressing [ENTER] will start the timer. ')
print ""
print (Style.RESET_ALL)
print ""
print ""
time.sleep(1)
print (Fore.WHITE + ' ROBOT>  Timer starts NOW! ')
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
print (Fore.WHITE + ' ROBOT>  Timer -STOP- ')
print (Style.RESET_ALL)
TOTAL =float("{0:.2f}".format(stop - start))
print ("")
time.sleep(1)
delay_printloading (" .....")
print (Style.RESET_ALL)
for i in range(2):
    print ("")
time.sleep(1)
print (" A.I>    Let's try your robot code now in action !")
print ("")
delay_printloading (" STARTING ROBOT FRAMEWORK")
print (Style.RESET_ALL)
print ("")