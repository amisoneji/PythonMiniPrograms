#Author :: AMISONEJI
#Sample Program for concatination of dictionary.

#Python script to concatenate following dictionaries to create a new one.

#sample dictinory
dic1= {1:10, 2:20}
dic2= {3:30, 4:40}
dic3= {5:50, 6:60}

dic1.update(dic2) #all items of dict2 update in dict1
dic1.update(dic3) #all items of dict3 update in dict1
print(dic1)

