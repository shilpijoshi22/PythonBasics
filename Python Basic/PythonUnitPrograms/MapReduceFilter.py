from functools import reduce
nums=[5,10,6,33,8,999,52,4,2,1000,20,1]


#Filter. So filtering means selecting some data based onsome logic
evens= list(filter(lambda n:n%2==0,nums))
print(evens)

#Map. MAp means to apply some operation on each data present in the list
doubles= list(map(lambda n:n*2, evens))
print(doubles)


#Reduce. Now Reduce means to apply some operation on the whole sequence and make it one. For example adding all the data and you have one sum
result= reduce(lambda a,b:a+b,doubles)
print("Sum of all the numbers is :",result)