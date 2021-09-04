#The program print the no of times a character is in a sting.
#eg in the name Mariya Mennen n appears 3 times

name = "mariya mennen"
count = 0
for char in name:
    if char == 'n':
        count = count + 1
    else:
        continue
print (count)