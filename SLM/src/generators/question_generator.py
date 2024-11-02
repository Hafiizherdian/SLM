from transformers import AutoTokenizer, AutoModelForCausalLM
from .templates import QuestionTemplates

class QuestionGeneratorBot:
    def __init__(self):
        self.model_name = "distilgpt2"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.templates = QuestionTemplates()

    def generate_questions(self, key_points, num_questions=5):
        """Membuat pertanyaan dari poin-poin penting"""
        questions = []
        
        for _ in range(num_questions):
            if not key_points:
                break
            
            # Generate question using templates
            question_data = self.templates.generate_question(key_points)
            if question_data:
                questions.append(question_data)
        
        return questions

    def generate_answer(self, question):
        """Generate jawaban untuk pertanyaan (opsional)"""
        input_text = f"Q: {question}\nA:"
        inputs = self.tokenizer(input_text, return_tensors="pt", max_length=150, truncation=True)
        
        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=150,
            num_return_sequences=1,
            temperature=0.7,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def format_question(self, question_data, include_answer=False):
        """Format pertanyaan untuk output"""
        formatted = f"[{question_data['type']}] {question_data['question']}"
        if include_answer and 'answer' in question_data:
            formatted += f"\nJawaban: {question_data['answer']}"
        return formatted

    def save_questions(self, questions, output_file):
        """Menyimpan pertanyaan ke file"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("BANK SOAL JARINGAN KOMPUTER\n")
                f.write("=" * 40 + "\n\n")
                
                for i, question_data in enumerate(questions, 1):
                    if not isinstance(question_data, dict) or 'type' not in question_data or 'question' not in question_data:
                        print(f"Warning: Pertanyaan pada indeks {i} tidak memiliki format yang valid, dilewati.")
                        continue  # Skip jika format tidak valid
                    
                    f.write(f"Soal {i}\n")
                    f.write("-" * 20 + "\n")
                    f.write(self.format_question(question_data, include_answer=True))
                    f.write("\n\n")
                    
            print(f"\nBerhasil generate {len(questions)} pertanyaan:")
            for i, q in enumerate(questions, 1):
                if isinstance(q, dict) and 'type' in q and 'question' in q:
                    print(f"{i}. [{q['type']}] {q['question']}")
                    
                    
        except Exception as e:
            print(f"Error menyimpan pertanyaan: {str(e)}")
            
