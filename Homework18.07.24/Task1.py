task_1a: list = []
for number in range (80, 100):
    task_1a.append (number)
print ('a.',task_1a)

#b.
print ('b.',task_1a[0]);
#c.
print ('c.',task_1a[-1]);
#d.
print ('d.',len(task_1a))
#e.
print ('e.',task_1a[3:12])
#f.
print ('f.',task_1a [3:])
#g.
print('g.',task_1a [:9])
#h.
task_1a.insert (10 , 999)
print ("h. The new list:", task_1a)
#i.
print ('i.',task_1a[::-1])
#j.
odd_numbers: list = []
for number in task_1a:
    if number % 2 != 0 :
        odd_numbers.append(number)
print ('j.',odd_numbers)

