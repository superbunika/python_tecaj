# declare
my_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# clean data
my_string = my_string.replace(".", "")
my_string = my_string.replace(",", "")
my_string = my_string.lower()

# string to list to set
my_set = set(my_string.split(" "))
print(len(my_set))

# new test comment
my_list = my_string.split(" ")
out_list = []
for word in my_list:
    is_distinct = True
    for dist_word in out_list:
        if word == dist_word: is_distinct = False
    if is_distinct: out_list.append(word)

print(len(out_list))



"""
for word in my_string:
    if not word in my_dict:
        my_dict[word] = 1
    else:
        my_dict[word] += 1

print(len(my_dict))
"""