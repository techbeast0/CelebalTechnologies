#  Lower Triangular pattern

def lowerTriangle(n):

    for i in range(n):

        for j in range(i):

            print("*",end = "")

        print("") 

# Upper Triangle Pattern

def upperTriangle(n):
    
    for i in range(n, 0, -1):
        
        for j in range(n - i):
            
            print(" ", end="")
        
        for j in range(i):
                
                print("*", end="")
        
        print(" ")  

# Pyramid Pattern

def pyramid(n):

    for i in range(1, n + 1):

        for j in range(n - i):
            
            print(" ", end="")
        
        for k in range(1, 2*i):
           
            print("*", end="")
        
        print(" ")



if __name__ == "__main__":
     
     n  = int(input("Enter the value of n (must be integer)"))

     print("Lower Triangle:-\n")
     
     lowerTriangle(n)

     print('\n\n')

     print("Upper Triangle:-\n")

     upperTriangle(n)

     print('\n\n')

     print("Pyramid:-\n")

     pyramid(n)



# Sample Output

# Enter the value of n (must be integer)10


# Lower Triangle:-

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********     
 
# Upper Triangle:-


# ********** 
#  ********* 
#   ******** 
#    ******* 
#     ****** 
#      ***** 
#       **** 
#        *** 
#         ** 
#          * 


# Pyramid:-


#          * 
#         *** 
#        ***** 
#       ******* 
#      ********* 
#     *********** 
#    ************* 
#   *************** 
#  ***************** 
# ******************* 


