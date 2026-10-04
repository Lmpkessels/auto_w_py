def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Error trough symbol")
    
    if width <= 2:
        raise Exception("Error trough width")
    
    if height <= 2:
        raise Exception("Error trough height")
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 1)) + symbol)
    print(symbol * width)

try:
    box_print('*', 3, 10)
    box_print('-', 100, 4)
    box_print("=", 3, 10)
    box_print("Z", 0, 0)
except Exception as err:
    print("An exception happened: " + str(err))