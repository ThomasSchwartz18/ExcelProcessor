import tkinter as tk
from tkinter import ttk

def process_data():
    output_text.delete("1.0", "end")
    data = text_input.get("1.0", "end").strip()
    if data:
        formatted_data = ';'.join(data.split())
        output_text.insert("1.0", formatted_data)

# Create the main window
root = tk.Tk()
root.title("Data Processor")

# Set initial window size
root.geometry("800x500")  # Width x Height

# Notebook (tab bar)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Processor tab
processor_tab = ttk.Frame(notebook)
notebook.add(processor_tab, text="Processor")

# Text Box label
textbox_label = tk.Label(processor_tab, text="Paste data here:")
textbox_label.pack()

# Text input (for Text Box)
text_input = tk.Text(processor_tab, height=5)
text_input.pack()

# Process data button
process_button = tk.Button(processor_tab, text="Process Data", command=process_data)
process_button.pack(pady=10)

# Output textbox
output_text = tk.Text(processor_tab, height=5)
output_text.pack()

# Additional tab 1
additional_tab1 = ttk.Frame(notebook)
notebook.add(additional_tab1, text="Excel Formatter")
label1 = tk.Label(additional_tab1, text="Content not added yet")
label1.pack()

# Run the application
root.mainloop()