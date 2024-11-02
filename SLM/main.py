import os
import argparse
from src.processors.material_processor import MaterialProcessor
from src.generators.question_generator import QuestionGeneratorBot
from src.utils.file_handler import FileHandler

def setup_argparse():
    parser = argparse.ArgumentParser(description='Question Generator from PDF/TXT materials')
    parser.add_argument(
        '--input',
        required=True,
        help='Path to input file (PDF/TXT)'
    )
    parser.add_argument(
        '--output',
        default='data/output/questions',
        help='Output directory for generated questions'
    )
    parser.add_argument(
        '--num_questions',
        type=int,
        default=10,
        help='Number of questions to generate'
    )
    return parser.parse_args()

def main():
    # Parse arguments
    args = setup_argparse()
    
    # Initialize components
    file_handler = FileHandler()
    bot = QuestionGeneratorBot()
    
    try:
        # Create output directory if it doesn't exist
        os.makedirs(args.output, exist_ok=True)
        
        # Generate output filename
        input_filename = os.path.basename(args.input)
        output_filename = f"questions_{os.path.splitext(input_filename)[0]}.txt"
        output_path = os.path.join(args.output, output_filename)
        
        # Generate questions
        print(f"Generating questions from: {args.input}")
        questions = bot.generate_questions(
            args.input,
            num_questions=args.num_questions
        )
        
        # Save questions
        bot.save_questions(questions, output_path)
        print(f"Questions saved to: {output_path}")
        
        # Display questions
        print("\nGenerated Questions:")
        
        for i, q in enumerate(questions, 1):
            print(f"\n{i}. [{q['type']}] {q['question']}")
            print(f"{i}. [{q['type']}] {q['topic']}")
            key_points = MaterialProcessor.extract_key_points(key_points)
            print("Extracted Topics:", key_points)  # Inspect extracted topics
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()