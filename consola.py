from repositorio import Repositorio
class Main:
    def __init__(self):     
        self.repositorio=Repositorio()
    def menu(self):
            bandera=0
            print()
            while bandera == 0:
                try:
                    print()
                    print("1)Hacer un commit")
                    print("2)Crear nueva rama")
                    print("3)Cambiar de rama")
                    print("4)Historial de commit")
                    print("5)Juntar")
                    print("0)Salir")
                    opcion=int(input("git  "))
                    print()
                    if opcion==1:
                        print("Ingrese los archivos que va a guardar")
                        self.repositorio.hacer_un_commit(input("git add "))
                    elif opcion==2:
                        print("Ingrese el nombre de la rama que quiere crear")
                        self.repositorio.crear_rama(input("git branch "))
                    elif opcion==3:
                        print("Ingrese el nombre de la rama a la que quiere cambiar")
                        self.repositorio.cambiar_rama(input("git checkout "))
                    elif opcion==4:
                        print("Presione enter para ver el historial de commit de la rama")
                        input("git log")
                        self.repositorio.historial_commit()
                    elif opcion==5:
                        print("Ingrese el nombre de la rama que desea fusionar con su rama actual")
                        self.repositorio.unir(input("git merge "))
                    elif opcion==0:
                        print("Fin del proceso")
                        bandera=1
                except Exception as e:
                    print(f"error {e}")

main=Main()
main.menu()




    
