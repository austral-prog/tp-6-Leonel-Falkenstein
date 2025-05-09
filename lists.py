def remove_elements(list_to_remove_elements): 
    x=len(list_to_remove_elements)
    if 6 <= x:
        del list_to_remove_elements[5]
    if 5<= x:
        del list_to_remove_elements[4]
    if 1<= x:
        del list_to_remove_elements[0]
    return list_to_remove_elements

def add_elements(listorti):
    listorti.append("Yellow")
    listorti.insert(0,"Pink")
    return listorti

def is_empty(listorta):
    return 0==len(listorta)

def check_lists(listortiano, listortin):
    if len(listortiano)>=3 and len(listortin) >=3:
        return listortiano[2] == listortin[2]
    else:
        return False
    
def list_of_lists (superlista):
    lista=[]
    if len(superlista)>=1:
        lista.append(superlista[0][0:2])
    if len(superlista)>=2:
        lista.append(superlista[1][1:4])
    if len(superlista)>=3:
        lista.append(superlista[2][-2:])
    return lista
