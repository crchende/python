import sys; #for error handling - the errors for which we do not know the error type 

def func_fara_param():
    print("1) Executie functii fara parametrii")
    

def func_cu_param(x, y):
    print("\n2) Executie functie cu doi parametrii:")
    print("x = ", x)
    print("y = ", y)
    
    print("Incerc sa adun parametrii")
    sum = x + y
    
    print("x + y = sum = ", sum)


def func_cu_param_implicit(x, y, z=0):
    print("\n3) Executie functie cu parametu implicit:")
    print("x = ", x)
    print("y = ", y)
    print("z = ", z)
    
    print("x + y + z = ", x + y + z)


def func_cu_nr_var_param(x, y, *args):
    print("4) Executie functie cu numar variabil de parametrii:")
    print("x =    ", x)
    print("y =    ", y)
    print("args = ", args)
    print("Elemente in args:")
    for el in args:
        print(el)
        

def func_cu_nr_var_param_si_param_cheie_val(x, y, *args, **kvargs):
    print("\n5) Executie functie cu numar variabil de parametrii si parametrii 'cheie = valoare':")
    print("x =      ", x)
    print("y =      ", y)
    print("args =   ", args)
    print("kvargs = ", kvargs)

    print("Elemente in args:")
    for el in args:
        print(el)
        
    print("Elemente cheie - valoare (un dictionar):")
    for k in kvargs:
        print("k: ", k, "; val: ", kvargs[k])
        
    # Verificare - vreau sa vad ce se intampla cu vaiabilele args si kwargs in exterior
    # daca le modific in functie
    try:
        print("Incerc sa modific: args[0] = 5555")
        args[0] = 5555;
    except TypeError as e:
        print("!!! Eroare tentativa modificare tuplu:", str(e))
        print("!!! Chiar daca dau args ca o lista, in interior este convertita in tuplu")
        
    print("Modific: kvargs['a'] = 9999")
    kvargs['a'] = 9999



 
#source:   
#https://stackoverflow.com/questions/18176602/how-to-get-the-name-of-an-exception-that-was-caught-in-python
def get_full_class_name(obj):
    module = obj.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return obj.__class__.__name__
    return module + '.' + obj.__class__.__name__
    
#########
# Apel functii
#########

##########################
func_fara_param()

##########################
# daca parametrii sunt ambii string sau int putem apela functia ca mai jos:
func_cu_param("a", "b")
func_cu_param(1, 2)

##########################
func_cu_param_implicit(1,2)
func_cu_param_implicit(1,2,100)

###########################
# apel direct
func_cu_nr_var_param(1, 2, 100, 200, 300, 400)

# folosire variabila pentru args - observati apelul cu *typlu_arg
tuplu_arg = (5, 10, 15, 20)
#lst_arg = [5, 10, 15, 20];# putem folosi si o lista
func_cu_nr_var_param(1, 2, *tuplu_arg)

###########################
func_cu_nr_var_param_si_param_cheie_val(1, 2, 100, 200, 300, a = 1000, b = 2000)

#apel folosind variabile tuplu si dictionar
lst_arg = (5, 10, 15, 20); #merge si cu 
dict_arg = {'a': 1000, 'b': 2000}
func_cu_nr_var_param_si_param_cheie_val(1, 2, *lst_arg, **dict_arg)

print("De observat ca am modificat kvarg = **dict_arg in interiorul funtiei.")
print("dar la iesirea din functie nu se vede modificarea")
print(" -- analogie cu parametrii dati prin valoare din 'C', nu prin referinta --")
print("lst_arg:  ", lst_arg)
print("dict_arg: ", dict_arg)


#
# test git
#







