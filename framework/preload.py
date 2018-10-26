import xlrd
from attrdict import AttrDict

from framework.elastic_search_client import ElasticSearchClient

base_path = "../data/{file_name}.xlsx"
base_index = "hotel_{}"
file_name_list = [
    "0 酒店及对应id",
    "1 大家问",
    "2 点评",
    "3 酒店房型设施",
    "4 酒店设施服务",
    "5 酒店政策",
    "6 酒店驾车步行信息"]

es_client = ElasticSearchClient()


class Preload:
    @staticmethod
    def preload_file_list():
        try:
            for file_name in file_name_list:
                file = xlrd.open_workbook(base_path.format(file_name))
                for sheet in file.sheets():
                    field_name_list = sheet.row_values(0)
                    factory = RowDictFactory(field_name_list)

                    for index in range(1, sheet.nrows):
                        if sheet_handler_dict.get(sheet.name):
                            doc_body = sheet_handler_dict[sheet.name](
                                factory.create_row_dict(field_name_list.row_values(index)))
                            es_client.create(base_index.format(file_name), sheet.name, doc_body)
                        else:
                            raise ValueError(f"Corresponding handler of {sheet.name} doesn't exist.")
        except Exception as e:
            print(e)


class RowDictFactory:
    def __init__(self, key_list: list):
        self.key_list = key_list

    def create_row_dict(self, value_list):
        row_dict = AttrDict()
        for index, key in enumerate(self.key_list):
            row_dict[key] = value_list[index]

        return row_dict


def qa_handler(row_dict: AttrDict) -> dict:
    body = {
        "hotel_id": row_dict.masterhotelid,
        "question": row_dict.asktitle,
        "answer": row_dict.replycontent
    }

    return body


def comments_handler(row_dict: AttrDict):
    if (row_dict.writingtype > 2  # 过滤酒店点评反馈
        and row_dict.contentstatus == 'T'
        and row_dict.status == 'T'):
        return
    body = {
        "hotel_id": row_dict.resource,
        "comment_title": row_dict.writingtitle,
        "comment_content": row_dict.writingcontent,
    }
    return body

def room_basic_info_handler(row_dict: AttrDict):
    body = {
        "hotel_id": row_dict.hotel,
        "room_name": row_dict.roomname,
        "room_area": row_dict.arearange,
        "room_floor": row_dict.floorrange,
        "room_has_window": "有窗户" if row_dict.haswindow == 2 else "无窗户"
    }
    return body

def room_facility_info_handler(row_dict: AttrDict):
    body = {
        "hotel_id": row_dict.hotel,
        "room_facility_name": row_dict.name
    }
    return body

def hotel_facility_info_handler(row_dict: AttrDict):
    body = {
        "hotel_id": row_dict.hotel,
        "hotel_facility_name": row_dict.facilityname
    }
    return body

def pet_child_policy_handler(row_dict: AttrDict):
    body = {
        "hotel_id": row_dict.hotelid,
        "is_pets_allowed": "允许携带宠物" if row_dict.ispetsallowed == 'T' else "不允许携带宠物",
        "has_pets_fee": "收取宠物费" if row_dict.haspetsfee == 'T' else ("不收取宠物费" if row_dict.haspetsfee == 'F' else ""),
        "chd_allowed ": "可携带儿童入住" if row_dict.allowaccomchd == 'T' else "不可携带儿童入住",
        "using_exist_bed_allowed": "可使用现有床位" if row_dict.allowusingexgbed == 'T' else "不可使用现有床位",
        "limit_of_chd_on_exist_bed": row_dict.limitofchdonexgbed,
        "range_type": row_dict.rangetype,
        "range_from_on_exg_bed": row_dict.rangefromonexgbed,
        "range_to_on_exg_bed": row_dict.rangetoonexgbed
    }
    return body

sheet_handler_dict = {
    "Q&A": qa_handler,
    "点评": comments_handler,
    "面积楼层是否有窗户": room_basic_info_handler
}
