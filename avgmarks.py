marks=[int(x) for x in input().split()][:5]
total_marks=sum(marks)

average_marks=total_marks/len(marks)
print(f"Average marks: {average_marks:.2f}")