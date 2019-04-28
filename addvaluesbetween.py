OC = """
def sumaValoresIntermedios(num1, num2): 
    total=0
    for i in range(num1, num2+1):
        total+=i
    return total
print(sumaValoresIntermedios(1,3)) 
"""
exec(LOC)
