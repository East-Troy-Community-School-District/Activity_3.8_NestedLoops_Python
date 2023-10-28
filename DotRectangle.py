'''
Dot Rectangle
Pawelski
10/28/2023
Introduction to Computer Science

Instructions:
Trace the program and predict what it
will display. Then run the program to
check your work. Modify the program
so that is displays a rectangle of dots
that is 5 dots tall and 3 dots wide.
Finally, be prepared to discuss the
following questions...
1. What loop controls the number of rows?
2. What loop controls the number of columns?
3. What does end mean in line 24? What is the
   default value for end?
4. What is the purpose of line 25 in the program?
'''

for i in range(0, 3):
    for j in range(0, 5):
        print("* ", end="")
    print()