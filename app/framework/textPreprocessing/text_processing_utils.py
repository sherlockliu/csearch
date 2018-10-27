from app.framework.textPreprocessing.zhcnSegment import *
from gensim.models import KeyedVectors
from app.framework.textPreprocessing import config as cfg
from app.framework.textPreprocessing.sentenceSimilarity import SentenceSimilarity
from app.framework.textPreprocessing.fileObject import FileObj
import pandas as pd
import re
model_map = {}
id_map = {}
def load_tfidf(hotelids,data_path):
    hotel_data = pd.read_excel(data_path)
    hotel_data = hotel_data.drop(['replycount', 'adoptedreplyid', 'askreplyid', 'replycontent', 'datachange_lasttime'],
                                axis=1)
    grouped_alls = hotel_data.groupby('masterhotelid')
    for id in hotelids:
        for name_all, group_all in grouped_alls:
            if not name_all == int(id):
                continue
            hotel_group = group_all.groupby('askid')
            list_id = []
            ask_list = []
            for hotel_name, hotel_data in hotel_group:
                list_id.append(hotel_name)
                ask = str(hotel_data['asktitle'].iloc[0])
                unused = re.findall("#.*?#", ask)
                if len(unused) >0:
                    ask = ask.replace(unused[0], "")
                ask_list.append(ask)
            if len(ask_list) < 3:
                continue
            seg = Seg()
            ss = SentenceSimilarity(seg)
            ss.set_sentences(ask_list)
            ss.TfidfModel()  # tfidf模型
            id_map[id] = list_id
            model_map[id] = ss

def get_hotelids(data_path):
    hotel_data = pd.read_excel(data_path)
    grouped_alls = hotel_data.groupby('masterhotelid')
    hotelids = []
    for name_all, group_all in grouped_alls:
        hotelids.append(name_all)
    return hotelids

hotelids = get_hotelids(cfg.get('constant', 'ask_data_path'))
load_tfidf(hotelids,cfg.get('constant','ask_data_path'))
def get_idmap(hotelids):
    id_map = dict
    for id in hotelids:
        file_obj = FileObj(cfg.get('constant','ask_data_path'))
        id_map[id] = file_obj.read_hotel_data(id).get_id_list()
    return id_map

word2Vec = KeyedVectors.load_word2vec_format(cfg.get('model','word2vec_path'))
seg = Seg()

def get_similar_words(sentence,num):
    result_list = []
    sililar_list = []
    # 原始数据分词后结果
    cut_words = seg.cut_for_search(sentence)
    result_list.append(cut_words)
    for word in cut_words:
        # 通过学习找相似的词
        sililar_list.extend(word2Vec.most_similar(word,topn = num))
    result_list.append(sililar_list)
    # 返回 2个 list  原始数据分词结果 ， 和原始词意思相近的结果
    return result_list

def get_similar_sentence(sentence,hotelid,num):
    try:
        model_map[hotelid]
    except Exception:
        return []
    else:
        if model_map[hotelid] is None:
            return
        ss = model_map[hotelid]
        id_list = id_map[hotelid]
        sentence_index = ss.similarity(sentence,num)
        result_list = []
        for id in sentence_index:
            result_list.append(id_list[id])
        return result_list




