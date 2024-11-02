import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from .text_cleaner import TextCleaner

class MaterialProcessor:
    def __init__(self):
        # Download NLTK data
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('indonesian'))
        self.text_cleaner = TextCleaner()

    def read_pdf(self, file_path):
        """Membaca dan mengekstrak teks dari file PDF"""
        text = ""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            return self.text_cleaner.clean_text(text)
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")

    def read_txt(self, file_path):
        """Membaca file TXT"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return self.text_cleaner.clean_text(text)
        except Exception as e:
            raise Exception(f"Error reading TXT: {str(e)}")

    def extract_key_points(self, text):
        """Mengekstrak poin-poin penting dari teks"""
        sentences = sent_tokenize(text)
        key_points = []
        
        for sentence in sentences:
            # Hanya ambil kalimat yang cukup panjang dan bermakna
            words = sentence.split()
            if len(words) > 5:  # minimal 5 kata
                clean_sentence = self.text_cleaner.clean_text(sentence)
                # Pastikan kalimat mengandung kata kunci penting
                if clean_sentence and len(clean_sentence.split()) > 3:  # minimal 3 kata setelah cleaning
                    key_points.append(clean_sentence)
        
        # Batasi jumlah karakter minimum
        key_points = [point for point in key_points if len(point) > 10]
        
        return key_points