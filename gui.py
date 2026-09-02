import threading
from tkinter import filedialog
import customtkinter as ctk
from main import run_outreach

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("MSP Outreach Automator v2")
root.geometry("420x360")

csv_file = ctk.StringVar(value="test.csv")
nmessage_file_path = ctk.StringVar(value="N_message.txt")
smessage_file_path = ctk.StringVar(value="S_message.txt")
nresume_file_path = ctk.StringVar(value="N_resume.pdf")
sresume_file_path = ctk.StringVar(value="S_resume.pdf")

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
        title="Select Sresume File",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")),
    )
    if path:
        sresume_file_path.set(path)
    print(csv_file.get())

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

frame = ctk.CTkFrame(root, corner_radius=10)
frame.pack(padx=20, pady=20, fill="both", expand=True)

select_csv_file_btn = ctk.CTkButton(frame, text="Select CSV File", command=select_csv_file, fg_color="#1e1f21", hover_color="#14375e")
select_csv_file_btn.pack(pady=5, padx=20)

select_nmessage_file_btn = ctk.CTkButton(frame, text="Select Nmessage File", command=select_Nmessage_file, fg_color="#1e1f21", hover_color="#14375e")
select_nmessage_file_btn.pack(pady=5, padx=20)

select_smessage_file_btn = ctk.CTkButton(frame, text="Select Smessage File", command=select_Smessage_file, fg_color="#1e1f21", hover_color="#14375e")
select_smessage_file_btn.pack(pady=5, padx=20)

select_nresume_file_btn = ctk.CTkButton(frame, text="Select Nresume File", command=select_Nresume_file, fg_color="#1e1f21", hover_color="#14375e")
select_nresume_file_btn.pack(pady=5, padx=20)

select_sresume_file_btn = ctk.CTkButton(frame, text="Select Sresume File", command=select_Sresume_file, fg_color="#1e1f21", hover_color="#14375e")
select_sresume_file_btn.pack(pady=5, padx=20)

send_btn = ctk.CTkButton(frame, text="Send Outreach!", command=run_engine, fg_color="#1e1f21", hover_color="#14375e")
send_btn.pack(pady=15, padx=20)

root.mainloop()