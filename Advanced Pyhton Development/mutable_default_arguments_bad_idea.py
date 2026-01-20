def create_account(name: str, holder: str, account_holders: list = None):
    if not account_holders:
        account_holders = []
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }

a1 = create_account('checking', 'Rolf') # instead of IF NOT ACCOUNT do a1 = create_account('checking', 'Rolf', [])
a2 = create_account('savings', 'Jen')

print(a2)