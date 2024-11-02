import os
import json
import yaml
from datetime import datetime

class FileHandler:
    def __init__(self):
        self.supported_extensions = ['.pdf', '.txt']

    def validate_file(self, file_path):
        """Validasi file input"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File tidak ditemukan: {file_path}")
            
        ext = os.path.splitext(file_path)[1].lower()
        if ext not in self.supported_extensions:
            raise ValueError(f"Format file tidak didukung: {ext}")
        
        return True

    def save_questions(self, questions, output_path, format='txt'):
        """Menyimpan pertanyaan ke file"""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        if format == 'txt':
            self._save_as_txt(questions, output_path)
        elif format == 'json':
            self._save_as_json(questions, output_path)
        else:
            raise ValueError(f"Format output tidak didukung: {format}")

    def _save_as_txt(self, questions, output_path):
        """Simpan sebagai file TXT"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"Generated Questions - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                for i, q in enumerate(questions, 1):
                    f.write(f"{i}. [{q['type']}] {q['question']}\n")
                    if 'answer' in q:
                        f.write(f"   Jawaban: {q['answer']}\n")
                    f.write("\n")
        except Exception as e:
            raise Exception(f"Error saving to TXT: {str(e)}")

    def _save_as_json(self, questions, output_path):
        """Simpan sebagai file JSON"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'generated_at': datetime.now().isoformat(),
                    'questions': questions
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise Exception(f"Error saving to JSON: {str(e)}")

    def load_config(self, config_path):
        """Load konfigurasi dari file YAML"""
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            raise Exception(f"Error loading config: {str(e)}")