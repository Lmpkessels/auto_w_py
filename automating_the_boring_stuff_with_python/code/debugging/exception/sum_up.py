def sum_up(x, y):
    if not isinstance(x, int): 
        raise Exception("'x' must be of type int")    
    if not isinstance(y, int):
        raise Exception("'y' must be of type int")
    
    print(f"{x} + {y} = {x + y}")

# Use try with except to raise an err when the try is invalid
try:
    sum_up(10,2)
    sum_up('1',2)
    sum_up(2,'1')
except Exception as err:
    print("An exception happened: " + str(err))