class Person:

    def __init__(self, name, birth_year, gender,
                 father=None, mother=None):
        self.name, self.birth_year, self.gender = name, birth_year, gender
        self.mother, self.father = mother, father
        for parent in [father, mother]:
            if parent:
                parent.add_children(self)
        self.children_list = []

    def add_children(self, *args):
        self.children_list.extend(args)

    def children(self, gender=""):
        return [child for child in self.children_list
                if not gender or child.gender == gender]

    def siblings(self, gender=""):
        siblings = set()
        for parent in [self.father, self.mother]:
            if parent:
                siblings.update(parent.children(gender))
        siblings.discard(self)
        return siblings

    def get_brothers(self):
        return list(self.siblings("M"))

    def get_sisters(self):
        return list(self.siblings("F"))

    def is_direct_successor(self, person):
        return person in self.children()
