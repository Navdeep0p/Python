
import time

print ("hello..! \n ");

print (' please enter,');

un = 'nani'
pas = 'nani'

uinput = input('Username: ')
pinput = input('Password: ')

if uinput == un and pinput == pas :

    print("loading...") 
    time.sleep(3)
    print("... \n")
    time.sleep(1)
    print("access granted..! \n");

    time.sleep(1)

    print("Welcome... \n");
    print("Path : P:\Personal\developing\python")
    
elif uinput != un and pinput == pas :
   
   print("invalid username!")

elif uinput == un and pinput != pas :
    print("invalid password!")

else : 
    print("invalid username and password!")    


