E_INT, E_FLOAT, E_STR = "INT", "FLOAT", "STR"


class EventSet:
    def __init__(self, prop):
        self.kind = {int: E_INT, float: E_FLOAT, str: E_STR}[type(prop)]
        self.prop = prop


class EventGet:
    def __init__(self, prop):
        self.kind = {int: E_INT, float: E_FLOAT, str: E_STR}[prop]
        self.prop = None


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, ob, event):
        if self.__successor is not None:
            return self.__successor.handle(ob, event)


class IntHandler(NullHandler):
    def handle(self, ob, event):
        if event.kind == E_INT:
            if event.prop is None:
                return ob.integer_field
            else:
                ob.integer_field = event.prop
        else:
            return super().handle(ob, event)


class StrHandler(NullHandler):
    def handle(self, ob, event):
        if event.kind == E_STR:
            if event.prop is None:
                return ob.string_field
            else:
                ob.string_field = event.prop
        else:
            return super().handle(ob, event)


class FloatHandler(NullHandler):
    def handle(self, ob, event):
        if event.kind == E_FLOAT:
            if event.prop is None:
                return ob.float_field
            else:
                ob.float_field = event.prop
        else:
            return super().handle(ob, event)
