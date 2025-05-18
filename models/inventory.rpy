init -20 python:
    class Inventory(store.object):
        def __init__(self, money=50):
            self.money = money
            self.items = []
        def add(self, item):
            self.items.append(item)
        def drop(self, item):
            self.clean()
            self.items = [i for i in self.items if i.id != item.id]
        def sell(self, item):
            self.money += item.cost
            self.drop(item)
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost
                return True
            else:
                return False
        def earn(self, amount):
            self.money += amount
        def has_item(self, item):
            self.clean()
            return len([i for i in self.items if i.id == item.id]) > 0
        def clean(self):
            self.items = [i for i in self.items if hasattr(i, 'id')]
