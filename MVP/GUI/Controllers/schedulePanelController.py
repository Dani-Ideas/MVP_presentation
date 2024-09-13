from Views.schedulePanelView1 import schedulePanelView1

class schedulePanelController:
    def __init__(self, root):
        self.root = root
        self.view = schedulePanelView1(root, self)