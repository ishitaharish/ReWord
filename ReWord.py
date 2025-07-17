import tkinter as tk
from tkinter import scrolledtext, messagebox
import cohere

# Replace with your actual Cohere API key
COHERE_API_KEY = 'your_key_here'

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

def convert_text():
    input_text = input_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    prompt = f"""Convert the following message into a formal, structured, and professional corporate tone:\n\n{input_text}"""

    try:
        response = co.generate(
            model='command-r-plus',
            prompt=prompt,
            max_tokens=300,
            temperature=0.5
        )
        output_text = response.generations[0].text.strip()
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output_text)
    except Exception as e:
        messagebox.showerror("API Error", f"Error from Cohere API:\n{str(e)}")

# GUI Setup
def run_app():
    global input_box, output_box

    root = tk.Tk()
    root.title("Corporate Email Rewriter")
    root.geometry("500x350")

    tk.Label(root, text="Enter Informal Text / Email:", font=("Arial", 12)).pack(pady=5)
    input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=5, font=("Arial", 11))
    input_box.pack(padx=10, pady=10)

    convert_button = tk.Button(
        root, text="Convert to Formal Tone", command=convert_text,
        font=("Arial", 12), bg="lightblue"
    )
    convert_button.pack(pady=10)

    tk.Label(root, text="Corporate Appropriate Version:", font=("Arial", 12)).pack(pady=5)
    output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=500, height=5, font=("Arial", 11))
    output_box.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_app()
