# text_cleaner.py
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class TextCleaner:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('indonesian'))

    def clean_text(self, text):
        """Membersihkan teks dari karakter yang tidak diinginkan"""
        if not text:
            return ""
            
        # Menghapus karakter khusus dan angka
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\d+', ' ', text)
        
        # Menghapus whitespace berlebih
        text = ' '.join(text.split())
        
        # Mengubah ke lowercase
        text = text.lower()
        
        return text.strip()