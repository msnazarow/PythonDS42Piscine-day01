import sys


def main(*args):
    if len(args) != 2:
        return
    clients = set(main.clients)
    participants = set(main.participants)
    recipients = set(main.recipients)

    if args[1] == 'call_center':
        print(clients - recipients)
    elif args[1] == 'potential_clients':
        print(participants - clients)
    elif args[1] == 'loyalty_program':
        print(clients - participants)


if __name__ == '__main__':
    main.clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com',
                    'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    main.participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                         'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    main.recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    main(*sys.argv)
