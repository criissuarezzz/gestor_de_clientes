import menu
import ui
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-t':    #si se ejecuta el test, se ejecuta el menu de test y no la interfaz. Sys.argv[1] es el primer argumento que se le pasa al programa y sys.argv es una lista con todos los argumentos
        menu.iniciar()
    else:
        app = ui.MainWindow()    #si no se ejecuta el test, se ejecuta la interfaz
        app.mainloop()
        