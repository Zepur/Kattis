N = int(input())

contest = []

for i in range(N):
    student = ''
    name, began, born, courses = input().split()
    student += name + ' '
    if int(began[:4]) >= 2010:
        student += 'eligible'
    elif int(born[:4]) >= 1991:
        student += 'eligible'
    elif int(courses) >= 41:
        student += 'ineligible'
    else:
        student += 'coach petitions'
    contest.append(student)

for s in contest:
    print(s)
