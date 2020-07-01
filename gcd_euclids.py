'''
Uses Euclids algorithm to find the G.C.D of two numbers 
''' 

def gcd(a,b):
    while(b!=0):
        t,a = a,b #store the value of a in a temporary variable and store b in a
        b = t%b  #assign the remainder of a/b to b
    
    return a;

print(gcd(20,8))