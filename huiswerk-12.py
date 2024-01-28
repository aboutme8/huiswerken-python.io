import tkinter as tk

# Functie om een reactie van de chatbot te genereren op basis van de gebruikersinvoer
def get_response():
    user_input = entry.get()
    response = "Ik begrijp je niet."

    if user_input.lower() == "hallo":
        response = "Hallo! Hoe kan ik je helpen?"
    elif user_input.lower() == "hoe gaat het?":
        response = "Het gaat goed, bedankt!"
    elif user_input.lower() == "wat is je naam?":
        response = "Ik ben een chatbot."

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Jij: " + user_input + "\n")
    chat_log.insert(tk.END, "Chatbot: " + response + "\n")
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Maak het hoofdvenster
root = tk.Tk()
root.title("Chatbot")

# Maak de chatlog en scrollbar
chat_log = tk.Text(root, height=10, width=40, state=tk.DISABLED)
scrollbar = tk.Scrollbar(root, command=chat_log.yview)
chat_log.config(yscrollcommand=scrollbar.set)

# Maak het invoerveld en knop
entry = tk.Entry(root, width=30)
send_button = tk.Button(root, text="Verstuur", command=get_response)

# Plaats de widgets op het scherm
chat_log.pack()
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
entry.pack()
send_button.pack()

# Start de GUI-loop
root.mainloop()