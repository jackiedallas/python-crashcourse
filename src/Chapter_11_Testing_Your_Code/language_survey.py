from survey import AnonymousSurvey

# Define a question and make a survey
question = "What languages do you speak? "
language_survey = AnonymousSurvey(question)

# show the question, and store responses to the question
language_survey.show_questions()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# show the results
print("\nThank you for taking the survey!")
language_survey.show_results()