class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

    def __init__(self, seq=None, **kwargs):  # known special case of dict.__init__
        super().__init__()
        for elem in seq:
            self[elem[0]] = elem[1]

    def __repr__(self):
        repl = ""
        for key in self.keys():
            for value in self[key]:
                repl += ("'%s': '%s'\n" % (key, value))
        return repl[:-1]


def main(*args):
    countries = dict(main.list_of_tuples)
    print(Dictlist(zip(countries.values(), countries.keys())))


if __name__ == '__main__':
    main.list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    main()
