import argparse
import os
import tkinter as tk

parser = argparse.ArgumentParser()
parser.add_argument("--storage", type=str, default="archive.zip")
parser.add_argument("--prompt", type=str, default="vfs:> ")
parser.add_argument("--script", type=str, default="")
args = parser.parse_args()

print(f"Запущено с параметрами: {args.storage}, {args.prompt}, {args.script}")


def process_command(cmd_text=None):
    raw_input = cmd_text if cmd_text is not None else command_entry.get()
    if cmd_text is None:
        command_entry.delete(0, tk.END)

    if not raw_input.strip():
        return

    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, f"{args.prompt}{raw_input.strip()}\n")

    parts = raw_input.split()
    command = parts[0] if parts else ""
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


def execute_start_script():
    if not args.script:
        return
    if not os.path.exists(args.script):
        print(f"Ошибка: скрипт {args.script} не найден!")
        return

    with open(args.script, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line and not clean_line.startswith("#"):
                process_command(clean_line)


root = tk.Tk()
root.title("vfs_emulator")
root.geometry("600x480")

output_text = tk.Text(root, height=15, font=("Arial", 13), state=tk.NORMAL)
output_text.pack(expand=True, fill="both", padx=10, pady=5)
output_text.config(state=tk.DISABLED)

input_frame = tk.Frame(root)
input_frame.pack(fill="x", padx=10, pady=10)

prompt_label = tk.Label(input_frame, text=args.prompt, font=("Arial", 13))
prompt_label.pack(side="left")

command_entry = tk.Entry(input_frame, font=("Arial", 13))
command_entry.pack(side="left", fill="x", expand=True)
command_entry.bind("<Return>", lambda e: process_command())
command_entry.focus_set()

root.after(100, execute_start_script)
root.mainloop()
