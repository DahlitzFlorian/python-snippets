import cooked_input as ci


cap_cleaner = ci.CapitalizationCleaner(style=ci.ALL_WORDS_CAP_STYLE)
name = ci.get_string(prompt="What is your name?", cleaners=[cap_cleaner])

print(name)
