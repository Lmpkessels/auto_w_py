import random

# Generate a list that contains 'H' or 'T' 100 times, then look for a
# streak of 6 * 'H' OR 6 * 'T' increment number_of_streaks and calculate
# the presentage
def coin_flip_streaks():
    EXPERIMENT_RANGE = 10000
    BUFF = 100
    STREAK = 6

    number_of_streaks = 0

    for experiment_num in range(EXPERIMENT_RANGE):
        list_w_flips = []
        count_h = 0
        count_t = 0
        for i in range(BUFF):
            list_w_flips.append(random.choice(['H', 'T']))

        for flip in list_w_flips:
            if flip == 'H':
                count_h += 1
                count_t = 0
            else:
                count_t += 1
                count_h = 0

            if count_h >= STREAK or count_t >= STREAK:
                number_of_streaks += 1
                break           

    print("Chance of streak: %s%%" % (number_of_streaks / 100))

coin_flip_streaks()
