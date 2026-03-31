"""
Curving scores
Write a function, print_scores(), that takes in a list of test scores and a number representing how many points to add.
"""


def print_scores(score, add):
    for i in range(len(score)):
        print(f"{score[i]} would be updated to", end=" ")
        score[i] += add
        print(score[i])
        
print_scores([67, 68, 72, 71, 69], 10)
print() # Print newline
print_scores([67, 68, 72, 71, 69], 5)