class Numero:

    def esPar(self, num):
        if( num%2 == 0 ):
	    return True 
        else:	
	    return False 

class NumeroTest:
    def Test_retorna_False_si_es_impar(self):
        numero=Numero()
        if(numero.esPar(3) == False):
	    print("Funciono")
	else:
            print("No Funciono")

    def Test_retorna_True_si_es_par(self):
        numero=Numero()
        if(numero.esPar(4) == True):
	    print("Funciono")
	else:
            print("No Funciono")

if __name__ == "__main__":
    NumeroTest().Test_retorna_False_si_es_impar()
    NumeroTest().Test_retorna_True_si_es_par()

