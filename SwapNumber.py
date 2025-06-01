# Problem Statement:
# Swap the numbers with and without the 3rd Variable.

# Questions:
# - How you will create and store the value in 3rd variable?
# - How you will do it without the 3rd Variable?

#------------------------------------------------------------------------------------------
#------ Date - 18 May, 2025, Written by - Shalini Singh ----------------------------------
#------------------------------------------------------------------------------------------


#  With 3rd variable
x, y = 11, 22
print (x,y)

z = x
x= y
y=z
print (x,y)

#  Without 3rd Variable
a,b=30,25
print(a,b)

a= a+b
b=a-b
a=a-b
print(a,b)

#---------------------------------- End of the program -----------------------------------------