import threading
import tkinter as tk
from tkinter import filedialog
from main import run_outreach

root = tk.Tk()
root.title("msp-outreach-automator")
root.geometry("1000x500")
root.config(background="black")

csv_file = tk.StringVar(value="targets.csv")

nmessage_file_path = tk.StringVar(value="nmessage.txt")
smessage_file_path = tk.StringVar(value="smessage.txt")

nresume_file_path = tk.StringVar(value="nresume.pdf")
sresume_file_path = tk.StringVar(value="sresume.pdf")

def select_csv_file():
    path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
    )
    if path:
        csv_file.set(path)

def select_Nmessage_file():
    path = filedialog.askopenfilename(
        title="Select Nmessage File",
        filetypes=(("TXT Files", "*.txt"), ("All Files", "*.*")),
    )
    if path:
        nmessage_file_path.set(path)

def select_Smessage_file():
    path = filedialog.askopenfilename(
        title="Select Smessage File",
        filetypes=(("TXT Files", "*.txt"), ("All Files", "*.*")),
    )
    if path:
        smessage_file_path.set(path)

def select_Nresume_file():
    path = filedialog.askopenfilename(
        title="Select Nresume File",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")),
    )
    if path:
        nresume_file_path.set(path)

def select_Sresume_file():
    path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")),
    )
    if path:
        sresume_file_path.set(path)
    print(csv_file)

def run_engine():
    def task():
        run_outreach(
            n_msg_path=nmessage_file_path.get(),
            s_msg_path=smessage_file_path.get(),
            recipients_path=csv_file.get(),
            n_resume_path=nresume_file_path.get(),
            s_resume_path=sresume_file_path.get(),
            dry_run=False,
        )
    threading.Thread(target=task, daemon=True).start()

frame = tk.Frame(root)
frame.grid(row=0, column=0)

select_csv_file_btn = tk.Button(
    frame, text="select CSV file!", command=select_csv_file
)
select_csv_file_btn.grid(row=0, column=0)

select_nmessage_file_btn = tk.Button(
    frame, text="select Nmessage file!", command=select_Nmessage_file
)
select_nmessage_file_btn.grid(row=1, column=0)

select_smessage_file_btn = tk.Button(
    frame, text="select Smessage file!", command=select_Smessage_file
)
select_smessage_file_btn.grid(row=2, column=0)

select_nresume_file_btn = tk.Button(
    frame, text="select Nresume file!", command=select_Nresume_file
)
select_nresume_file_btn.grid(row=3, column=0)

select_sresume_file_btn = tk.Button(
    frame, text="select Sresume file!", command=select_Sresume_file
)
select_sresume_file_btn.grid(row=4, column=0)

send_btn = tk.Button(frame, text="send!", command=run_engine)
send_btn.grid(row=5, column=0)

root.mainloop()