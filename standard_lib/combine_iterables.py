grades = [1, 2, 3, 4, 5]
phrases = ["very good", "good", "okay", "at least not failed", "failed"]

combined = list(zip(grades, phrases))
print(combined)

for grade, phrase in combined:
    print(grade, phrase)
