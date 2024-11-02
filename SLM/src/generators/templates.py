import random

class QuestionTemplates:
    def __init__(self):
        self.templates = {
            "pengertian": [
                "Apa yang dimaksud dengan {topic}?",
                "Jelaskan definisi dari {topic}!",
                "Bagaimana Anda menjelaskan konsep {topic}?",
                "Uraikan pengertian {topic} secara lengkap!",
                "Deskripsikan apa yang Anda ketahui tentang {topic}!"
            ],
            "penerapan": [
                "Berikan contoh penerapan {topic} dalam kehidupan sehari-hari!",
                "Bagaimana cara menerapkan konsep {topic} dalam praktik?",
                "Sebutkan manfaat dari {topic} dalam bidang {context}!",
                "Jelaskan implementasi {topic} dalam konteks {context}!",
                "Bagaimana {topic} dapat digunakan untuk menyelesaikan masalah {context}?"
            ],
            "analisis": [
                "Analisis perbedaan antara {topic} dan {context}!",
                "Apa kelebihan dan kekurangan dari {topic}?",
                "Mengapa {topic} penting dalam konteks {context}?",
                "Bagaimana hubungan antara {topic} dengan {context}?",
                "Jelaskan dampak {topic} terhadap {context}!"
            ],
            "evaluasi": [
                "Evaluasi efektivitas {topic} dalam {context}!",
                "Bagaimana pendapat Anda tentang peran {topic} dalam {context}?",
                "Berikan kritik dan saran terhadap penerapan {topic} dalam {context}!",
                "Seberapa efektif penggunaan {topic} dalam menyelesaikan {context}?",
                "Bandingkan keefektifan {topic} dengan {context}!"
            ]
        }

    def generate_question(self, key_points):
        """Generate pertanyaan menggunakan template"""
        if not key_points:
            return None
            
        # Pilih tipe pertanyaan dan template secara random
        question_type = random.choice(list(self.templates.keys()))
        template = random.choice(self.templates[question_type])
        
        # Pilih topic dan context
        topic = random.choice(key_points)
        context = random.choice(key_points) if "{context}" in template else None
        
        # Format pertanyaan
        if context:
            question = template.format(topic=topic, context=context)
        else:
            question = template.format(topic=topic)
        
        return {
            'type': question_type,
            'question': question,
            'topic': topic,
            'context': context
        }

    def add_template(self, question_type, template):
        """Menambahkan template baru"""
        if question_type not in self.templates:
            self.templates[question_type] = []
        self.templates[question_type].append(template)