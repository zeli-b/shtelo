from economy import Currency, Company

terro = Currency('테로', 'Ŧ', 10**10, 10**10, 0)
companies = list()


def show_state():
    print(f' === {terro.symbolize_expectation(terro.get_expectation())} ===')
    print(f'{"DISCORD ID":>20} {"BALANCE":>12}')
    for company in companies:
        print(f'{company.discord_id:20d} {terro.symbolize(company.balance, "10,.2f")}')
    print()


def main():
    companies.append(sch := Company(366565792910671873, 0, terro))
    companies.append(weiss := Company(668118780542451713, 0, terro))

    show_state()

    sch.earn(600)
    weiss.earn(600)
    show_state()

    print(weiss.pay(weiss.balance))
    print(sch.pay(sch.balance))
    show_state()


if __name__ == '__main__':
    main()
