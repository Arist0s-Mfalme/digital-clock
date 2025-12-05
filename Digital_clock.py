from tkinter import Label, Tk
import time

app = Tk()
app.title("🕛 Digitle Clock")
app.geometry("600x250")
app.resizable(False, False)  # whether the user can resize your window
app.configure(bg="red")

# ---Time Label ---
clock_label = Label(app, anchor="center",
                    bg='green',
                    fg="white",
                    font=("Helvetica", 40, "bold italic"),
                    relief="flat",
                    cursor="hand2",
                    underline=8)
clock_label.pack(side="left", fill="y")

# --- Date Label ---

date_label = Label(app,
                   bg="red",
                   fg="white",
                   font=("Helvetica", 16, "bold"))

date_label.pack(side="right", fill="x")


def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    app.after(1000, update_time)


update_time()
app.mainloop()
