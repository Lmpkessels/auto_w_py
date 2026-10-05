# Let spam trigger an error if less than 10
def test_if_spam_is_less_than_ten(spam):
    assert spam < 10

# Cause an assert if var eggs equals var bacon
def test_if_eggs_equals_bacon(eggs, bacon):
    assert eggs != bacon

# This function will cause assert at all times because the
# argument of par will equal at all times
def causes_assert_at_all_times(par):
    assert par != par


test_if_spam_is_less_than_ten(8)
test_if_eggs_equals_bacon("Eggs", "Bacon")

#test_if_spam_is_less_than_ten(11)
test_if_eggs_equals_bacon("Eggs", "Eggs")

#causes_assert_at_all_times(5)
#causes_assert_at_all_times("hello")