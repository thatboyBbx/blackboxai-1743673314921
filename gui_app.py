import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from classifier import DocumentClassifier
from ocr_utils import extract_text
import os

class DocumentProcessorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ministry Document Processor")
        self.root.geometry("800x600")
        
        self.classifier = DocumentClassifier()
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # File selection frame
        file_frame = ttk.LabelFrame(self.root, text="Document Selection", padding=10)
        file_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.file_path = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.file_path, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Browse...", command=self.browse_file).pack(side=tk.LEFT)
        ttk.Button(file_frame, text="Process", command=self.process_document).pack(side=tk.LEFT, padx=10)
        
        # Results frame
        results_frame = ttk.LabelFrame(self.root, text="Results", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Category results
        ttk.Label(results_frame, text="Category:").grid(row=0, column=0, sticky=tk.W)
        self.category_var = tk.StringVar()
        ttk.Label(results_frame, textvariable=self.category_var, font=('Arial', 10, 'bold')).grid(row=0, column=1, sticky=tk.W)
        
        ttk.Label(results_frame, text="Confidence:").grid(row=1, column=0, sticky=tk.W)
        self.confidence_var = tk.StringVar()
        ttk.Label(results_frame, textvariable=self.confidence_var).grid(row=1, column=1, sticky=tk.W)
        
        # Extracted text
        ttk.Label(results_frame, text="Extracted Text:").grid(row=2, column=0, sticky=tk.NW)
        self.text_display = tk.Text(results_frame, wrap=tk.WORD, width=80, height=20)
        self.text_display.grid(row=3, column=0, columnspan=2, pady=5)
        
        scrollbar = ttk.Scrollbar(results_frame, command=self.text_display.yview)
        scrollbar.grid(row=3, column=2, sticky=tk.NS)
        self.text_display.config(yscrollcommand=scrollbar.set)
        
    def browse_file(self):
        filetypes = (
            ('PDF files', '*.pdf'),
            ('Image files', '*.png *.jpg *.jpeg'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(title="Select document", filetypes=filetypes)
        if filename:
            self.file_path.set(filename)
            
    def process_document(self):
        path = self.file_path.get()
        if not path or not os.path.exists(path):
            messagebox.showerror("Error", "Please select a valid file")
            return
            
        try:
            # Process document
            text = extract_text(path)
            category, confidence = self.classifier.predict(text)
            
            # Update UI
            self.category_var.set(category)
            self.confidence_var.set(f"{confidence:.1%}")
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, text)
            
        except Exception as e:
            messagebox.showerror("Processing Error", f"Failed to process document:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentProcessorGUI(root)
    root.mainloop()