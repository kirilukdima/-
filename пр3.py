students = {}

print("Введіть ім'я студента та його оцінку (1-12). Для завершення введіть 'stop'.")

while True:
    name = input("Ім'я студента: ")
    if name.lower() == "stop":
        break
    try:
        grade = int(input("Оцінка: "))
        if 1 <= grade <= 12:
            students[name] = grade
        else:
            print("⚠️ Оцінка має бути в діапазоні 1-12!")
    except ValueError:
        print("⚠️ Введіть число як оцінку!")

print("\n📊 Результати:")
for name, grade in students.items():
    print(f"{name}: {grade}")
if students:
    avg = sum(students.values()) / len(students)
    print(f"\nСередній бал по групі: {avg:.2f}")
else:
    print("\nСписок студентів порожній.")
    exit()
excellent = [name for name, grade in students.items() if 10 <= grade <= 12]
good = [name for name, grade in students.items() if 7 <= grade <= 9]
bad = [name for name, grade in students.items() if 4 <= grade <= 6]
failed = [name for name, grade in students.items() if 1 <= grade <= 3]
print(f"\nВідмінники (10-12): {len(excellent)} → {excellent}")
print(f"Хорошисти (7-9): {len(good)} → {good}")
print(f"Відстаючі (4-6): {len(bad)} → {bad}")
print(f"Не здали (1-3): {len(failed)} → {failed}")
