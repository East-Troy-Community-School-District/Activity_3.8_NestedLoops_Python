'''
Nested Loops 2
1/18/2023
Python I

Instructions:
Trace the program and predict what it
will display. Then run the program to
check your work. Finally, be prepared
to discuss the following questions...
1. Compare the previous program and this
   program. How does the output differ?
   Why do you think this happened?
2. How many times does the inner loop
   repeat for each pass of the outer loop?
'''

for i in range(0, 9, 3):
    for k in range(0, 6, 2):
        print(str(k) + "\t" + str(i))
