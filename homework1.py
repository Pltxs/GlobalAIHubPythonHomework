# #Beginner approach:
value1= input("Write what you want: ")
value2= input("Write what you want: ")
value3= input("Write what you want: ")
value4= input("Write what you want: ")
value5= input("Write what you want: ")
print(f"value1: {value1}\nvalue2: {value2}\nvalue3: {value3}\nvalue4: {value4}\nvalue5: {value5}")
print("1.value: ",type(value1))
print("2.value: ",type(value2))
print("3.value: ",type(value3))
print("4.value: ",type(value4))
print("5.value: ",type(value5))

# Another approach:
# values=[]
# y=1
# for i in range(0,5):
#     value=input("Write what you want: ")
#     values.append(value)
# print("value1: {0}\nvalue2: {1}\nvalue3: {2}\nvalue4: {3}\nvalue5: {4}"
#     .format(values[0],values[1],values[2],values[3],values[4]))
# for i in values:
#     print("{0}.value: {1}".format(y,type(i)))
#     y+=1