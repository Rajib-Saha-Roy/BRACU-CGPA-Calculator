class Model:

    def __init__(self):
        pass

    def possible_credits(self):
        return [1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10]

    def possible_grades(self):
        return ["F", "D-", "D", "D+", 'C-', "C", "C+", "B-", "B", "B+", "A-", "A"]

    def coreesponding_point(self, grd):
        dict_ = {'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3, 'B-': 2.7, 'C+': 2.3, 'C-': 2, 'D+': 1.7, 'D-': 1, 'D': 1.3,
                 'F': 0}
        return dict_[grd]
