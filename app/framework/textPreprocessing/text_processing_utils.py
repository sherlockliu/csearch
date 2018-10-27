from app.framework.textPreprocessing.zhcnSegment import *
from gensim.models import KeyedVectors
from app.framework.textPreprocessing import config as cfg
from app.framework.textPreprocessing.sentenceSimilarity import SentenceSimilarity
from app.framework.textPreprocessing.fileObject import FileObj
from xpinyin import Pinyin
import pandas as pd
import re
model_map = {}
id_map = {}
pinyin = Pinyin()
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
def load_pinyin_map():
    highFrequencySearchMap = {}
    for word in cfg.get_highFrequencySearch():
        highFrequencySearchMap[pinyin.get_pinyin(word,"")] = word
    return highFrequencySearchMap

highFrequencySearchMap =load_pinyin_map()

hotelids = get_hotelids(cfg.get('constant', 'ask_data_path'))
load_tfidf(hotelids,cfg.get('constant','ask_data_path'))
def get_idmap(hotelids):
    id_map = {}
    for id in hotelids:
        file_obj = FileObj(cfg.get('constant','ask_data_path'))
        id_map[id] = file_obj.read_hotel_data(id).get_id_list()
    return id_map

word2Vec = KeyedVectors.load_word2vec_format(cfg.get('model','word2vec_path'))
seg = Seg()


def levenshtein(s, t):
    if s == t:
        return 0
    elif len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(t)]

def get_similar_words(sentence,num):
    if len(sentence) <= 3:
        return [[sentence],[]]
    result_list = []
    sililar_list = []
    # 原始数据分词后结果
    cut_words = seg.cut(sentence)
    result_list.append(cut_words)
    for word in cut_words:
        # 通过学习找相似的词
        sililar_list.extend(word2Vec.most_similar(word,topn = num))
    result_list.append(sililar_list)
    # 返回 2个 list  原始数据分词结果 ， 和原始词意思相近的结果
    return result_list
#hotelid  为数字类型
def get_similar_sentence(sentence,hotelid,num):
    try:
        model_map[int(hotelid)]
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

def get_pinyin_words(words):
    try:
       result = highFrequencySearchMap[pinyin.get_pinyin(words,"")]
    except Exception:
        return ""
    else:
        return result
def get_least_levenshtein(word,minDistance = 1):

    for highFrequency in cfg.get_highFrequencySearch():
        tmpDistance = levenshtein(highFrequency,word)
        if tmpDistance <= minDistance:
            return highFrequency
    return ''





