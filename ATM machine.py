import xdrlib


PIN = "1234"
PERCENT_PULL = 0.015
OPERATION_ADDED = 3
PERCENT_ADD = 0.03
MIN_PERCENTAGE = 30
MAX_PERCENTAGE = 600
MIN_BANKNOTE = 50
MIN_TAX = 5_000_000
PERCENT_TAX = 0.1

operation_log = []


def logging(operation: str):
    operation_log.append(operation)


def show_log():
    print("-- ЖУРНАЛ ОПЕРАЦИЙ --")
    for o in operation_log:
        print(o)


def tax_pay(summ: float) -> float:
    tax = summ * PERCENT_TAX
    print(f"Удержан налог на богатых: {tax:.2f}")
    summ -= tax
    logging(f"Удержан налог на богатых: {tax:.2f}")
    return summ


def push_cash(balance: float) -> (float):
    summ = float(input("Введите сумму пополнения: "))
    logging(f"Пополняем баланс на {summ}")
    result = False

    
    if balance > MIN_TAX:
        balance = tax_pay(balance)

    
    if summ % 50 == 0:
        balance += summ
        print(f"Баланс увеличен: {summ:.2f}")
        logging(f"Успешно! Баланс увеличен: {summ:.2f}")
        result = True
    else:
        print("Сумма должна быть кратной 50!")
        logging("Отмена! Сумма должна быть кратной 50!")

    show_balance(balance)
    return result, balance


def pull_cash(balance: float) -> (float):
    result = False
    show_balance(balance)
    summ = float(input("Введите сумму для снятия: "))
    logging(f"Попытка снятия - {summ}")
    if balance > MIN_TAX:
        balance = tax_pay(balance)

    if summ % 50 == 0:
        percent_summ = summ * PERCENT_PULL

        if percent_summ > MAX_PERCENTAGE:
            percent_summ = MAX_PERCENTAGE
        if percent_summ < MIN_PERCENTAGE:
            percent_summ = MIN_PERCENTAGE

        if balance - summ - percent_summ < 0:
            print("Недостаточно средств!")
            logging("Отмена! Недостаточно средств!")
        else:
            balance -= (summ + percent_summ)
            print(f"Выдано {summ:.2f}, комиссия {percent_summ:.2f}")
            logging(f"Успешно! Выдано {summ:.2f}, комиссия {percent_summ:.2f}")
            result = True
    else:
        print("Сумма должна быть кратной 50!")
        logging("Отмена! Сумма должна быть кратной 50!")

    show_balance(balance)

    return result, balance


def show_balance(summ: float):
    print(f"Текущий баланс : {summ:.2f}")


def show_menu(menu: dict[int, str]) -> int:
    for k, v in menu.items():
        print(f"{k} - {v}")
    result = int(input("> "))
    return result if result in menu.keys() else 0


balance: float = 0
operation_counter = 0
menu_bank: dict = {
    1: "снять",
    2: "пополнить",
    3: "баланс",
    0: "выход",
}


authorized = PIN == (input("Введите PIN: "))

while authorized:
    action = show_menu(menu_bank)
    match action:
        case 1:
            success, balance = pull_cash(balance)
            if success:
                operation_counter += 1
        case 2:
            success, balance = push_cash(balance)
            if success:
                operation_counter += 1
        case 3:
            show_balance(balance)
        case 0:
            print("До встречи!")
            break

    if operation_counter == OPERATION_ADDED:
        operation_counter = 0
        summ_add = balance * PERCENT_ADD
        print(f"Начисление %: {summ_add:.2f}")
        logging(f"Начисление %: {summ_add:.2f}")
        balance += summ_add
        show_balance(balance)
else:
    print("Неверный пин-код!")

show_log()