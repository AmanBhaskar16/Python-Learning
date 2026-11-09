# Check Voting Eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# Check Exam Eligibility

attendance = int(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))

if attendance >= 75 and marks >= 40:
    print("You passed eligibility criteria")
else:
    print("You did not meet eligibility criteria")