CONFIG = {'model':{'word2vec_path':'F:/word2vec/sgns.baidubaike.bigram-char','min_frequency':1}
          ,'constant':{'stop_words_path':'E:/hackson/csearch/app/textPreprocessing/stopwordList/stopword.txt','similar_words_num':'2',
                       'ask_data_path':'D:/Users/lh.zhu/Desktop/极客文化/1 店内搜索/1 大家问.xlsx'}

          }
HIGHFREQUENCYSEARCH = ['房型']
def get(root_path, sub_path):
    return CONFIG[root_path][sub_path]

def get_highFrequencySearch():
    return HIGHFREQUENCYSEARCH