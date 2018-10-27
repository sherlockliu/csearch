import app.framework.textPreprocessing.text_processing_utils as utils
# from app.framework.textPreprocessing.text_processing_utils import get_pinyin_words, get_least_levenshtein
import os

from data import get_file_path

print(utils.get_similar_sentence('酒店有没早餐',345078,3))
print(utils.get_similar_words('酒店有没早餐',3))
print(utils.get_pinyin_words('方形'))
print(utils.get_least_levenshtein('房性'))