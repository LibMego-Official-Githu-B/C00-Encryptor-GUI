import tkinter as tk
from tkinter import messagebox, colorchooser


def char_to_code(char):
    if char.isalpha():
        return str(ord(char.lower()) - ord('a') + 1)
    elif char == ' ':
        return '00'  # space
    else:
        return '.'  # any other symbol


def encrypt_phrase(phrase):
    # Step 1: Convert phrase chars to code string (letters to numbers, spaces to 00, symbols to .)
    codes = [char_to_code(c) for c in phrase]
    base_num_str = ''.join(codes)

    # Step 2: Length of the base number string (digits count)
    length = len(base_num_str)

    # Step 3: Multiply base number by length
    if '.' in base_num_str:
        return f"Cannot encrypt phrase with symbols, '.' detected in encoding."

    base_num_int = int(base_num_str)
    multiplied = base_num_int * length

    # Step 4: Reverse the multiplied number string
    multiplied_str = str(multiplied)
    reversed_str = multiplied_str[::-1]

    # Step 5: Subtract reversed number from multiplied number
    reversed_int = int(reversed_str)
    subtracted = multiplied - reversed_int

    # Step 6: Multiply by 2
    final_result = subtracted * 2

    # Step 7: Prefix with length + "/"
    encrypted = f"{length}/{final_result}"
    return encrypted


def encrypt_action():
    phrase = input_entry.get()
    if not phrase:
        messagebox.showwarning("Input Error", "Please enter a phrase to encrypt.")
        return
    encrypted_phrase = encrypt_phrase(phrase)
    result_label.config(text=f"Encrypted Result:\n{encrypted_phrase}")


def change_background_color():
    color_code = colorchooser.askcolor(title="Pick a Background Color")[1]
    if color_code:  # If a valid color is selected
        root.config(bg=color_code)
        header_label.config(bg=color_code)
        footer_label.config(bg=color_code)
        input_entry.config(bg=color_code)
        encrypt_button.config(bg=color_code)
        result_label.config(bg=color_code)


def change_text_color():
    color_code = colorchooser.askcolor(title="Pick a Text Color")[1]
    if color_code:  # If a valid color is selected
        header_label.config(fg=color_code)
        footer_label.config(fg=color_code)
        input_entry.config(fg=color_code)
        encrypt_button.config(fg=color_code)
        result_label.config(fg=color_code)


# Main window
root = tk.Tk()
root.title("C00 Encryption")
root.geometry("400x600")  # Mobile-friendly window size
root.config(bg="#1d1f2f")

# Header
header_label = tk.Label(root, text="Encrypt Your Phrase", font=("Arial", 18, "bold"), fg="white", bg="#1d1f2f")
header_label.pack(pady=20)

# Input field
input_entry = tk.Entry(root, font=("Arial", 14), width=30, bd=0, relief="solid", highlightthickness=2, highlightcolor="#ff6f61")
input_entry.pack(pady=10)

# Encrypt Button
encrypt_button = tk.Button(root, text="Encrypt", font=("Arial", 14), fg="white", bg="#ff6f61", relief="flat", padx=20, pady=10, command=encrypt_action)
encrypt_button.pack(pady=20)

# Result label (with automatic text wrapping)
result_label = tk.Label(root, text="Encrypted Result: ", font=("Arial", 12), fg="white", bg="#1d1f2f", justify="left", anchor="w", wraplength=1025)
result_label.pack(pady=10, padx=10, fill="x")

# Change background button
color_button = tk.Button(root, text="Change Background Color", font=("Arial", 12), fg="white", bg="#4caf50", relief="flat", padx=20, pady=10, command=change_background_color)
color_button.pack(pady=10)

# Change text color button
text_color_button = tk.Button(root, text="Change Text Color", font=("Arial", 12), fg="white", bg="#007bff", relief="flat", padx=20, pady=10, command=change_text_color)
text_color_button.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="C00 Encryption App", font=("Arial", 10), fg="#bbbbbb", bg="#1d1f2f")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
