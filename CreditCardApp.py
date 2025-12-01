from CreditCard import CreditCard

if __name__ == '__main__':
    cc = CreditCard('John Doe', 'Bank of Python', '1234 5678 9012 3456', 5000)
    
    print(f'Customer: {cc.get_customer()}')
    print(f'Bank: {cc.get_bank()}')
    print(f'Account: {cc.get_account()}')
    print(f'Limit: {cc.get_limit()}')
    print(f'Initial Balance: {cc.get_balance()}')
