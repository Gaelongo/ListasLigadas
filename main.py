from Clases import LinkedList

def main():
    
    opc = 1
    lista_creada = 0
    while opc != '':
        print("1. Crear lista || 2. Imprimir lista || 3. append || 4. pop || 5. popFirst || 6. remove || 7. prepend || 8. get || 9. insert || 10. set")
        opc = input("Ingresa una opción: ")
        try:
            match opc:
                case '1':
                    valor = input("Primer elemento: ")
                    lista_creada = LinkedList(valor)
                    print("Se ha creado la lista")
                    print(lista_creada)
                    print("-------------")
                case '2':
                
                    print(lista_creada)
                    print("--------")
                    imprimirInfo(lista_creada)
        
                case '3':
                    valor = input("Ingrese el elemento: ")
                    lista_creada.append(valor)
                    print("Elemento agregado")
                    print("------------")
                case '4':
                    lista_creada.pop()
                    print("Lista popeada")
                    print("----------")
                case '5':
                    lista_creada.popFirst()
                    print("Primer elemento eliminado")
                    print("----------")
                case '6':
                    valor = input("Ingrese el elemento a eliminar: ")
                    lista_creada.remove(valor)
                    print("Elemento eliminado")
                    print("---------") 
                case '7':
                    valor = input("Ingrese el valor a ingresar: ")
                    lista_creada.prepend(valor)
                    print("Lista preprend")
                    print("------------")
                case '8':
                    indice = input("Ingresa el indice del valor: ")
                    nodo = lista_creada.get(int(indice))
                    print(nodo.value)
                    print("---------")
                case '9':
                    valor = input("Ingresa el valor a ingresar: ")
                    indice = input("Ingresa la posición en la cual ingresarlo: ")
                    lista_creada.insert(int(indice), valor)
                    print("Elemento agregado")
                    print("--------------")
                case '10':
                    indice = input("Ingrese el indice a reemplazar: ")
                    valor = input("Ingrese el valor: ")
                    lista_creada.set(int(indice), valor)
                    print("Elemento reemplazado")
                    print("-----------")
        except AttributeError:
            print("Es necesario crear una lista primero.")
        continue
            
    return
            

def imprimirInfo(lista_creada):
    
    print("Head: ", lista_creada.head.value)
    print("Tail: ", lista_creada.tail.value)
    print("Length:", lista_creada.length)
    print("-------------------")
    
    
main()