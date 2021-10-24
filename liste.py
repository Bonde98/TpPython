from statistics import mean
#Liste de transaction
transaction_list = [250,12,45,32,23,25,250,12]
#1: La somme des transaction 
print("1)La somme des transactions est :",sum(transaction_list))
#2: Afficher la 5e transaction
print("2)La 5e transaction est:",transaction_list[4])
#3: Ordonner la liste
print("3)Voici la liste ordonner :",sorted(transaction_list))
print(sorted(transaction_list,reverse=True))
#4: Transformer la liste en tuple
nbr_tuple = tuple(transaction_list)
print("4)La liste en tuple :",nbr_tuple)
#5: Afficher la transaction la plus petite
print("5)La  transaction la plus ptite est :",min(transaction_list))
#6: Afficher la dernière transaction
print("6)La dernière transaction est :",transaction_list[7])
#7: supprimer les transaction dupliquer
transaction_list =  [250,12,45,32,23,25,250,12]
list_deplique = set(transaction_list)
print("7)Après la suppression des transaction dupliquer ",list_deplique)
#8: Supprimer la dernière transaction
transaction_list.pop(7)
print("8) Après la suppression du dernière transaction ",transaction_list)
#9: créer une copie des transactions
transaction_list 
copie_trans = transaction_list.copy()
print("9) la copie des transaction est :",copie_trans)
#10: Ecris un programme qui fait la moyens des transactions

result = mean(transaction_list)
print("10) La moyenne des transactions est :{}".format(result))
