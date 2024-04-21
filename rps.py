import random
import time

print('hello..! ');

def rps():
  while True:
           user = input('please choose one. (rock = r, paper = p, scissors = s): ')

           comp = random.choice(['r', 'p', 's'])
           
            
           if user == comp:
              print('i also chose: ' + comp);
              time.sleep(1)
              print('draw');
           elif user == 'r' and comp == 'p' :
             print('i chose: ' + comp);
             time.sleep(1)
             print('you lost!');
           elif user == 'p' and comp == 'r':
             print('i chose: ' + comp);
             time.sleep(1)
             print('you won..!');
           elif user == 'p' and comp == 's':
             print('i chose: ' + comp);
             time.sleep(1)
             print('you lost..!');
           elif user == 's' and comp == 'r':
              print('i chose: ' + comp);
              time.sleep(1)
              print('you lost..!');
           elif user == 's' and comp == 'p':
               print('i chose ' + comp);
               time.sleep(1)
               print('you won..!');
           elif user == 'r' and comp == 's':
               print('i chose ' + comp);
               time.sleep(1)
               print('you won..!');
           else :
             print("invalid choice!");
            
           answer = input("Press enter to play (q to quit).")
             
           if answer == "q":   
             break
    
  
    
rps()