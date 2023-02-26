import helpers
import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING


class CenterWidgetMixin:   #clase para centrar la ventana
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")


class CreateClientWindow(Toplevel, CenterWidgetMixin):    #clase para crear la ventana de crear cliente
    def __init__(self, parent):  #constructor de la clase
        super().__init__(parent) 
        self.title("Crear cliente") 
        self.build()  #el metodo build crea la ventana
        self.center()  #centra la ventana
        self.transient(parent)  #hace que la ventana sea hija de la ventana principal
        self.grab_set()   #hace que la ventana sea modal, no se puede interactuar con la ventana principal hasta que no se cierre esta ventana

    def build(self):    #metodo para crear la ventana
        frame = Frame(self)    #crea un frame
        frame.pack(padx=20, pady=10)   #añade el frame a la ventana

        Label(frame, text="DNI (2 ints y 1 upper char)").grid(row=0, column=0)    #crea un label de dni y lo añade al frame
        Label(frame, text="Nombre (de 2 a 30 chars)").grid(row=0, column=1)   #crea un label de nombre y lo añade al frame
        Label(frame, text="Apellido (de 2 a 30 chars)").grid(row=0, column=2)   #crea un label de apellido y lo añade al frame

        dni = Entry(frame)   #crea un entry para el dni y lo añade al frame
        dni.grid(row=1, column=0)    #añade el entry al frame
        dni.bind("<KeyRelease>", lambda event: self.validate(event, 0))   #cuando se suelta una tecla, se llama al metodo validate
        nombre = Entry(frame)    #crea un entry para el nombre y lo añade al frame
        nombre.grid(row=1, column=1)    #añade el entry al frame
        nombre.bind("<KeyRelease>", lambda event: self.validate(event, 1))  #cuando se suelta una tecla, se llama al metodo validate
        apellido = Entry(frame)   #crea un entry para el apellido y lo añade al frame
        apellido.grid(row=1, column=2)   #añade el entry al frame
        apellido.bind("<KeyRelease>", lambda event: self.validate(event, 2))   #cuando se suelta una tecla, se llama al metodo validate

        frame = Frame(self)  #crea un frame
        frame.pack(pady=10)   #añade el frame a la ventana

        crear = Button(frame, text="Crear", command=self.create_client)    #crea un boton de crear y lo añade al frame
        crear.configure(state=DISABLED)    #desactiva el boton
        crear.grid(row=0, column=0)    #añade el boton al frame
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)    #crea un boton de cancelar y lo añade al frame

        self.validaciones = [0, 0, 0]   #lista de validaciones, que sirve para saber si los datos introducidos son validos
        self.crear = crear    #crea un atributo de la clase
        self.dni = dni    #crea un atributo de la clase con el dni
        self.nombre = nombre   #crea un atributo de la clase con el nombre
        self.apellido = apellido  #crea un atributo de la clase con el apellido

    def create_client(self):   #metodo para crear el cliente
        self.master.treeview.insert(    #inserta el cliente en el treeview, que es la tabla de la ventana principal
            parent='', index='end', iid=self.dni.get(),    #el id del cliente es el dni, que es unico, el parent es vacio porque es el primer nivel de la tabla, y el index es el final
            values=(self.dni.get(), self.nombre.get(), self.apellido.get()))     #los valores son el dni, el nombre y el apellido
        db.Clientes.crear(self.dni.get(), self.nombre.get(), self.apellido.get())   #crea el cliente en la base de datos
        self.close()   #cierra la ventana

    def close(self):   #metodo para cerrar la ventana
        self.destroy()  #destruye la ventana
        self.update()  #actualiza la ventana

    def validate(self, event, index):    #metodo para validar los datos introducidos
        valor = event.widget.get()    #obtiene el valor del entry, que es el dni, el nombre o el apellido
        valido = helpers.dni_valido(valor, db.Clientes.lista) if index == 0 \
            else (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)  #si el index es 0, llama al metodo dni_valido, que comprueba que el dni es valido, y si no, comprueba que el nombre o el apellido son validos
        event.widget.configure({"bg": "Green" if valido else "Red"})  #cambia el color del entry en base a si es valido o no
        # Cambiar el estado del botón en base a las validaciones
        self.validaciones[index] = valido   #guarda en la lista de validaciones si el dni, el nombre o el apellido son validos
        self.crear.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)   #si todos los datos son validos, activa el boton de crear, si no, lo desactiva


class EditClientWindow(Toplevel, CenterWidgetMixin):   #clase para la ventana de editar cliente
    def __init__(self, parent):   #constructor
        super().__init__(parent)
        self.title("Actualizar cliente")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):   #metodo para crear la ventana
        frame = Frame(self)   
        frame.pack(padx=20, pady=10)

        Label(frame, text="DNI (no editable)").grid(row=0, column=0)
        Label(frame, text="Nombre (de 2 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="Apellido (de 2 a 30 chars)").grid(row=0, column=2)

        dni = Entry(frame)
        dni.grid(row=1, column=0)
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        apellido = Entry(frame)
        apellido.grid(row=1, column=2)
        apellido.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        cliente = self.master.treeview.focus()    #obtiene el cliente seleccionado en la tabla de la ventana principal
        campos = self.master.treeview.item(cliente, 'values')   #obtiene los valores del cliente seleccionado, es decir, el dni, el nombre y el apellido
        dni.insert(0, campos[0])   #inserta el dni en el entry del dni
        dni.config(state=DISABLED)   #desactiva el entry del dni
        nombre.insert(0, campos[1])   #inserta el nombre en el entry del nombre
        apellido.insert(0, campos[2])  #inserta el apellido en el entry del apellido

        frame = Frame(self)
        frame.pack(pady=10)

        actualizar = Button(frame, text="Actualizar", command=self.edit_client)   #crea un boton de actualizar, command es el metodo que se ejecuta al pulsar el boton
        actualizar.grid(row=0, column=0)  #añade el boton al frame
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)  #crea un boton de cancelar y lo añade al frame

        self.validaciones = [1, 1]   #lista de validaciones, que sirve para saber si los datos introducidos son validos
        self.actualizar = actualizar    #crea un atributo de la clase
        self.dni = dni   
        self.nombre = nombre  
        self.apellido = apellido

    def edit_client(self):
        cliente = self.master.treeview.focus()   #obtiene el cliente seleccionado en la tabla de la ventana principal
        self.master.treeview.item(cliente, values=(    #actualiza los valores del cliente seleccionado en la tabla de la ventana principal
            self.dni.get(), self.nombre.get(), self.apellido.get()))     #Con los valores del dni, el nombre y el apellido
        db.Clientes.modificar(self.dni.get(), self.nombre.get(), self.apellido.get())    #actualiza los valores del cliente en la base de datos
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get()
        valido = (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)  #comprueba que el nombre o el apellido son validos
        event.widget.configure({"bg": "Green" if valido else "Red"})
        # Cambiar el estado del botón en base a las validaciones
        self.validaciones[index] = valido   #guarda en la lista de validaciones si el nombre o el apellido son validos
        self.actualizar.config(state=NORMAL if self.validaciones == [1, 1] else DISABLED)    #si todos los datos son validos, activa el boton de actualizar, si no, lo desactiva

class SearchClientWindow(Toplevel, CenterWidgetMixin):     #clase para la ventana de buscar cliente
    def __init__(self, parent):   #constructor
        super().__init__(parent)
        self.title("Buscar cliente")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()
    
    def build(self):   #metodo para crear la ventana
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text="Buscar por:").grid(row=0, column=0)
        Label(frame, text="Valor:").grid(row=0, column=1)

        self.search_by = StringVar()   #crea una variable de tipo StringVar que sirve para guardar el valor del combobox, que es el valor por el que se va a buscar
        self.search_by.set("DNI")   #establece el valor por defecto del combobox
        OptionMenu(frame, self.search_by, "DNI", "Nombre", "Apellido").grid(row=1, column=0)         #crea un combobox con las opciones de buscar por dni, nombre o apellido

        self.valor = Entry(frame)   #crea un entry para introducir el valor por el que se va a buscar
        self.valor.grid(row=1, column=1)    #añade el entry al frame
        self.valor.bind("<Return>", self.validate)          #añade un evento al entry para validar los datos introducidos al pulsar enter
        
        frame = Frame(self)
        frame.pack(pady=10)

        Button(frame, text="Buscar", command=self.search_client).grid(row=0, column=0)  #crea un boton de buscar, command es el metodo que se ejecuta al pulsar el boton
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        self.validaciones = [0]
        self.valor = self.valor

    def search_client(self):
        self.close()  #cierra la ventana
        self.destroy() #destruye la ventana
        self.update()  #actualiza la ventana
        self.parent.search_client(self.search_by.get(), self.valor.get())   #llama al metodo search_client de la ventana principal, pasandole como parametros el valor del combobox y el valor del entry, el parent es la ventana principal

    def close(self):
        self.destroy()
        self.update()
    
    def validate(self, event):
        valor = event.widget.get()
        valido = helpers.dni_valido(valor, db.Clientes.lista) if self.search_by.get() == "DNI" \
            else (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg": "Green" if valido else "Red"})
        # Cambiar el estado del botón en base a las validaciones
        self.validaciones[0] = valido
        self.valor.config(state=NORMAL if self.validaciones == [1] else DISABLED)




class MainWindow(Tk, CenterWidgetMixin):  #clase para la ventana principal
    def __init__(self):
        super().__init__()
        self.title("Gestor de clientes")
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('DNI', 'Nombre', 'Apellido')

        treeview.column("#0", width=0, stretch=NO)   #crea las columnas de la tabla
        #crea las columnas de dni, nombre y apellido
        treeview.column("DNI", anchor=CENTER)    
        treeview.column("Nombre", anchor=CENTER)
        treeview.column("Apellido", anchor=CENTER)

        #Los encabezados de las columnas
        treeview.heading("DNI", text="DNI", anchor=CENTER)   
        treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        treeview.heading("Apellido", text="Apellido", anchor=CENTER)

        #Como treeview no tiene scrollbar, se crea uno y se le asigna al treeview
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        treeview['yscrollcommand'] = scrollbar.set

        #Añade los clientes a la tabla
        for cliente in db.Clientes.lista:
            treeview.insert(
                parent='', index='end', iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellido))  #con los valores de dni, nombre y apellido

        treeview.pack()  #añade el treeview al frame y el frame a la ventana

        frame = Frame(self)   #crea un frame para los botones
        frame.pack(pady=20)

        #crea los botones
        Button(frame, text="Crear", command=self.create).grid(row=0, column=0)   
        Button(frame, text="Modificar", command=self.edit).grid(row=0, column=1)
        Button(frame, text="Borrar", command=self.delete).grid(row=0, column=2)
        Button(frame, text="Buscar", command=self.search).grid(row=0, column=3)

        self.treeview = treeview
    
    def search(self):
        SearchClientWindow(self)

    def delete(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, "values")
            confirmar = askokcancel(    #crea una ventana de confirmacion, askokcancel devuelve True si se pulsa el boton de ok y False si se pulsa el boton de cancelar
                title="Confirmar borrado",
                message=f"¿Borrar {campos[1]} {campos[2]}?",
                icon=WARNING)
            if confirmar:
                self.treeview.delete(cliente)
                db.Clientes.borrar(campos[0])

    def create(self):
        CreateClientWindow(self)

    def edit(self):
        if self.treeview.focus():
            EditClientWindow(self)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()