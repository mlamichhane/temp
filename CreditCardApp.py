from CreditCard import CreditCard

if __name__ == '__main__':

    visaCard = CreditCard('Ram Bahadur', 'NIMB', '1234 5678 9012 3456', 5000)
    masterCard = CreditCard('Hari Gopal', 'Nabil Bank', '1010 2020 3356 9657', 15000)

    print('Customer:', visaCard.get_customer())
    print(f'Bank: {visaCard.get_bank()}')
    print(f'Account: {visaCard.get_account()}')
    print(f'Limit: {visaCard.get_limit()}')
    print(f'Initial Balance: {visaCard.get_balance()}')

    visaCard.make_payment(8000)
    print(f'Balance: {visaCard.get_balance()}')

    if visaCard.charge(4000):
        print('Charge approved.')
    else:
        print('Charge denied.')
    
    print(f'Balance: {visaCard.get_balance()}')

