# Nota: CR = Chamadas Recursivas

# Exemplo 1
count=0
def SaySomething(word):
    global count

    if (len(word)>=5):
        return f"Saying {word} right now..."
    
    else:
        count+=1
        return SaySomething(word+'a')

print(f'Resultado: {SaySomething("a")}, CR: {count}\n')


# Exemplo 2
count=0
def IsEven(num):
    global count

    if (num%2!=0):
        return False
    
    elif (num==0):
        return True
    
    else:
        count+=1
        return IsEven(num-2)

print(f'Resultado: {IsEven(8)}, CR: {count}\n')


# Exemplo 3 (lista de exercícios)
count=0
def x(n):
    global count

    if (n>=0) and (n<=2):
        count+=1
        return n
    
    else:
        return x(n-1)+x(n-2)+x(n-3)

print(f'Resultado: {x(6)}, CR: {count}\n')