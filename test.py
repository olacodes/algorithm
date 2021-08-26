class testing:
    name = 'siduq'
    def __init__(self):
        print('helo World')
    # def __init__(self):
    #     print("sodiq")

    def run(self, name):
        return (f'{name} can run if is a {self.name} living theing')


x = testing()
print(x.run('ola'))