
# Recursion practice using a countdown function

def countdown(num):
    if num ==0:
        print('Done')
        return
    else:
        print(num, '...')
        countdown(num-1)
        

countdown(5)