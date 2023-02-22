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

            Label(frame, text="DNI(2 números y una letra mayusc)").grid(row=0, column=0) #para poner un label
            Label(frame, text="Nombre").grid(row=0, column=1)
            Label(frame, text="Apellidos").grid(row=0, column=2)

            dni=Entry(frame)
            dni.grid(row=1, column=0)
            dni.bind("<KeyRelease>", lambda event: self.validate(event,0))
            nombre=Entry(frame)
            nombre.grid(row=1, column=1)
            nombre.bind("<KeyRelease>", lambda event: self.validate(event,1))
            apellido=Entry(frame)
            apellido.grid(row=1, column=2)
            apellido.bind("<KeyRelease>", lambda event: self.validate(event,2))

            frame=Frame(self)
            frame.pack(pady=10)

            crear=Button(frame, text="Crear", command=self.create_client)
            crear.configure(state=DISABLED)
            crear.grid(row=0, column=0)
            Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1) #para poner un boton

            self.validaciones=[0, 0, 0]
            self.crear=crear
            self.dni=dni
            self.nombre=nombre
            self.apellido=apellido

        def create_client(self):
            self.master.treeview.insert(
                parent='', index='end', iid=self.dni.get(),
                values=(self.dni.get(), self.nombre.get(), self.apellido.get()))
            db.Clientes.crear(self.dni.get(), self.nombre.get(), self.apellido.get())
            self.close()

        def close(self):
            self.destroy()
            self.update()
        
        def validate (self, event, index):
            valor=event.widget.get()
            valido=helpers.dni_valido(valor, db.Clientes.lista) if index == 0 else (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
            event.widget.configure({"bg": "Green" if valido else "Red"}) #para cambiar el color del fondo
            self.validaciones[index]=valido
            self.crear.config(state=NORMAL if self.validaciones == [1,1,1] else DISABLED)

    class EditClientWindow(Toplevel, CenterWidgetMixin):
        def __init__ (self, parent):
            super().__init__(parent)
            self.title('Actualizar cliente')
            self.build()
            self.center()
            self.transient(parent)
            self.grab_set()

            

if __name__ == '__main__':
    app=MainWindow()
    app.mainloop()
