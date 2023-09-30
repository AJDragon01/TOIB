while True:
    password = input("Введите пароль (или введите 'q' для завершения): ")
    
    if password == 'q':
        break
    
    strength = 0
    special_character = False

    for p in password:
        if p.isdigit():
            strength += 1
        elif p.islower():
            strength += 1
        elif p.isupper():
            strength += 1
        elif p in '!@#$%&':
            special_character = True
            break  # Выход из цикла, как только найден спецсимвол

    if strength >= 8 and special_character:
        print("Действительный пароль.")
    else:
        print("Действительный пароль. Рекомендации:", end=" ")
        recommendations = []

        if not any(p.isdigit() for p in password):
            recommendations.append("добавить 1 цифру")
        if not any(p.islower() for p in password):
            recommendations.append("добавить 1 маленькую букву")
        if not any(p.isupper() for p in password):
            recommendations.append("добавить 1 заглавную букву")
        if not special_character:
            recommendations.append("добавить 1 спецсимвол")
        if len(password) < 7:
            recommendations.append(f"увеличить число символов на {8 - len(password)}")

        print(', '.join(recommendations))
