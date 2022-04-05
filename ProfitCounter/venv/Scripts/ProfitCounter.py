def ProfitCounter(money:int,period=1):
    """
    :param money: сумма вклада
    :param period: срок, на который делается вклад
                    поскольку в условиях не оговаривается, по умолчанию выбирается 1 год
    :return: максимакльная сумма зароботка
    """
    per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
    deposit = []
    for i in range(len(per_cent)):
        deposit.append(money*(1+list(per_cent.values())[i]/100)*period)
    return max(deposit) - money

money = input("Укажите сумму вклада:")
print("Максимальная сумма, которую вы можете заработать — "+str(ProfitCounter(int(money))))