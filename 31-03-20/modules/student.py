def division(percent):
    switch_case_replicate={}
    for i in range(0, 36):
        switch_case_replicate[i]='D'
    for i in range(36, 61):
        switch_case_replicate[i]='C'
    for i in range(61, 81):
        switch_case_replicate[i]='B'
    for i in range(81, 101):
        switch_case_replicate[i]='A'
    return switch_case_replicate[percent]

def start_calculation():
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
    print("Your division is :", division(percent))
