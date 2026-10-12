kickboxing_class = {
    'Luuk': {'Unlimited': '61.00'},
    'Jan': {'Unlimited': '61.00'},
    'Peter': {'2x per week': '51.00'},
    'Frank': {'Unlimited': '61.00'},
    'Lucas': {'1x per week': '41.00'},
}

def sign_up(name, subscription, stored_class):
    if name not in stored_class:
        if subscription == 'Unlimited':
            stored_class[name] = {'Unlimited': '61.00'}

        if subscription == '2x per week':
            stored_class[name] = {'2x per week': '51.00'}
        
        if subscription == '1x per week':
            stored_class[name] = {'1x per week': '41.00'}
    else:
        print(f"{name} you already have a {subscription} subscription")

# Count total income, and difference in subscription
def count_subscription(kbx_class):
    unl_people = 0
    two_people = 0
    one_people = 0

    unlimited = 0
    two_times = 0
    one_time = 0

    for k, v in kbx_class.items():
        if v.get('Unlimited', 0):
            unl_people += 1
            unlimited += 61.00
        
        if v.get('2x per week', 0):
            two_people += 1
            two_times += 51.00

        if v.get('1x per week', 0):
            one_people += 1
            one_time += 41.00

    print(f"Amount of people with a unlimited subscription: {unl_people}")
    print(f"Amount of people with a 2x per week subscription: {two_people}")
    print(f"Amount of people with a 1x per week subscription: {one_people}")
    print(f"Total income is: € {unlimited + two_times + one_time}")
            

print("Provide your name: ")
name = input()
print("Choose a subscription (Unlimited, 2x per week, 1x per week)")
print(
    """
    Unlimited = €61,- per month\n
    2x per week = €51,- per month\n
    1x per week = €41,- per month

    Choose (Unlimited, 2x per week, 1x per week)
    """
)
choice_subscription = input()

sign_up(name, choice_subscription, kickboxing_class)
count_subscription(kickboxing_class)