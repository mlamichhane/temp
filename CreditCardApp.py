from CreditCard import CreditCard

if __name__ == '__main__':
    cc = CreditCard('John Doe', 'Bank of Python', '1234 5678 9012 3456', 5000)

    print(f'Customer: {cc.get_customer()}')
    print(f'Bank: {cc.get_bank()}')
    print(f'Account: {cc.get_account()}')
    print(f'Limit: {cc.get_limit()}')
    print(f'Initial Balance: {cc.get_balance()}')

    cc.make_payment(8000)
    print(f'Balance: {cc.get_balance()}')

    if cc.charge(3000):
        print('Charge approved.')
    else:
        print('Charge denied.')
    
    print(f'Balance: {cc.get_balance()}')

