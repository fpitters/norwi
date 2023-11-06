from googletrans import Translator


import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext

translator = Translator()

root = tk.Tk()
root.title('Norwi')
root.geometry('600x200')

style = ttk.Style()
style.theme_use('clam')

content = root.selection_get()
output = translator.translate(content, src='no', dest='en')

text_area = scrolledtext.ScrolledText(root)
text_area.grid(column = 0, pady = 10, padx = 10)
text_area.pack()
text_area.insert(tk.INSERT, output.text)
text_area.configure(state ='disabled')
#w = tk.Label(scrollable_frame, text=output.text, wraplength=500)
#w.pack()

root.mainloop()
