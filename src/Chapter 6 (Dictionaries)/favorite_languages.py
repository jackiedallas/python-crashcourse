# create dictionary storing the results of a poll
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

# put language values in variable using title method
# language_sarah = favorite_languages['sarah'].title()
# lang_jen = favorite_languages['jen'].title()
# lang_edward = favorite_languages['edward'].title()
# lang_phil = favorite_languages['phil'].title()

# print each person's favorite language
# print(f"Sarah's favorite programming language is {language_sarah}.")
# print(f"Jen's favorite programming language is {lang_jen}.")
# print(f"Edward's favorite programming language is {lang_edward}.")
# print(f"Phil's favorite programming language is {lang_phil}.")

for k, v in favorite_languages.items():
    print(f"{k.title()}'s favorite programming language is {v.title()}.")
