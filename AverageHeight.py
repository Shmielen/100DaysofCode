# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
count = 0
sumof = 0
for i in student_heights:
    count += 1 

for height in student_heights:
    sumof += height

avg = sumof/count

print(round(avg))
#Write your code below this row 👇




