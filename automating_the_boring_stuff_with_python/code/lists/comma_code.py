# comma code: receives a list as argument and creates a sentence from
# the values within the list
def comma_code(spam):
    n = len(spam)
    sentence = ""

    # Create the sentence
    for i in range(0, n):
        if spam[i] == spam[n-1]:
            sentence += f"and {spam[n-1]}"
        else:
            sentence += f"{spam[i]}, "

    print(sentence) 

spam = ['Apples', 'Bananas', 'Peers', 'Mangos']
comma_code(spam)
