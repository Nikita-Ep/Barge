from models import Barge, BargeError

def check_params(n, k, p):
    return (1 <= n <= 100000) and (1 <= k <= 100000) and (1 <= p <= 100000)

def parse_line(line):
    parts = line.strip().split()
    if len(parts) != 3:
        raise ValueError(f"Неверное число аргументов: '{line}'")

    op = parts[0]
    if op not in ('+', '-'):
        raise ValueError(f"Неизвестная операция '{op}'")

    try:
        sec = int(parts[1])
        fuel = int(parts[2])
    except ValueError:
        raise ValueError(f"Параметры должны быть целыми числами: '{line}'")

    if sec < 1:
        raise ValueError(f"Неверный номер отсека: {sec}")
    if not (1 <= fuel <= 10000):
        raise ValueError(f"Тип топлива вне диапазона: {fuel}")

    return op, sec, fuel

def run_sim(n, k, p, ops):
    barge = Barge(k, p)
    for op, sec, fuel in ops:
        try:
            if op == '+':
                barge.load(sec, fuel)
            else:
                barge.unload(sec, fuel)
        except BargeError:
            return -1

    if not barge.is_empty():
        return -1
    return barge.get_max()
