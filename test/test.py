import app.framework.textPreprocessing.text_processing_utils as utils
import os

from data import get_file_path

print(utils.get_similar_sentence('酒店有没早餐',345078,3))
print(utils.get_similar_words('酒店有没早餐',3))
print(os.path.exists(get_file_path('stopword.txt', folder='stopwordList')))