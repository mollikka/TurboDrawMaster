from tool import Tool as default_tool
default_color = (0,0,0)

class User(object):

    def __init__(self):
        self.active_tool = default_tool()
        self.active_color = default_color
