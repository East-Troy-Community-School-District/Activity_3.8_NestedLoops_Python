'''
Repeatable Repeat Phrase
Pawelski
10/28/2023
Introduction to Computer Science

Instructions:
Trace the program and predict what it
will display. Then run the program to
check your work. Finally, be prepared
to discuss the following questions...
1. Based on this example, is it possible
   to have a loop inside a while loop?
2. Based on this example, how would you
   make any program repeat while the user
   wants to repeat the program?
'''

repeat = "yes"
while repeat == "yes":
    phrase = input("Enter a phrase >> ")
    times = int(input("Times to repeat >> "))
    for i in range(0, times):
        print(phrase)
    repeat = input("Would you like to repeat? (yes/no) >> ")
    print()