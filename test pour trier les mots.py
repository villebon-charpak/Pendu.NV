question = "haricot"
nlettres = len(question)
new_list = []
for i in range(0,len(liste)):
    if len(liste[i]) == nlettres:
        new_list.append(liste[i])
liste = new_list
new_list = []
    

step = {'e':[0,5], 'a':[2]} 
step['b']=[1] 
for i in range(0,len(liste)):  
    for j in range(0,len(liste[i])): 
        if liste[i][j] in step and j in step[liste[i][j]]: 
            new_list.append(liste[i])
            break
                
    