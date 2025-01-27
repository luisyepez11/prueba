from repositorio import Repositorio
class Main:
    def __init__(self):     
        self.repositorio=Repositorio()
    def menu(self):
            bandera=0
            while bandera == 0:
                try:
                    print("1)hacer un commit")
                    print("2)crear nueva rama")
                    print("3)cambiar de rama nueva rama")
                    print("4)Historial de commit")
                    print("5)juntar")
                    print("0)eliminar")
                    opcion=int(input("git  "))
                    print()
                    if opcion==1:
                        self.repositorio.hacer_un_commit(input("git add "))
                    elif opcion==2:
                        self.repositorio.crear_rama(input("git branch "))
                    elif opcion==3:
                        self.repositorio.cambiar_rama(input("git checkout "))
                    elif opcion==4:
                        input("git log")
                        self.repositorio.historial_commit()
                    elif opcion==5:
                        self.repositorio.unir(input("git merge "))
                    elif opcion==0:
                        bandera=1
                except Exception as e:
                    print(f"error {e}")

main=Main()
main.menu()




    
