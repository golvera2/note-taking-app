import tkinter as tk

class NoteApp:
    def __init__(self, master):
        self.master = master
        master.title("Note App")

        self.text = tk.Text(master)
        self.text.pack()

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_note)
        file_menu.add_command(label="Save", command=self.save_note)
        file_menu.add_command(label="Open", command=self.open_note)

    def new_note(self):
        self.text.delete("1.0", tk.END)

    def save_note(self):
        filepath = filedialog.asksaveasfilename()
        if filepath:
            with open(filepath, 'w') as f:
                text = self.text.get("1.0", 'end-1c')
                f.write(text)

    def open_note(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as f:
                text
