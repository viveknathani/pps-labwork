data={'java programming':0,
       'data structures':0,
       'oop':0,
       'operating systems':0,
       'networking':0
}

sum=0
# each subject carries a maximum of 50 marks
for subject, subject_marks in data.items():
    print("Enter marks obatined in ", subject, end=" ")
    subject_marks=float(input(" : "))
    sum+=subject_marks
    data[subject]=subject_marks

percent=(sum*0.4)
print("This is your data set : ", data)
print("This is your total : ", sum)
print("This is your percentage : ", percent, "%")


if(percent<35):
    print("You have failed.")
else:
    print("You have passed")
