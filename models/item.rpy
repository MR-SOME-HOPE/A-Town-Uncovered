init -20 python:
    class Item(store.object):
        description = "This doesn't work because you're using a save from an older version, sorry."
        def __init__(self, id, name, description = "", image = "", cost = 0):
            self.id = id
            self.name = name
            self.description = description
            self.image = image
            self.cost = cost
