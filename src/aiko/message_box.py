class message_box_t:

    def __init__(self): 
        self.__messages = []
    

    def is_readable(self):
        return len(self.__messages) > 0


    def send(self, data):
        self.__messages.append(data)


    def read(self):
        if not self.is_readable():
            return None

        return self.__messages.pop()


    def show(self):
        if not self.is_readable():
            return None

        return self.__messages[len(self.__messages) - 1]

