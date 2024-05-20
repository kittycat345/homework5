immutable_var=(1,2,True,False,"python top",[1,2,"listikkkk"])# переменная содержит кортеж, состоящий из элементов  с разными типами данных. Изменить в данном кортеже можно только элементы списка, который является последним элементом кортежа.Остальные элементы менять нельзя, т.к кортеж принадлежит к неизменяемому типу данных.
print("immutable tuple: ",immutable_var)
immutable_var[5][2]="bumaga" #изменил список, который является элементом кортежа
# immutable_var[2][2]= False эта строка кода не будет работать, т.к кортеж является неизменяемым типом данных
print("immutable tuple mod: ",immutable_var)
mutable_list=["life",1,686,True,"False"]
mutable_list[0]=166
mutable_list[-1]=True
print("mutable list: ",mutable_list)
