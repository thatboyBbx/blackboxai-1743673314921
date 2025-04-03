from classifier import DocumentClassifier
from ocr_utils import extract_text
from typing import Tuple
import os

class DocumentProcessor:
    """Core document processing engine without UI"""
    
    def __init__(self):
        self.classifier = DocumentClassifier()
        
    def process(self, file_path: str) -> dict:
        """Process document and return results as dict
        
        Args:
            file_path: Path to PDF/image document
            
        Returns:
            {
                'category': str,
                'confidence': float, 
                'text': str,
                'success': bool,
                'error': str|None
            }
        """
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
                
            text = extract_text(file_path)
            category, confidence = self.classifier.predict(text)
            
            return {
                'category': category,
                'confidence': confidence,
                'text': text,
                'success': True,
                'error': None
            }
            
        except Exception as e:
            return {
                'category': None,
                'confidence': 0.0,
                'text': None, 
                'success': False,
                'error': str(e)
            }

# Example usage:
if __name__ == "__main__":
    # Demo the core functionality
    processor = DocumentProcessor()
    result = processor.process("sample.pdf")
    
    if result['success']:
        print(f"Category: {result['category']}")
        print(f"Confidence: {result['confidence']:.1%}")
        print(f"Text extracted ({len(result['text'])} chars):")
        print(result['text'][:200] + "...")
    else:
        print(f"Error: {result['error']}")