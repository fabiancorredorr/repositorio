from main import Main

class MainTest:
    def test_debe_retortar_un_saludo(self):
        el_main = Main()
        if(el_main.saludar() == "Hola"):
            print("funciona")
        else:
            print("no funciona")

if __name__ == "__main__":
    MainTest().test_debe_retortar_un_saludo()
