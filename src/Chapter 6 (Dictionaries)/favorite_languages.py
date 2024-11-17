# create dictionary storing the results of a poll
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'c#', 'javascript'],
    'phil': ['python', 'java', 'dart']
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

# for k, v in favorite_languages.items():
#     print(f"{k.title()}'s favorite programming language is {v.title()}.")

# for name in favorite_languages.keys():
#     # print(f"{name.title()}")
#     print(f"Hi {name.title()}!")
#     friends = ['phil', 'sarah']
#     if name in friends:
#         lang = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {lang}!")
#     if 'erin' not in favorite_languages.keys():
#         print("Erin, please take our poll!")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()} thank you for taking our poll!")

# print("The following languages have been mentioned:")
# # for lang in favorite_languages.values():
# #     print(f"{lang.title()}")

# for lang in set(favorite_languages.values()):
#     print(f"{lang.title()}")

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        if language == 'javascript':
            print("\tJavaScript")
        else:
            print(f"\t{language.title()}")
