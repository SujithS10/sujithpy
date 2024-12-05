class dad:
    def action(self):
        print("He use left hand")
        self.__priv_fun()

    def __priv_fun(self):
        print("smoking")

class first_son(dad):
    def music(self):
        print("singing")

class second_son(dad):
    def song(self):
        print("dance")

parent = dad()
parent.action()