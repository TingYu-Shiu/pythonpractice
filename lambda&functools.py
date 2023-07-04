my_list = [1,2,3,4,5,6,7,8,9,10]
odd_list =list(filter(lambda x:(x%2==1), my_list))
print(odd_list)


my_list = [5, 10 ,15, 20, 25, 30]
sqrt_list = list(map(lambda x: x**2, my_list))
print(sqrt_list)



from functools import reduce
my_list = [5, 8, 10, 20, 50, 100] 
reduce_result = reduce(lambda x,y: x+y, my_list)
print(reduce_result) #(((((5+8)+10)+20)+50)+100)