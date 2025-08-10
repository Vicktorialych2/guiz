questions = {
    "Сколько планет в Солнечной Системе?": "8",
    "Столица Франции?": "Париж",
    'Какая планета красного цвета?': 'Марс'
}

score = 0


for q, a in questions.items():
    user_answer = input(f"{q} ")
    if user_answer.lower() == a.lower():
        print("Правильно")
        score += 1
    else:
        print("Неправильно")

print(f"Ваш результат {score} из {len(questions)}.")