import helpers
import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING


class CenterWidgetMixin:
    def center(self):
        self.update()#para que se actualice la ventana
        w=self.winfo_width()#para obtener el ancho de la ventana
        h=self.winfo_height()#para obtener el alto de la ventana
        ws=self.winfo_screenwidth()#para obtener el ancho de la pantalla
        hs=self.winfo_screenheight()#para obtener el alto de la pantalla
        x=int(ws/2-w/2)#para obtener la posicion x en el centro de la pantalla
        y=int(hs/2-h/2)#para obtener la posicion y en el centro de la pantalla
        self.geometry('{}x{}+{}+{}'.format(w,h,x,y))#para centrar la ventana

class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):   #parent es la ventana principal
        super().__init__(parent)   #para que herede de la ventana principal
        self.title('Crear cliente')  #para ponerle titulo a la ventana
        self.build()   #para construir la ventana
        self.center()  #para centrar la ventana
        self.transient(parent)  #para que no se pueda minimizar la ventana principal
        self.grab_set()  #para que no se pueda interactuar con la ventana principal

        def build(self):
            frame=Frame(self)
            frame.pack(padx=20, pady=10)  #para darle margen a la ventana

            

if __name__ == '__main__':
    app=MainWindow()
    app.mainloop()
