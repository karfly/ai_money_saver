import time


class ScenarioRunner(object):
    def __init__(self, browser, scenario):
        self.browser = browser
        self.scenario = scenario
        self.current_step = 0

    def run_act(self, act):
        message = act['description'] if 'description' in act else ''
        message += ' | '
        message += 'delay {} sec'.format(act['delay']) if 'description' in act else ''
        print(message)

        if act['action'] == 'get':
            self.browser.get(act['url'])
        else:
            element = self.browser.find_element_by_xpath(act['xpath'])
            if act['action'] == 'send_keys':
                element.send_keys(act['text'])
            elif act['action'] == 'click':
                element.click()

        if 'delay' in act:
            time.sleep(act['delay'])

    def run(self):
        for act in self.scenario:
            self.run_act(act)

    def run_next(self):
        self.run_act(self.scenario[self.current_step])
        self.current_step += 1