#Michael Lannon
logging = open('finchlog.txt', 'r+')
log = logging.readlines()
#This makes text to test the program
#logging.write('This is a test \n')
logging.close()
def show_log():
    for x in log:
        print(x,' ')

