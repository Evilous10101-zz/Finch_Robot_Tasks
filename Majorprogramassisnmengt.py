#Michael Lannon

from finch import Finch
from time import sleep
from Finch_project_dance import dance1,dance2,dance3
from Finch_project_loggig import show_log
file = open('finchlog.txt', 'a+')
logging = open('finchlog.txt', 'r')
log = logging.readlines()
myFinch = Finch()
a = 220
#keeping this here just in case
bflat = 233
hbflat=466
asharp = bflat

fsharp=370
gflat=fsharp

b = 247
c = 262
d = 294
e = 330
f = 349
g = 392
ha=int(2*a)     #this is an 'a' note one octave above the other
hb=int(2*b)     #this is a 'b' note one octave above the other, etc....
hc=int(2*c)
hd=int(2*d)
he=int(2*e)
hf=int(2*f)
hg=int(2*g)
hbflat=int(2*bflat)
hfsharp=(2*fsharp)

bpm = 80                        #this sets the tempo
# myFinch.buzzer_with_delay(eighth,f) eighth = how long, f = note
whole = 4*60/bpm                 #in 4/4 time a whole note is four beats
dothalf = 1.5*2*60/bpm          #in 4/4 time a dotted half note is three beats
half = 2*60/bpm                 #in 4/4 time a half note is two beats
dotquarter = 1.5*60/bpm         #dotted quarter is on and a half beats
quarter = 60/bpm                #quarter note is one beat
dot8th=1.5*60/bpm/2              #dotted eight is three quarters of a beat
eighth = 60/bpm/2                #eight note is one half of a beat (two notes per beat)
sixteenth=60/bpm/4              #sixteenth note is four notes per beat.
def ask_user_a():
    #check with user for light show with error checking
    print('----------------------------------------------')
    print('1= color show 1')
    print('2= color show 2')
    print('3= color show 3')
    print('----------------------------------------------')
    aa=input('which LED light show do you want>')
    # Made code in this file since calling the function gave the api an error
    aaa=int(aa)
    if aaa == 1:
        myFinch.led(0, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(255, 0, 0)
        sleep(1)
        myFinch.led(255, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(255, 255, 0)
        sleep(1)
        myFinch.led(0, 0, 255)
        sleep(1)
        myFinch.led(0, 255, 0)
        sleep(1)
        myFinch.led(0, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(255, 0, 0)
        sleep(1)
        myFinch.led(255, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(0, 255, 0)
        sleep(1)
        myFinch.led(0, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
    if aaa == 2:
        myFinch.led(255, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(255, 255, 0)
        sleep(1)
        myFinch.led(255, 0, 0)
        sleep(1)
        myFinch.led(0, 0, 255)
        sleep(1)
        myFinch.led(0, 255, 0)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(0, 255, 0)
        sleep(1)
        myFinch.led(0, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(255, 0, 0)
        sleep(1)
        myFinch.led(0, 0, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(0, 255, 0)
        sleep(1)
        myFinch.led(0, 255, 255)
        sleep(1)
        myFinch.led(255, 255, 255)
    if aaa == 3:
        myFinch.led(255, 0, 255)
        myFinch.led(0, 255, 255)
        sleep(1)
        myFinch.led(255, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 0)
        sleep(1)
        myFinch.led(255, 255, 0)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(0, 255, 0)
        sleep(1)
        myFinch.led(0, 0, 255)
        sleep(1)
        myFinch.led(0, 255, 0)
        sleep(1)
        myFinch.led(0, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(255, 0, 0)
        sleep(1)
        myFinch.led(255, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
        sleep(1)
        myFinch.led(0, 0, 255)
        sleep(1)
        myFinch.led(0, 255, 255)
        sleep(1)
        myFinch.led(255, 0, 255)
    if 4 <= aaa <= 30000000000:
        print("Oops!  That was not a valid number.  Try again...")
        return ask_user_a()
    if -10000 <= aaa <= 0:
        print("Oops!  That was not a valid number.  Try again...")
        return ask_user_a()
    return aa
        
def ask_user_b():
    #ask user for song with error checking
    print('----------------------------------------------')
    print('1= song 1')
    print('2= song 2')
    print('3= song 3')
    print('----------------------------------------------')
    bb=input('what song do you want the finch to sing>')
    bbb=int(bb)
    #Made code in this file since calling the function gave the api an error
    if bbb == 1:
        for i in range(2):
            myFinch.buzzer_with_delay(eighth, g)
            myFinch.buzzer_with_delay(quarter, hg)
            myFinch.buzzer_with_delay(half, e)
            myFinch.buzzer_with_delay(quarter, c)
            myFinch.buzzer_with_delay(eighth, b)
            myFinch.buzzer_with_delay(sixteenth, c)
            myFinch.buzzer_with_delay(quarter, b)
            myFinch.buzzer_with_delay(eighth, c)
            myFinch.buzzer_with_delay(whole, e)
            myFinch.buzzer_with_delay(quarter, b)
            myFinch.buzzer_with_delay(eighth, g)
            myFinch.buzzer_with_delay(dothalf, hg)
            myFinch.buzzer_with_delay(quarter, g)
            myFinch.buzzer_with_delay(half, e)
            myFinch.buzzer_with_delay(whole, c)
    if bbb == 2:
        for i in range(2):
            myFinch.buzzer_with_delay(eighth, g)
            myFinch.buzzer_with_delay(quarter, d)
            myFinch.buzzer_with_delay(half, e)
            myFinch.buzzer_with_delay(quarter, d)
            myFinch.buzzer_with_delay(eighth, b)
            myFinch.buzzer_with_delay(quarter, c)
            myFinch.buzzer_with_delay(quarter, b)
            myFinch.buzzer_with_delay(eighth, d)
            myFinch.buzzer_with_delay(whole, e)
            myFinch.buzzer_with_delay(quarter, d)
            myFinch.buzzer_with_delay(eighth, g)
            myFinch.buzzer_with_delay(dothalf, hg)
            myFinch.buzzer_with_delay(half, g)
            myFinch.buzzer_with_delay(half, d)
            myFinch.buzzer_with_delay(half, c)
    if bbb == 3:
        for i in range(2):
            myFinch.buzzer_with_delay(quarter, f)
            myFinch.buzzer_with_delay(quarter, hg)
            myFinch.buzzer_with_delay(half, e)
            myFinch.buzzer_with_delay(quarter, c)
            myFinch.buzzer_with_delay(eighth, c)
            myFinch.buzzer_with_delay(half, c)
            myFinch.buzzer_with_delay(quarter, b)
            myFinch.buzzer_with_delay(half, c)
            myFinch.buzzer_with_delay(whole, e)
            myFinch.buzzer_with_delay(quarter, b)
            myFinch.buzzer_with_delay(eighth, c)
            myFinch.buzzer_with_delay(dothalf, hg)
            myFinch.buzzer_with_delay(eighth, c)
            myFinch.buzzer_with_delay(eighth, c)
            myFinch.buzzer_with_delay(eighth, c)
    if 4 <= bbb <= 30000000000:
        print("Oops!  That was not a valid number.  Try again...")
        return ask_user_b()
    if -10000 <= bbb <= 0:
        print("Oops!  That was not a valid number.  Try again...")
        return ask_user_b()
    return bb
def ask_user_c():
    #asks user for dance they want with errorchecking
    print('----------------------------------------------')
    print('1= Dance 1')
    print('2= Dance 2')
    print('3= Dance 3')
    print('----------------------------------------------')
    cc=input('what dance do you want the finch to do?>')
    ccc=int(cc)
    if ccc == 1:
        dance1()
    if ccc == 2:
        dance2()
    if ccc == 3:
        dance3()
        #Errorchecking
    if 4 <= ccc <= 30000000000:
        print("Oops!  That was not a valid number.  Try again...")
        return ask_user_c()
    if -10000 <= ccc <= 0:
        print("Oops!  That was not a valid number.  Try again...")
        return ask_user_c()
    return cc
def ask_user_all():
    #Main
    N=0
    Y=0
    aaaa=ask_user_a()
    sleep(1)
    bbbb=ask_user_b()
    sleep(1)
    cccc=ask_user_c()
    sleep(1)
    print('I hope you liked my song, dance and light show')
    file.write(' the user choose: ')
    file.write(aaaa)
    file.write(bbbb)
    file.write(cccc)
    file.write('\n')
    print('This is the log for all inputs of this program')
    show_log()
    errorcheck=input('do you want to go again? please put in Y for yes or N for no. please use capital letters>')
    #testting=int(errorcheck)
    if errorcheck == Y:
        return ask_user_all()
    if errorcheck == N:
            #Suppost to print all lines in log fine but doesn't work
        print('thank you for using this program. I hope you enjoyed it')


ask_user_all()