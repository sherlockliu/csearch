from framework.handler.csearch_handler import CSearchHandler


class DemoHanlder(CSearchHandler):
    def get(self):
        self.write("This is the demo for CSearch.")
