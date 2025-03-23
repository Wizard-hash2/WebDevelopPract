my_list = []

listrep = [10,20,30,40]
for u in listrep:
    my_list.append(u)
my_list[1] = 15

my_secondlist = [50,60,70]

my_list.extend(my_secondlist)

del my_list[-1]

my_list.sort()
print("MyList after Sorting is", my_list)

count = 0
for x in my_list:
    if(x == 30):
        print("The index of the count is", count)
    count +=1

        



