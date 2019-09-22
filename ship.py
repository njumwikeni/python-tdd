class Ship:
    def __init__(self, draft, crew):
        self.draft=draft
        self.crew=crew

    def is_worth_it(self):

        return True if (self.draft - (1.5 * self.crew))>20 else False

Titanic = Ship(40,10)
print (Titanic.is_worth_it())
