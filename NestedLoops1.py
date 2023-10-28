'''
Nested Loops 1
Pawelski
10/28/2023
Introduction to Computer Science

Instructions:
Trace the program and predict what it
will display. Then run the program to
check your work. Finally, be prepared
to discuss the following questions...
1. Why is it important to use two different
   loop control variables for the inner and
   outer loop?
2. In total, how many times does the inner
   loop repeat?
3. Does the outer loop control the left or
   right number? What about the inner loop?
'''

for i in range(0, 9, 3):
    for k in range(0, 6, 2):
        print(str(i) + "\t" + str(k))