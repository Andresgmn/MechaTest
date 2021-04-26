from tkinter import *
import Archivo as leer
from time import time
import operaciones as op
import evaluaString as evaluar

def main():
    
    class Application(Frame):
        def __init__(self, master = None):
            super().__init__(master)
            self.master = master
            self.grid()
            master.columnconfigure(0, weight = 1)
            master.rowconfigure(0, weight = 1)
            master.configure(background = '#2E2E2E')
            self.Inicio()
            master.title("MechaTest")
    

        def Inicio(self):
            
            self.IniciarVariables()
            
            #Parametros para iniciar el cuadro de texot
            self.textPanel = Text(self, height = 7, width = 69, bd = 5, wrap = WORD)
            self.textPanel.insert(END, self.lista, 'color')
            #self.textPanel.insert(END, "test", 'color')
            self.textPanel.config(font=("Serif", 20, "italic"), foreground = 'black',background = '#ffe5b4')
            self.textPanel.grid(row = 0, column = 0, columnspan = 4)
            
            
            self.textPanel.tag_add(self.auxList[0], self.testInicio, self.testFinal)
            self.textPanel.tag_config(self.auxList[0], background = "#FFCA66")

            #Panel para el scoreboardPPM
            self.scorePPMLabel = Label(self, height = 7, width = 30, bd = 1)
            self.scorePPMLabel.grid(row = 1, column = 0, sticky = W)
                      
            #Panel para las palabras correctas
            self.scoreWordsLabel = Label(self, height = 7, width = 30, bd = 1)
            self.scoreWordsLabel.grid(row = 1, column = 1, sticky = W)
            
            #Panel para las palabras incorrectas
            self.scoreErrorLabel = Label(self, height = 7, width = 30, bd = 1)
            self.scoreErrorLabel.grid(row = 1, column = 2, sticky = W)
            
            #Panel para las keystrokes
            self.scoreKeyStrokesLabel = Label(self, height = 7, width = 30, bd = 1)
            self.scoreKeyStrokesLabel.grid(row = 1, column = 3, sticky = E)
            
            #Widget de entrada de texto
            self.textEntry = Entry(self, textvariable = self.mi_variable, width = 15)
            self.textEntry.config(font = ("Serif", 30, "italic"))
            self.textEntry.grid(row = 2, column = 0, columnspan = 5, pady = 15)
            self.textEntry.focus_set()
            
            #Boton de reset
            self.resetButton = Button(self, height = 3, width = 5)
            self.resetButton.config(font = ("Serif", 12, "italic"))
            self.resetButton['text'] = "Reset"
            self.resetButton["command"] = self.reset
            self.resetButton.grid(row = 4, column = 3, sticky = E)
            
            #Boton de salir
            self.endButton = Button(self, height = 3, width = 5)
            self.endButton.config(font = ("Serif", 12, "italic"))
            self.endButton['text'] = "Salir"
            self.endButton["command"] = self.master.destroy
            self.endButton.grid(row = 4, column = 0, sticky = W)
        
                
        #Variables globales para operaciones de PPM y carga de textos    
        def IniciarVariables(self):
            self.lista = []
            self.lista = leer.LeerArchivo()
            print(self.lista)
            
            self.auxList = self.lista.copy()
            self.variableInicio = 0
            self.primerKeyStroke = 0
            self.getCoordinates = 0
            self.testInicio = "1.0"
            self.testFinal = "1" + "." + str(len(self.auxList[0]))
            
            self.mi_variable = StringVar()
            self.mi_variable.trace_add('write', self.my_callback)
            
            self.rightC = 0
            self.rightWords = 0
            self.wrongWords = 0
            
            self.endTime = 0
            self.listaDobles = evaluar.generaDobles()
            print(self.listaDobles)
            
            self.totalCaracteres = op.calcTLetras(self.lista)
            print(self.totalCaracteres)
            
        def my_callback(self, var, indx, mode):
            self.pattern = self.mi_variable.get()
            #self.setScore()           
            #verifica que la lista sea diferente a null

            bandCheckList = self.checkList()
            if bandCheckList:
                
                self.primerKeyStroke += 1
                if self.primerKeyStroke == 1:
                    self.StartTimer()

                
                if self.auxList[0].startswith(self.pattern):
                    print("doing nice")
                    self.textPanel.tag_add(self.pattern, self.testInicio, self.testFinal)
                    self.textPanel.tag_config(self.pattern, foreground = "green")
        
                else:
                    self.textPanel.tag_add(self.pattern, self.testInicio, self.testFinal)
                    self.textPanel.tag_config(self.pattern, foreground = "red")

                print(self.pattern)
                #print(self.timeIni)

                if " " in self.pattern:
                    self.CompareKeyStrokes()
                    self.textPanel.tag_add(self.auxList[0], self.testInicio, self.testFinal)
                    self.textPanel.tag_config(self.auxList[0], background = "#FFCA66")

            else:
                print("Done...")
        
            self.setScore()

        def StartTimer(self):
            self.timeIni = time()

        def CompareKeyStrokes(self):
            if self.auxList[0] == self.pattern[:-1]:
                print("Bien escrito")
                self.textPanel.tag_add(self.pattern, self.testInicio, self.testFinal)
                self.textPanel.tag_config(self.pattern, foreground = "green", background = '#ffe5b4')
                
                self.rightC += evaluar.evaluaPalabra(self.auxList[0], self.listaDobles) + 1
                print(self.rightC)

                self.rightWords += 1
            else:
                self.textPanel.tag_add(self.pattern, self.testInicio, self.testFinal)
                self.textPanel.tag_config(self.pattern, foreground = "red", background = '#ffe5b4')
                self.wrongWords += 1
            
            self.mi_variable.set('')
            self.Avanza()


        def setScore(self):
            if len(self.auxList) == 1 and "." in self.pattern:
                self.timeEnd = time()
                self.endTime = self.timeEnd - self.timeIni
                print("El tiempo de termino de escritura fue de >> ", end = " ")
                print(round(self.endTime,2))
                print("ultima frase y termino :]")
                print(self.auxList[0])

                if self.auxList[0] == self.pattern:
                    print("Bien escrito")
                    self.textPanel.tag_add(self.pattern, self.testInicio, END)
                    self.textPanel.tag_config(self.pattern, foreground = "green", background = '#ffe5b4')
                    self.rightWords += 1

                    self.rightC += evaluar.evaluaPalabra(self.auxList[0], self.listaDobles)
                    print(self.rightC)

                else:
                    self.textPanel.tag_add(self.pattern, self.testInicio, END)
                    self.textPanel.tag_config(self.pattern, foreground = "red")
                    self.wrongWords += 1
                    print(self.rightC)
                print("Palabras correctas", self.rightWords)
                print("Palabras incorrectas", self.wrongWords)
                self.scoreWordsLabel['text'] = "Correct Words: \n",str(self.rightWords)
                self.scoreErrorLabel['text'] = "Wrong words: \n",str(self.wrongWords)
                
                ppm = op.calculaPPM(self.rightC, self.endTime)
                self.scorePPMLabel['text'] = 'PPM ', ppm
                self.scoreKeyStrokesLabel['text'] = 'Caracteres Correctos ', self.rightC, "\nCaracteres Totales", self.totalCaracteres

        def Avanza(self):
            self.getCoordinates += len(self.auxList[0]) + 1

            del self.auxList[0]

            if self.auxList:
                self.testInicio = "1" + "." + str(self.getCoordinates)
                self.auxiliar = len(self.auxList[0]) + 1
                calc = (self.getCoordinates) + self.auxiliar
                self.testFinal = "1" + "." + str(calc - 1)
                self.primerSpace = True
            else:
                print("List empty... Done...") 

        def checkList(self):
            if self.auxList:
                return True
            else:
                return False

        def reset(self):
            self.IniciarVariables()
            self.Inicio()
            self.textPanel.delete("1.0",END)
            self.textPanel.insert(END, self.lista, 'color')
            self.textEntry.focus_set()
            self.textPanel.tag_add(self.auxList[0], self.testInicio, self.testFinal)
            self.textPanel.tag_config(self.auxList[0], background = "#FFCA66")
            
    """
    Inicio de toda la instancia general
    """

    root = Tk()
    app = Application(master = root)
    app.mainloop()

if __name__ == '__main__':
    main()
    
