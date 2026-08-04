grade_book = {"Ava":75, "Ben":55, "Charlie":85, "Diana":95, "Ethan":65}

total = 0
for score in grade_book.values():
    total += score


average = total / len(grade_book)
print("Students average is", average)

highest_mark = max(grade_book.values())
print("Highest mark is", highest_mark)
highest_scorer = max(grade_book, key=grade_book.get)
print("Highest mark recieved by ", highest_scorer)

lowest_mark = min(grade_book.values())
print("Lowest mark is ", lowest_mark)
lowest_scorer = min(grade_book, key=grade_book.get)
print("Lowest mark recieved by ", lowest_scorer)

search = input("Enter a student's name to search for their score: ")

student_score = grade_book.get(search)
if student_score is not None:
    print(search, "received a score of", student_score)
else:
    print(search, "is not in the grade book.")
