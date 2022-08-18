a = ["asd", "bbd", "ddfa", "mcsa"]


#list = list(map(lambda x: len(a[x]), range(0, len(a))))

print(list(map(lambda x:len(str(x)),a)))

print (list(map(lambda x: len(a[x]), range(0, len(a)))))

#print(list1)

print(list(map(len, a)))

