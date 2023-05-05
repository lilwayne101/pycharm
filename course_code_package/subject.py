class Subject:
    def __init__(self, math, chinese, english):
        self.math = math
        self.cne = chinese
        self.eng = english
    pass

    def __getattr__(self, item):
        pass