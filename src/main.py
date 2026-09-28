import tkinter as tk

def process_command(event=None):
    raw_input = command_entry.get().strip()
    if not raw_input:
        return
    command_entry.delete(0, tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, f"vfs:> {raw_input}\n")
    
    parts = raw_input.split()
    command = parts[0] if parts else ""
    arguments = parts[1:]

    if command == "exit":
        root.destroy()
        return
    elif command in ["ls", "cd"]:
        output_text.insert(tk.END, f"[Заглушка] Вызвана команда: {command}, Аргументы: {arguments}\n\n")
    else:
        output_text.insert(tk.END, f"Ошибка: неизвестная команда '{command}'\n\n")
    
    output_text.config(state=tk.DISABLED)
    output_text.see(tk.END)

root = tk.Tk()
root.title("vfs_emulator")
root.geometry("600x450")
root.configure(bg="#1e1e1e")

output_text = tk.Text(root, bg="black", fg="#00ff00", font=("Courier", 12), state=tk.NORMAL)
output_text.pack(expand=True, fill="both", padx=10, pady=5)
output_text.insert(tk.END, "Эмулятор оболочки ОС запущен.\nДоступные команды: ls, cd, exit\n\n")
output_text.config(state=tk.DISABLED)

input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(fill="x", padx=10, pady=10)

prompt_label = tk.Label(input_frame, text="vfs:> ", bg="#1e1e1e", fg="#00ff00", font=("Courier", 12))
prompt_label.pack(side="left")

command_entry = tk.Entry(input_frame, bg="white", fg="black", font=("Courier", 12), insertbackground="black")
command_entry.pack(side="left", fill="x", expand=True)

command_entry.bind("<Return>", process_command)
command_entry.focus_set()

root.mainloop()
