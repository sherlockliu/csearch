from data import get_file_path

CONFIG = {'model':{'word2vec_path':get_file_path('sgns.baidubaike.bigram-char.bz2'),'min_frequency':1}
          ,'constant':{'stop_words_path':get_file_path('stopword.txt', folder='stopwordList'),'similar_words_num':'2',
                       'ask_data_path':get_file_path('3 questions.xlsx')}
          }

HIGHFREQUENCYSEARCH = ['房型', '早餐', '游泳池', '接送机', '停车场', '房型', '服务设施', '交通', '加床', '附近景点']
QUESTION = ['为什么没有送机服务', '为什么同样的房型几种价格呢', '为什么小朋友需要另付早餐费', '为什么没有到机场的免费接驳巴士', '为什么没有游泳池', '为什么不可以加床']
HOTELLIST = [('三亚亚龙湾华宇度假酒店', '346693'), ('三亚亚龙湾美高梅度假酒店', '345078'), ('金茂三亚亚龙湾希尔顿大酒店', '345071'), ('三亚亚龙湾喜来登度假酒店', '345080'), ('三亚天域度假酒店', '345522'),
('三亚亚龙湾红树林度假酒店', '345553'), ('三亚亚龙湾万豪度假酒店', '344928'), ('金茂三亚亚龙湾丽思卡尔顿酒店', '345101'), ('三亚维景国际度假酒店', '353871'),
('三亚亚龙湾君澜度假酒店（原假日度假酒店）', '429615'), ('三亚亚龙湾凯莱仙人掌度假酒店', '346766'), ('三亚华宇亚龙湾迎宾馆', '4371952'), ('三亚亚龙湾人间天堂-鸟巢度假村', '435983'),
('三亚亚龙湾瑞吉度假酒店', '345074'), ('三亚亚龙湾铂尔曼别墅度假酒店', '430163'), ('三亚太阳湾柏悦酒店', '1601597'), ('三亚亚龙湾五号度假别墅酒店', '396528'),
('三亚亚龙湾爱琴海全套房精品度假酒店', '345076'), ('三亚亚龙湾金棕榈度假酒店', '371722')]

def get(root_path, sub_path):
    return CONFIG[root_path][sub_path]


def get_highFrequencySearch():
    return HIGHFREQUENCYSEARCH

def get_hotel_list():
    return HOTELLIST
