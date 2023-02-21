from tkinter import *

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestor de clientes')
        self.build()

    def build(self):
        button=Button(self.root, text='Hola mundo', command=self.hola_mundo)
        button.pack()
    
    def hola_mundo(self):
        print('Hola mundo')
    
if __name__ == '__main__':
    app=MainWindow()
    app.mainloop()
