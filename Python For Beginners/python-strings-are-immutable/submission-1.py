def remove_fourth_character(word: str) -> str:
    return word[:4] + word[5:]


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
