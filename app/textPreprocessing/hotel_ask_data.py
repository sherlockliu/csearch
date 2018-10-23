class HotelAskData(object):
    def __init__(self,id_list,ask_list):
        self.id_list = id_list
        self.ask_list = ask_list
    def get_ask_list(self):
        return self.ask_list
    def get_id_list(self):
        return self.id_list