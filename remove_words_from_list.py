# Write a python function to remove a given word from a list ad strip it at the same time.
def remove_strip(word_list,remove_word):
    return [word.strip() for word in word_list if word.strip() != remove_word]

word_list=["APPLE", "BANANA","CHERRY"]
word_to_remove="APPLE"
print(remove_strip(word_list,word_to_remove))