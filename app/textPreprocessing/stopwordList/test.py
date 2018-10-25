import app.textPreprocessing.text_processing_utils as utils
import os
print(utils.get_similar_sentence('酒店有没早餐',345078,3))
print(utils.get_similar_words('酒店有没早餐',3))
print(os.path.exists('E:/hackson/csearch/app/textPreprocessing/stopwordList/stopword.txt'))