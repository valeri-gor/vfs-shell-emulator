import tkinter as tk


def process_command(event=None):
    raw_input = command_entry.get().strip()
    if not raw_input:
        return
    command_entry.delete(0, tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, f"vfs:> {raw_input}\n")

    parts = raw_input.split()
    command = parts if parts else ""
    arguments = parts[1:]

    if command == "exit":
        root.destroy()
        return
    elif command in ["ls", "cd"]:
        stub_msg = (
            f"[Заглушка] Вызвана команда: {command}, "
            f"Аргументы: {arguments}\n\n"
        )
        output_text.insert(tk.END, stub_msg)
    else:
        err_msg = f"Ошибка: неизвестная команда '{command}'\n\n"
        output_text.insert(tk.END, err_msg)

    output_text.config(state=tk.DISABLED)
    output_text.see(tk.END)


root = tk.Tk()
root.title("vfs_emulator")
root.geometry("600x480")

# Стандартное белое поле для текста со стандартным шрифтом
output_text = tk.Text(root, height=15, font=("Arial", 13), state=tk.NORMAL)
output_text.pack(expand=True, fill="both", padx=10, pady=5)

welcome_msg = (
    "Эмулятор оболочки ОС запущен.\n"
    "Доступные команды: ls, cd, exit\n\n"
)
output_text.insert(tk.END, welcome_msg)
output_text.config(state=tk.DISABLED)

input_frame = tk.Frame(root)
input_frame.pack(fill="x", padx=10, pady=10)

# Обычный текст перед вводом
prompt_label = tk.Label(input_frame, text="vfs:> ", font=("Arial", 13))
prompt_label.pack(side="left")

# Обычное стандартное поле ввода
command_entry = tk.Entry(input_frame, font=("Arial", 13))
command_entry.pack(side="left", fill="x", expand=True)

command_entry.bind("<Return>", process_command)
command_entry.focus_set()

root.mainloop()
