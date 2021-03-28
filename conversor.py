import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import *

#Starting tk
root = tk.Tk()
root.title('MP4 to MP3 Converter')

#Setting canvas
canvas = tk.Canvas(root, width = 300, height = 250, bg = 'snow', relief = 'raised')
canvas.pack()

#Setting label
label1 = tk.Label(root, text = 'MP4 to MP3 Converter', bg = 'snow')
label1.config(font=('Arial', 20))
canvas.create_window(150, 60, window=label1)

#Function to get the file
def getFile():

    global video
    file_path = filedialog.askopenfilename()
    video = VideoFileClip(file_path)

#Setting get file button
getfilebutton = tk.Button(root, text = 'Select file', command = getFile, bg = 'seashell3', fg = 'black', font = ('Arial', 12, 'bold'))
canvas.create_window(150, 130, window = getfilebutton)

#Function to save the converted file
def saveFile():
    save_file_path = filedialog.asksaveasfilename(defaultextension = '.mp3')
    video.audio.write_audiofile(save_file_path)

#Setting save button
savebutton = tk.Button(root, text = 'Convert file', command = saveFile, bg = 'seashell3', fg = 'black', font = ('Arial', 12, 'bold'))
canvas.create_window(150, 180, window = savebutton)

#Function when closing the app
def closeApp():
    if messagebox.askokcancel('Quit', 'Do you wanto to close the app?'):
        root.destroy()


root.protocol('WM_DELETE_WINDOW', closeApp)
root.mainloop()

