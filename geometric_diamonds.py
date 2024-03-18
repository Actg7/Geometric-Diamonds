#
# Code by: Athanasios Grivakis
# Prints a hollow diamond formed of numbers 1 through n
#
# ex diamonds(3)
#
#    1
#   2 2
#  3   3
#   2 2
#    1
#

def diamonds(n):
    num = n
    if (n < 1) or (n % 1 != 0):
        print("Please try again with a positive integer.")
        return
    elif n == 1:
        print(1)
    else:
        
        # Position the 1 correctly
        print((n - 1)*" "+str(1))
        
        # The rest of the numbers 2,...,n for diamond top half
        for i in range(2, num+1):
            
            # Amount of spaces from left screen border to first occurrence
            space_left = n - 2
            
            # Amount of spaces from first occurrence to second occurrence
            num_digits = 0
            temp = i
            while temp != 0:
                temp //= 10
                num_digits += 1
            adjust = i - (num_digits - 1) # positions numbers with mutiple digits correctly
            space_between = 2 * adjust - 3
            
            print(space_left*" "+str(i)+space_between*" "+str(i))
            n -= 1
            
    if num == 1:
        print(1)
    else:
        
        # Amount of spaces from left screen border to first occurrence
        space_left = 0
        
        for i in range(num, 1,-1):
            
            # Amount of spaces from first occurrence to second occurrence
            num_digits = 0
            temp = i
            while temp != 0:
                temp //= 10
                num_digits += 1
            adjust = i - (num_digits - 1) # positions numbers with mutiple digits correctly
            space_between = 2 * adjust - 3
            
            print(space_left*" "+str(i)+space_between*" "+str(i))
            space_left += 1
        print((num - 1)*" "+str(1))
    return
