
def is_valid(line: str) -> bool:
    symbol, interval, password = line.split(" ")
    interval_from, interval_to = interval.split("-")
    appears = password.count(symbol)
    if int(interval_from) <= appears <= int(interval_to[:-1]):
        return True
    return False


def check_file_passwords(file_name: str) -> int:
    with open("data.txt", "r") as f:
        result = 0
        for line in f:
            result += is_valid(line)
    return result

if __name__ == '__main__':
    print(check_file_passwords("data.txt"))