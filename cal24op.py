
class Cal24op():
    # if all 3 params are given, l and r are objects
    # if only 1 param is given, l is a number
    def __init__(self, l, r=0, op="$"):
        self.l = l
        self.r = r
        self.op = op
        self.result = 0
        self.print_result = "(" + str(l) + ")"
        self.valid = True
        self.cal()

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
             self.result = self.l.result + self.r.result
             self.print_result = "(" + self.l.print_result + " + " + self.r.print_result + ")"
        elif self.op == "*":
             self.result = self.l.result * self.r.result
             self.print_result = "(" + self.l.print_result + " * " + self.r.print_result + ")"
        elif self.op == "-":
             if self.l.result > self.r.result:
                 self.result = self.l.result - self.r.result
                 self.print_result = "(" + self.l.print_result + " - " + self.r.print_result + ")"
             else:
                 self.result = self.r.result - self.l.result
                 self.print_result = "(" + self.r.print_result + " - " + self.l.print_result + ")"
        elif self.op == "/":
                 if self.l.result >= self.r.result and self.r.result != 0 and self.l.result % self.r.result == 0:
                     self.result = int(self.l.result / self.r.result)
                     self.print_result = "(" + self.l.print_result + " / " + self.r.print_result + ")"
                 elif self.r.result >= self.l.result and self.l.result != 0 and self.r.result % self.l.result == 0:
                     self.result = int(self.r.result / self.l.result)
                     self.print_result = "(" + self.r.print_result + " / " + self.l.print_result + ")"
                 else:
                     self.valid = False
        else:
            self.valid = False
       

