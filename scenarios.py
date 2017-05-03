def get_tinkoff_login_scenario(login, password):
    tinkoff_login_scenario = list()

    tinkoff_login_scenario.append({
        'action': 'get',
        'url': 'https://www.tinkoff.ru/login/',
        'delay': 20,
        'description': 'load login page'
    })

    tinkoff_login_scenario.append({
        'action': 'send_keys',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/form/div/div[1]/div/div/div/label/div[1]/input',
        'text': login,
        'delay': 10,
        'description': 'enter login'
    })

    tinkoff_login_scenario.append({
        'action': 'send_keys',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/form/div/div[1]/div[2]/div/div/label/div[1]/input',
        'text': password,
        'delay': 10,
        'description': 'enter password'
    })

    tinkoff_login_scenario.append({
        'action': 'click',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/form/div/span/button[1]',
        'delay': 20,
        'description': 'click login button'
    })

    return tinkoff_login_scenario


def get_tinkoff_transfer_scenario(amount):
    tinkoff_transfer_scenario = list()

    tinkoff_transfer_scenario.append({
        'action': 'get',
        'url': 'https://www.tinkoff.ru/payments/card-to-card/',
        'delay': 20,
        'description': 'load card-to-card page'
    })

    tinkoff_transfer_scenario.append({
        'action': 'click',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div[1]/div/div/div[1]/div',
        'delay': 1,
        'description': 'drag down upper menu'
    })

    tinkoff_transfer_scenario.append({
        'action': 'click',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/ul/li[4]/div/div[1]/div',
        'delay': 1,
        'description': 'choose random card to swap'
    })

    tinkoff_transfer_scenario.append({
        'action': 'click',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div[1]/div[2]',
        'delay': 1,
        'description': 'drag down lower menu'
    })

    tinkoff_transfer_scenario.append({
        'action': 'click',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/form/div[3]/div[2]/div/div/div/div/div[2]/div/div[1]/ul/li[2]/div/div[1]/div[1]',
        'delay': 1,
        'description': 'choose virtual card'
    })

    tinkoff_transfer_scenario.append({
        'action': 'click',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div[1]/div/div/div[1]/div',
        'delay': 1,
        'description': 'drag down upper menu'
    })

    tinkoff_transfer_scenario.append({
        'action': 'click',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/ul/li[1]/div/div[1]/div[1]',
        'delay': 1,
        'description': 'choose tinkoff card'
    })

    tinkoff_transfer_scenario.append({
        'action': 'send_keys',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/form/div[4]/div/div/div/div/label/div[1]/input',
        'text': str(amount),
        'delay': 5,
        'description': 'enter money amount'
    })

    tinkoff_transfer_scenario.append({
        'action': 'click',
        'xpath': '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/form/div[6]/div/div/div/div[1]/div/div/div/button',
        'delay': 1,
        'description': 'click transfer money'
    })

    return tinkoff_transfer_scenario


def get_tinkoff_caffeine_scenario():
    tinkoff_caffeine_scenario = list()

    tinkoff_caffeine_scenario.append({
        'action': 'get',
        'url': 'https://www.tinkoff.ru/profile/',
        'delay': 0,
        'description': 'wait'
    })

    return tinkoff_caffeine_scenario
