string1 = input("Ingrese el primer string: ").upper().replace(" ", "")
string2 = input("Ingrese el segundo string: ").upper().replace(" ", "")
        

if len(string1) == len(string2):
    
    letras = []
    for i in string1:
        
        if i != " ":
        
            if i not in letras:
                
                if string2.count(i) == string1.count(i):
                    letras.append(i)
                
                else:
                    print("No son anagramas")
                    exit()
            
            letras.append(i)
            
        else:
            pass
    
    print("Son anagramas")
    exit()
    
else:
    print("No son anagramas")
    exit()