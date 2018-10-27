from data import get_file_path

CONFIG = {'model':{'word2vec_path':get_file_path('sgns.baidubaike.bigram-char.bz2'),'min_frequency':1}
          ,'constant':{'stop_words_path':get_file_path('stopword.txt', folder='stopwordList'),'similar_words_num':'2',
                       'ask_data_path':get_file_path('1 大家问.xlsx')}
          }

HIGHFREQUENCYSEARCH = ['房型']


def get(root_path, sub_path):
    return CONFIG[root_path][sub_path]


def get_highFrequencySearch():
    return HIGHFREQUENCYSEARCH
