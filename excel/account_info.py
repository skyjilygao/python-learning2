class account_info:
    act = ''
    sale = ''
    dept = ''
    owner_company = ''
    apply_info = ''

    def __init__(self, act, sale: str = '', dept: str = '', owner_company: str = '', apply_info: str = ''):
        self.act = act
        self.sale = sale
        self.dept = dept
        self.owner_company = owner_company
        self.apply_info = apply_info
