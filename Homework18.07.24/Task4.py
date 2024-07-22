import random
num_1 = [ i for i in range (95, 106)]
print ("a.", num_1)
#b.
even_num = [ j for j in range (10 , 21 , 2)]
print ("b.", even_num)
#c.
rnd_bool = [random.choice ([True, False]) for _ in range (5)]
print("c.", rnd_bool)
#d.
######NO IDEA####
#e.
rnd_num = [random.randint(1 , 100) for k in range (10)]
print ("e.", rnd_num)
#f.
big_num = [ l for l in rnd_num if l > 50]
print ("f.",big_num)
#g.
big_num2 = [ m for m in [random.randint (1 , 100) for _ in range (10)] if m > 50 ]
print ("g.",big_num2)
#h.
word_list = [ n for n in (input ("Enter a sentence: ")) if n != 't' and n != ' ']
print ("h.", word_list)
