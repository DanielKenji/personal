# Return odd positions in a list. 

def list_odd(lista):
    if type(lista) == list:
        return lista[0::2]
    else:
        print(lista, "is not a list")


        
