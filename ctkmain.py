import customtkinter

def main():

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")

        root = customtkinter.CTk()
        root.geometry("500x220")
        root.resizable(False, False)
        root.wm_iconbitmap(r'D:\Pictures\youtubeBLUEFINAL.ico')
        root.wm_title("Youtube Downloader")

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill='both', expand=True)
        
        root.mainloop()
        
main()