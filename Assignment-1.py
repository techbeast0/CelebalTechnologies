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

def full_pyramid(n):

    for i in range(1, n + 1):

        for j in range(n - i):
            
            print(" ", end="")
        
        for k in range(1, 2*i):
           
            print("*", end="")
        
        print(" ")



if __name__ == "__main__":
     
     n  = int(input("Enter the value of n (must be integer)"))
     
     lowerTriangle(n)

     print('\n\n')

     upperTriangle(n)

     print('\n\n')

     full_pyramid(n)



