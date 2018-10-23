#encoding=utf-8

import pandas as pd
from app.textPreprocessing.hotel_ask_data import HotelAskData
import re
class FileObj(object):

    def __init__(self,filepath):
        self.filepath = filepath

    def read_hotel_data(self,hotelid):
        hotel_data = pd.read_excel(self.filepath)
        hotel_data = hotel_data.drop(['replycount','adoptedreplyid','askreplyid','replycontent','datachange_lasttime'],axis=1)
        grouped_alls = hotel_data.groupby('masterhotelid')

        for name_all, group_all in grouped_alls:
            if not name_all == int(hotelid):
                continue
            hotel_group = group_all.groupby('askid')
            list_id = []
            ask_list = []
            for hotel_name,hotel_data in hotel_group:
                list_id.append(hotel_name)
                ask = str(hotel_data['asktitle'].iloc[0])
                hotel_name = re.findall("#.*?#", ask)
                ask_list.append(ask.replace(hotel_name[0],""))
            return HotelAskData(list_id,ask_list)

if __name__ == '__main__':
    file = FileObj('D:/Users/lh.zhu/Desktop/极客文化/1 店内搜索/test.xlsx')
    file.read_hotel_data('345078')
    print('over')


