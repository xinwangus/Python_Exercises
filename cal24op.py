
class Cal24op():
    def __init__(self, l, r, op):
        self.l = l
        self.r = r
        self.op = op
        self.result = 0
        self.print_result = ""
        self.valid = True

    def cal(self):
        if self.l == 0 and self.r == 0:
            self.valid = False
        elif self.l == 0:
            self.result = self.r
            self.print_result = "(" + str(self.r) + ")"
        elif self.r == 0:
            self.result = self.l
            self.print_result = "(" + str(self.l) + ")"
        elif self.op == "+":
             self.result = self.l + self.r
             self.print_result = "(" + str(self.l) + " + " + str(self.r) + ")"
        elif self.op == "*":
             self.result = self.l * self.r
             self.print_result = "(" + str(self.l) + " * " + str(self.r) + ")"
        elif self.op == "-":
             if self.l > self.r:
                 self.result = self.l - self.r
                 self.print_result = "(" + str(self.l) + " - " + str(self.r) + ")"
             else:
                 self.result = self.r - self.l
                 self.print_result = "(" + str(self.r) + " - " + str(self.l) + ")"
        elif self.op == "/":
                 if self.l >= self.r and self.l % self.r == 0:
                     self.result = int(self.l / self.r)
                     self.print_result = "(" + str(self.l) + " / " + str(self.r) + ")"
                 elif self.r >= self.l and self.r % self.l == 0:
                     self.result = int(self.r / self.l)
                     self.print_result = "(" + str(self.r) + " / " + str(self.l) + ")"
                 else:
                     self.valid = False
        else:
            self.valid = False
       

