import os
import textwrap
from classifier import DocumentClassifier
from ocr_utils import extract_text

class ConsoleInterface:
    def __init__(self):
        self.classifier = DocumentClassifier()
        self.width = 80
        
    def display_header(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        title = "Ministry Document Processing System"
        print("=" * self.width)
        print(title.center(self.width))
        print("=" * self.width)
        print()
        
    def display_menu(self):
        print("MAIN MENU".center(self.width))
        print("-" * self.width)
        print("1. Process document")
        print("2. View help")
        print("3. Exit")
        print("-" * self.width)
        
    def process_document(self):
        self.display_header()
        print("DOCUMENT PROCESSING".center(self.width))
        print("-" * self.width)
        file_path = input("Enter document path (or drag & drop file here): ").strip('"\' ')
        
        if not os.path.exists(file_path):
            input("\nError: File not found. Press Enter to continue...")
            return
            
        try:
            print("\nProcessing document...")
            text = extract_text(file_path)
            category, confidence = self.classifier.predict(text)
            
            self.display_header()
            print("PROCESSING RESULTS".center(self.width))
            print("-" * self.width)
            print(f"File: {os.path.basename(file_path)}")
            print(f"Category: {category}")
            print(f"Confidence: {confidence:.1%}")
            print("-" * self.width)
            print("\nEXTRACTED TEXT:\n")
            
            # Format text with wrapping
            wrapped_text = textwrap.fill(text, width=self.width-4)
            print(wrapped_text[:1000])  # Show first 1000 chars
            if len(text) > 1000:
                print("\n[...truncated...]")
                
            input("\nPress Enter to continue...")
            
        except Exception as e:
            input(f"\nError: {str(e)}\nPress Enter to continue...")
            
    def display_help(self):
        self.display_header()
        print("HELP & INSTRUCTIONS".center(self.width))
        print("-" * self.width)
        print("Supported file types: PDF, PNG, JPG, JPEG")
        print("For best results use clear, legible documents")
        print("The system will:")
        print("- Extract text using OCR")
        print("- Classify document type")
        print("- Show confidence score")
        print("- Display extracted text")
        input("\nPress Enter to return to menu...")

def main():
    interface = ConsoleInterface()
    while True:
        interface.display_header()
        interface.display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            interface.process_document()
        elif choice == "2":
            interface.display_help()
        elif choice == "3":
            print("\nExiting system...")
            break
        else:
            input("Invalid choice. Press Enter to continue...")

if __name__ == "__main__":
    main()