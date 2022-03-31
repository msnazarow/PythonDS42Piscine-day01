import sys


class CaseInsensitiveKey(object):
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key.lower())

    def __eq__(self, other):
        return self.key.lower() == other.key.lower()

    def __str__(self):
        return self.key


class CaseInsensitiveDict(dict):
    def __init__(self, *args, **kwargs):
        super(CaseInsensitiveDict, self).__init__(*args, **kwargs)
        self._convert_keys()

    def __setitem__(self, key, value):
        key = CaseInsensitiveKey(key)
        super(CaseInsensitiveDict, self).__setitem__(key, value)

    def __getitem__(self, key):
        key = CaseInsensitiveKey(key)
        return super(CaseInsensitiveDict, self).__getitem__(key)

    def get(self, key):
        return super(CaseInsensitiveDict, self).get(CaseInsensitiveKey(key)) if key else None

    def _convert_keys(self):
        for k in list(self.keys()):
            v = super(CaseInsensitiveDict, self).pop(k)
            self.__setitem__(k, v)


def main(*args):
    if len(args) != 2:
        return
    inputs = map(lambda x: x.strip(), args[1].split(','))
    companies = CaseInsensitiveDict(zip(main.companies.values(), main.companies.keys()))
    for input in inputs:
        company = main.companies.get(input)
        if company:
            stock = main.stocks.get(company)
            if stock:
                print('{} stock price is {}'.format(input.capitalize(), stock))
                continue
        company = companies.get(input)
        if company:
            print('{} is a ticker symbol for {}'.format(input.upper(), company))
            continue
        print('{} is an unknown company or an unknown ticker symbol'.format(input))


if __name__ == '__main__':
    main.companies = CaseInsensitiveDict({
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    })
    main.stocks = CaseInsensitiveDict({
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    })
    main(*sys.argv)
