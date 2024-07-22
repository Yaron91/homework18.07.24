import statistics
#a.
temp_list : list = []
#b.
while True:
    x: float = float (input("Please enter the temperature, enter -999 to stop: "));

    if x == -999:
        break
    if x >= -50 and x<= 50:
        temp_list.append(x)
    else:
        continue
print ("b.",temp_list)
#c.
temp_list.extend([18.5 ,39.1, -20.0])
print("c.", temp_list)
#d.
print (f"d. The hottest temperature is: {max (temp_list)}");
#e.
print (f"e. The coldest temperature is: {min (temp_list)}");
#f.
print (f"f. The average temperature is: {sum (temp_list) / len (temp_list) : .2f}");
#g.
print ("g. The average temperature using mean from statistics is:", statistics.mean(temp_list) )
#h.
del temp_list [0];
print ("h.", temp_list);
#i.
temp_list.remove(18.5);
print ("i.", temp_list);
#j.
temp_last: float = temp_list.pop()
print ("j. the last temperature on the list is:", temp_last);
#k.
copy_list: list = temp_list.copy()
copy_list.sort()
print (f"k. The list sorted", copy_list);
#l.
copy_2: list = copy_list.copy()
copy_2.reverse()
print ("l. The new list reversed", copy_2)
#m.
print ("m. The differenec between sort and sorted is that sort will modify the existing list while with sorted, the list will return sorted, but without modifying the list.")
#n.
print ('n. Reversed function returns back object called iterator which includes all the organs of a string/ list/ etc.. In order for to return as a list we will perform the following: ')
print ('copy_2 reversed', list(reversed(copy_2)))