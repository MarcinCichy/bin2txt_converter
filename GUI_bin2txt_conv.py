from tkinter import *
from bin2txt_conv import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.btn_Flip = None
        self.btn_Convert = None
        self.convert_direction = None
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create variable to represents direction of conversion
        self.convert_direction = StringVar()
        self.convert_direction.set('bin2txt')

        frm_txtField_Frame1 = Frame(self)  # , bg = 'blue'
        frm_txtField_Frame1.grid(row=0, column=0, ipadx=5, ipady=5, sticky=N)
        frm_txtField_Frame2 = Frame(self)  # , bg = 'blue'
        frm_txtField_Frame2.grid(row=1, column=0, ipadx=5, ipady=5, sticky=N)
        frm_RadioButtons_Frame = Frame(self)  # , bg = 'red'
        frm_RadioButtons_Frame.grid(row=0, column=1, ipadx=5, ipady=5, sticky=N)
        frm_Buttons_Frame = Frame(self)  # , bg = 'green'
        frm_Buttons_Frame.grid(row=1, column=1, ipadx=5, ipady=5, sticky=N)

        # create frames that surround and group text boxes
        labelframe_first_txt = LabelFrame(frm_txtField_Frame1, text='Enter text:')
        labelframe_first_txt.grid(row=0, column=0, padx=5, pady=5, sticky=N)
        labelframe_second_txt = LabelFrame(frm_txtField_Frame2, text='Converted text:')
        labelframe_second_txt.grid(row=1, column=0, padx=5, pady=5, sticky=N)

        # create a frame that surrounds and groups the radio buttons
        labelframe_buttons = LabelFrame(frm_RadioButtons_Frame, text='Conversion type')
        labelframe_buttons.grid(row=0, column=1, padx=5, pady=2, sticky=NW)

        # create text boxes
        self.txt_enterField_1 = Text(labelframe_first_txt , width=60, height=10)  # ,width = 100, height = 100
        self.txt_enterField_1.grid(row=1, column=0, padx=10, pady=10, sticky=N)
        self.txt_enterField_2 = Text(labelframe_second_txt, width=60, height=10)  # ,width = 100, height = 100
        self.txt_enterField_2.grid(row=2, column=0, padx=10, pady=10, sticky=N)

        # create radio buttons
        Radiobutton(labelframe_buttons, text='bin to txt', variable=self.convert_direction, value='bin2txt', command=None).grid(row=0, column=0, padx=2, pady=2, sticky=W)
        Radiobutton(labelframe_buttons, text='txt to bin', variable=self.convert_direction, value='txt2bin', command=None).grid(row=1, column=0, padx=2, pady=2, sticky=W)

        # create buttons that support conversion
        self.btn_Convert = Button(frm_Buttons_Frame)
        self.btn_Convert['text'] = 'Convert'
        self.btn_Convert['command'] = self.convert
        self.btn_Convert.grid(row=0, column=0, padx=5, pady=5, sticky=SW)
        self.btn_Flip = Button(frm_Buttons_Frame)
        self.btn_Flip['text'] = 'Clear'
        self.btn_Flip['command'] = self.clear
        self.btn_Flip.grid(row=1, column=0, padx=5, pady=10, sticky=SW)

    def convert(self):
        convert_type = self.convert_direction.get()
        if convert_type == 'bin2txt':
            first_txt_field_content = self.txt_enterField_1.get("1.0", "end")
            conversion = bin2txt(first_txt_field_content.rstrip())
            self.txt_enterField_2.insert(END, conversion)
        else:
            first_txt_field_content = self.txt_enterField_1.get("1.0", "end")
            conversion = txt2bin(first_txt_field_content.rstrip())
            self.txt_enterField_2.insert(END, conversion)

    def clear(self, first_txt_field_content=None):
        self.txt_enterField_1.delete("1.0", "end")
        self.txt_enterField_2.delete("1.0", "end")


root = Tk()
root.title('txt2bin2txt Converter')
root.geometry('650x450')
root.resizable(False, False)
app = Application(root)
root.mainloop()