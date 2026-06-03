from logic import check_params, parse_line, run_sim

def show_menu():
    print("\n" + "=" * 33)
    print(" СИМУЛЯТОР БАРЖИ ".center(33, "="))
    print("=" * 33)
    print(" 1. Ввести маршрут вручную")
    print(" 2. Загрузить маршрут из файла")
    print(" 0. Выход")
    print("=" * 33)

def get_params():
    while True:
        try:
            print("\nВведите параметры маршрута N, K, P через пробел:")
            line = input("Параметры: ").strip()
            parts = line.split()
            if len(parts) != 3:
                print("Ошибка: введите ровно три числа.")
                continue
            n, k, p = map(int, parts)
            if not check_params(n, k, p):
                print("Ошибка: числа должны быть от 1 до 100000.")
                continue
            return n, k, p
        except ValueError:
            print("Ошибка: нужно ввести целые числа.")

def get_ops(n):
    print(f"\nВведите {n} строк с операциями (формат: + A B или - A B):")
    ops = []
    while len(ops) < n:
        try:
            line = input(f"Операция {len(ops) + 1}/{n}: ")
            ops.append(parse_line(line))
        except ValueError as e:
            print(f"Ошибка: {e}")
    return ops

def show_res(res):
    if res == -1:
        print("\nРезультат: Error")
    else:
        print(f"\nРезультат: {res}")

def run_manual():
    try:
        n, k, p = get_params()
        ops = get_ops(n)
        res = run_sim(n, k, p, ops)
        show_res(res)
    except (EOFError, KeyboardInterrupt):
        print("\nВвод прерван.")

def run_file():
    filename = input("\nВведите путь к файлу: ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        if not lines:
            print("Ошибка: файл пуст.")
            return

        n, k, p = map(int, lines[0].split())
        if not check_params(n, k, p) or len(lines) - 1 < n:
            print("Ошибка: неверные параметры или мало строк.")
            return

        ops = [parse_line(lines[i]) for i in range(1, n + 1)]
        res = run_sim(n, k, p, ops)
        show_res(res)
    except (FileNotFoundError, PermissionError):
        print("Ошибка: не удалось прочитать файл.")
    except ValueError as e:
        print(f"Ошибка в формате данных: {e}")

def main():
    print("\nДобро пожаловать в симулятор погрузки баржи!")
    while True:
        show_menu()
        choice = input("Выберите пункт меню (1, 2 или 0): ").strip()
        if choice == "1":
            run_manual()
        elif choice == "2":
            run_file()
        elif choice == "0":
            print("\nЗавершение работы. До свидания!")
            break
        else:
            print("Ошибка: введите корректный пункт.")

if __name__ == "__main__":
    main()
