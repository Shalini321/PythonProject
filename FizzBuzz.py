# Python Activity 1
# Write a code in python in which you can get “Fizz Buzz” for all numbers 
# which can be divided by (3, 5, 15). The range should from (1 to 100).

# if number divided by 3 then say 'Fizz'
# if number divided by 5 then say 'Buzz'
# if number divided by 15 then say 'Fizz Buzz'

#------------------------------------------------------------------------------------------
#------ Date - 17 May, 2025, Written by - Shalini Singh ----------------------------------
#------------------------------------------------------------------------------------------

for i in range(100):
    if i % 3 ==0 and i % 15 != 0:
        print('Fizz')
    elif i % 5 == 0 and i % 15 != 0:
        print('Buzz')
    elif i % 5 == 0 and i % 15 == 0 :
        print('Fizz Buzz')
    else :
        print(i)

#---------------------------------- End of the program -----------------------------------------