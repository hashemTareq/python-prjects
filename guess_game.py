questions = [
  {
    'question': 'What is the captical of Yemen?',
    'option': ['A. Sanaa', 'B. Aden', 'C. Taiz'],
    'answer': 'A'
  },
  {
    'question': 'How many goals did messi score in 2012?',
    'option': ['A. 73', 'B. 91', 'C. 88'],
    'answer': 'B'
  },
  {
    'question': 'Where does lion live?',
    'option': ['A. Mountian', 'B. Desert', 'C. Forest'],
    'answer': 'C'
  },
  {
    'question': 'What is the biggest country in the world?',
    'option': ['A. China', 'B. Russa', 'C. Canada'],
    'answer': 'B'
  }
]

def guess_game(the_questions):
  score = 0
  for question in the_questions:
    print(question['question'])
    for option in question['option']:
      print(option)

    answer = input('Type your answer (A, B, C): ').strip().upper()
    if answer == question['answer']:
      score += 1
      print('Nice. Correct answer ✔.\n')
    else:
      print(f'Incorrect ❌. The answer is {question['answer']}.\n')

  print(f'You got {score} answers correct from {len(questions)} questions.')

guess_game(questions)
