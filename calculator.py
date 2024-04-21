from tkinter import N


print("hello world");
print('enter your name: ');
un = input()
print("hello, " + un );
print('how can i help you? ');
print("(m - multiplication, d - division, a - addition, s - subtraction.)");

rep = input()

if rep == 'm':
    print("please enter first number:");

    mx = input()
    print('please enter second number:');
    my = input()
    print('product of two numbers is: ')
    print(int(mx) * int(my))
elif rep == 'd':
     print("please enter first number:");

     dx = input()
     print('please enter second number:');
     dy = input()
     print('division of two numbers is: ')
     print(int(dx) / int(dy));
elif rep == 'a':
     print("please enter first number:");

     ax = input()
     print('please enter second number:');
     ay = input()
     print('sum of two numbers is: ')
     print(int(ax) + int(ay));
elif rep == 's':
     print("please enter first number:");

     sx = input()
     print('please enter second number:');
     sy = input()
     print('difference of two numbers is: ')
     print(int(sx) - int(sy));
else:
     print('invalid selection.');


