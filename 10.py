questions = [
             "Capital of India ?", 
             "How many States in India ?",
             "India's Largest city by population ?",
             "What is the India's national aquatic animal ?",
             "First Prime Minister of India ?",
             ]
options =[
        ["A. Delhi",                 "B. New Delhi", 
         "C. Chennai",               "D.Banglore"],
        ["A. 28",                   "B. 27", 
         "C. 29",                   "D.30"],
        ["A. Chennai",        "B. Banglore", 
         "C. Delhi",          "D. Mumbai"],
        ["A. Crocodile",           "B. Green Frog",
         "C. River Dolphin",       "D. Katla fish"],
        ["A. Jawaharlal Nehru",    "B. Sirimavo Bandaranaike", 
         "C. Shri Rajiv Gandhi",   "D. Indira Gandhi"],
        ]

answers = ["b", "c", "d", "c", "a"]

keys = zip(questions, options, answers)

score = 0
for ques, opts, ans in keys:
    print("")
    print(ques)
    for opt in opts:
        print("\t" + opt)
    print("")

    choice = input("Enter choice: ")

    if(choice.lower() == ans):
        score+=1


print("Score: ", score)
