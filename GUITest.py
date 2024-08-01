import customtkinter
import changeDir
import downloadFunc


def updateOptionMenu(choice):
    global labelwithtype
    labelwithtype.configure(text=f"Selected type: {choice}")
    print(choice)


def updateDirNameHeader():
    global labelwithdir
    changeDir.changeDownloadDir()
    labelwithdir.configure(text="Folder Opened: "+changeDir.directory)

def downloadFile(link):
    global labelwithdir
    filetype = labelwithdir.cget("text")
    if filetype == "Audio":
        downloadFunc.downloadAudio(link)
    elif filetype == "Video":
        downloadFunc.downloadVideo(link)
    else:
        downloadFunc.downloadAudio(link)


def main():
        global labelwithtype
        global labelwithdir

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")

        root = customtkinter.CTk()
        root.geometry("500x220")
        root.resizable(False, False)
        # root.wm_iconbitmap(r'D:\Pictures\youtubeBLUEFINAL.ico')
        root.wm_title("Youtube Downloader")

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill='both', expand=True)
        
        entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="YouTube Video Link:", width=360)
        entry1.place(y=12,x=10)
        
        labelwithdir = customtkinter.CTkLabel(master=frame, text="Selected Directory:")
        labelwithdir.place(y=45,x=155)
        
        buttonsearch = customtkinter.CTkButton(master=frame, text="Select!", command=updateDirNameHeader)
        buttonsearch.place(x=10, y=45)
        
        dropdown = customtkinter.CTkOptionMenu(master=frame, values= ['Audio', 'Video'], width=140, command=updateOptionMenu)
        dropdown.place(x=10, y=80)
                                                #Trying to get text type from values list.. not needed
        labelwithtype = customtkinter.CTkLabel(master=frame, text=f"Selected Type: ")
        labelwithtype.place(y=80,x=155)
        
        
        button = customtkinter.CTkButton(master=frame, text="Download!", command=lambda: downloadFile(entry1.get()), hover_color="#0932b0", width= 300)
        button.place(x=40, y=140)
        
        root.mainloop()


if __name__ == "__main__":
    main()    
    
