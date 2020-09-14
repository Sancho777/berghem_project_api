def get_change_formated_for(value, received):

    available_paper = [1, 5, 10, 50, 100]
    available_coins = [1, 5, 10, 50]

    if value > received:
        raise Exception(
            "The received value may not be larger than the initial value."
        )

    change_value = float(received) - float(value)

    l = []
    if change_value > 1 and len(available_paper) > 0:
        for p in reversed(available_paper):
            if change_value >= p:
                n = int(change_value/p)
                r = change_value - p * n
                l.append(f"{n} nota(s) de R$ {p}. ")
                change_value = r

    if change_value > 0:
        change_value *= 100
        # print(change_value)
        for p in reversed(available_coins):
            if change_value >= p:
                n = int(change_value/p)
                r = change_value - p * n
                l.append(f"{n} moeda(s) de {p} centavos. ")
                change_value = r
    result = ''.join(l)
    return result
