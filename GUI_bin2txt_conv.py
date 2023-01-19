from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.btn_Flip = None
        self.btn_Convert = None
        self.convert_direction = None
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        frm_txtField_Frame1 = Frame(self)  # , bg = 'blue'
        frm_txtField_Frame1.grid(row=0, column=0,  ipadx=5, ipady=5, sticky=NW)
        frm_txtField_Frame2 = Frame(self)  # , bg = 'blue'
        frm_txtField_Frame2.grid(row=1, column=0, ipadx=5, ipady=5, sticky=NW)
        frm_RadioButtons_Frame = Frame(self)  # , bg = 'red'
        frm_RadioButtons_Frame.grid(row=0, column=1, ipadx=5, ipady=5, sticky=NW)
        frm_Buttons_Frame = Frame(self)  # , bg = 'green'
        frm_Buttons_Frame.grid(row=1, column=1, ipadx=5, ipady=5, sticky=NW)
        
        self.txt_enterField_1 = Text(frm_txtField_Frame1, width=60, height=10)  # ,width = 100, height = 100
        self.txt_enterField_1.grid(row=1, column=0, padx=2, pady=10, sticky=NE)
        self.txt_enterField_2 = Text(frm_txtField_Frame2, width=60, height=10)  # ,width = 100, height = 100
        self.txt_enterField_2.grid(row=2, column=0, padx=2, pady=10, sticky=NE)

        # # utwórz ramkę, która okala pola tekstowe i je grupuje
        # labelframe = LabelFrame(frm_RadioButtons_Frame, text='Conversion type')
        # labelframe.grid(row=0, column=1, padx=5, pady=2, sticky=NW)
       
       
        # utwórz ramkę, która okala przyciski wyboru i je grupuje
        labelframe = LabelFrame(frm_RadioButtons_Frame, text='Conversion type')
        labelframe.grid(row=0, column=1, padx=5, pady=2, sticky=NW)

        # utwórz zmienną, która ma reprezentowac typ konversji
        self.convert_direction = StringVar()
        self.convert_direction.set('bin2txt')

        # utwórz przycisk wyboru (radio button)
        Radiobutton(labelframe, text='bin to txt', variable=self.convert_direction, value='bin2txt', command=None).grid(row=0, column=0, padx=2, pady=2, sticky=W)
        Radiobutton(labelframe, text='txt to bin', variable=self.convert_direction, value='txt2bin', command=None).grid(row=1, column=0, padx=2, pady=2, sticky=W)

        # utwórz przycisk do otwierania i wyboru katalgów
        self.btn_Convert = Button(frm_Buttons_Frame)
        self.btn_Convert['text'] = 'Convert'
        self.btn_Convert['command'] = self.convert
        self.btn_Convert.grid(row=0, column=0, padx=5, pady=5, sticky=SW)
        self.btn_Flip = Button(frm_Buttons_Frame)
        self.btn_Flip['text'] = 'Flip'
        self.btn_Flip['command'] = self.flip
        self.btn_Flip.grid(row=1, column=0, padx=5, pady=10, sticky=SW)
        
        # scrollbar = Scrollbar(orient='vertical', command=self.txt_ListOfFiles.yview)
        # scrollbar.grid(row=1, column=2, sticky='NS')
        # self.txt_enterField.config(yscrollcommand=scrollbar.set)
        
    def convert(self):
        pass
    
    def flip(self):
        pass
        
        
root = Tk()
root.title('bin2txt Converter')
root.geometry('610x380')
app = Application(root)
root.mainloop()