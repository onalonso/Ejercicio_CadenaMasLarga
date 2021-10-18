
def cadena_larga(cadena):
    max = 0
    index = 0
    for i in range (len(cadena)):
        if max <= len(cadena[i]):
            max = len(cadena[i])
            index = i            
    return index


    return


if __name__=='__main__':  
    lista = ["aquellostr",'yo', 'tu', "el","nosotros","aquellostr_12345","ellos","vosotros","ustedes", "aquellos","esos"]          
    print("lista :", lista)
    print( "cadena mas larga :", lista[cadena_larga(lista)] )
    print( "índice de cadena mas larga :",  cadena_larga(lista))
    