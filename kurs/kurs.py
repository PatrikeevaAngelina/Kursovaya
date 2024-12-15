def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Значение должно быть неотрицательным.")
            return value
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, введите корректное число.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Значение должно быть неотрицательным.")
            return value
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, введите корректное целое число.")


def calculate_event_cost():
    print("Калькулятор стоимости мероприятия (Выставка)")

    # Ввод данных
    exhibition_name = input("Введите название выставки: ")
    venue_cost = get_float_input("Введите стоимость аренды помещения (в рублях): ")
    number_of_participants = get_int_input("Введите количество участников: ")
    cost_per_participant = get_float_input("Введите стоимость участия одного человека (в рублях): ")
    catering_cost = get_float_input("Введите стоимость гастрономического обслуживания (в рублях): ")
    marketing_cost = get_float_input("Введите стоимость маркетинга (в рублях): ")
    additional_costs = get_float_input("Введите дополнительные расходы (в рублях): ")

    number_of_staff = get_int_input("Введите количество сотрудников на мероприятии: ")
    staff_salary_per_person = get_float_input("Введите зарплату одного сотрудника за выставку (в рублях): ")

    # Расчет общей стоимости
    total_participant_cost = number_of_participants * cost_per_participant
    total_staff_cost = number_of_staff * staff_salary_per_person
    total_cost = (venue_cost + total_participant_cost + catering_cost +
                  marketing_cost + additional_costs + total_staff_cost)

    # Вывод результата
    print("\n--- Итоговая стоимость мероприятия ---")
    print(f"Название выставки: {exhibition_name}")
    print(f"Стоимость аренды помещения: {venue_cost:.2f} руб.")
    print(f"Стоимость участия для {number_of_participants} участников: {total_participant_cost:.2f} руб.")
    print(f"Стоимость гастрономического обслуживания: {catering_cost:.2f} руб.")
    print(f"Стоимость маркетинга: {marketing_cost:.2f} руб.")
    print(f"Дополнительные расходы: {additional_costs:.2f} руб.")
    print(f"Зарплата для {number_of_staff} сотрудников: {total_staff_cost:.2f} руб.")
    print(f"Общая стоимость мероприятия: {total_cost:.2f} руб.")


if __name__ == "__main__":
    calculate_event_cost()

