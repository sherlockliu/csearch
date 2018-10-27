import xlrd
from attrdict import AttrDict

from app.framework.elastic_search_client import ElasticSearchClient

base_path = "../data/{}.xlsx"
base_index = "hotel_{}"
file_name_list = [
    "0 酒店及对应id",
    # "1 大家问",
    # "2 点评",
    "3 酒店房型设施",
    "4 酒店设施服务",
    "5 酒店政策",
    "6 酒店驾车步行信息"
]


class Preload:
    def __init__(self):
        self.es_client = ElasticSearchClient()

    def preload_file_list(self):
        try:
            for file_name in file_name_list:
                file = xlrd.open_workbook(base_path.format(file_name))
                for sheet in file.sheets():
                    try:
                        field_name_list = sheet.row_values(0)
                        factory = RowDictFactory(field_name_list)

                        if sheet_handler_dict.get(sheet.name):
                            handler = sheet_handler_dict[sheet.name]
                        else:
                            print(f"Corresponding handler of {sheet.name} doesn't exist.")
                            continue

                        for index in range(1, sheet.nrows):
                            doc_body = handler(factory.create_row_dict(sheet.row_values(index)))
                            if doc_body:
                                doc_body['info_type'] = sheet.name
                                self.es_client.create(base_index.format(file_name).replace(' ', ''),
                                                      "hotel_info", doc_body)
                    except Exception as e:
                        continue
        except Exception as e:
            print(e)


class RowDictFactory:
    def __init__(self, key_list: list):
        self.key_list = [key for key in key_list if key]

    def create_row_dict(self, value_list):
        row_dict = AttrDict()
        for index, key in enumerate(self.key_list):
            row_dict[key] = value_list[index]

        return row_dict


def qa_handler(row_dict: AttrDict):
    if not row_dict.masterhotelid:
        return
    return {
        "hotel_id": str(int(row_dict.masterhotelid)),
        "question_id": str(int(row_dict.askid)),
        "question": row_dict.asktitle,
        "answer": row_dict.replycontent
    }


def comments_handler(row_dict: AttrDict):
    if (row_dict.writingtype > 2  # 过滤酒店点评反馈
        or row_dict.contentstatus != 'T'
        or row_dict.status != 'T'
        or not row_dict.resource):
        return
    return {
        "hotel_id": str(int(row_dict.resource)),
        "comment_title": row_dict.writingtitle,
        "comment_content": row_dict.writingcontent,
    }


def room_basic_info_handler(row_dict: AttrDict):
    if not row_dict.hotel:
        return
    return {
        "hotel_id": str(int(row_dict.hotel)),
        "room_name": row_dict.roomname,
        "room_area": str(row_dict.arearange),
        "room_floor": row_dict.floorrange,
        "room_has_window": row_dict.haswindow  # "有窗户" if row_dict.haswindow == 2 else "无窗户"
    }


def room_facility_info_handler(row_dict: AttrDict):
    if not row_dict.hotel:
        return
    return {
        "hotel_id": str(int(row_dict.hotel)),
        "room_facility_name": row_dict.name
    }


def hotel_facility_info_handler(row_dict: AttrDict):
    if not row_dict.hotel:
        return
    return {
        "hotel_id": str(int(row_dict.hotel)),
        "hotel_facility_name": row_dict.facilityname
    }


def pet_child_policy_handler(row_dict: AttrDict):
    if not row_dict.hotelid:
        return
    return {
        "hotel_id": str(int(row_dict.hotelid)),
        # "允许携带宠物" if row_dict.ispetsallowed == 'T' else "不允许携带宠物",
        "is_pets_allowed": row_dict.ispetsallowed,
        # "收取宠物费" if row_dict.haspetsfee == 'T' else ("不收取宠物费" if row_dict.haspetsfee == 'F' else ""),
        "has_pets_fee": row_dict.haspetsfee,
        # "可携带儿童入住" if row_dict.allowaccomchd == 'T' else "不可携带儿童入住",
        "chd_allowed ": row_dict.allowaccomchd,
        # "可使用现有床位" if row_dict.allowusingexgbed == 'T' else "不可使用现有床位",
        "using_exist_bed_allowed": row_dict.allowusingexgbed,
        "limit_of_chd_on_exist_bed": row_dict.limitofchdonexgbed,
        "range_type": row_dict.rangetype,
        "range_from_on_exg_bed": row_dict.rangefromonexgbed,
        "range_to_on_exg_bed": row_dict.rangetoonexgbed
    }


def arrival_policy_handler(row_dict: AttrDict):
    if not row_dict.hotelid:
        return
    return {
        "hotel_id": str(int(row_dict.hotelid)),
        "arrival_from": row_dict.arrivalfrom,
        "arrival_to": row_dict.arrivalto
    }


def payment_card_handler(row_dict: AttrDict):
    if row_dict.active != 'T' or not row_dict.hotel:
        return
    return {
        "hotel_id": str(int(row_dict.hotel)),
        "credit_card_name": row_dict.creditcardname,
        "credit_card_ename": row_dict.creditcardename,
    }


def notification_handler(row_dict: AttrDict):
    # if row_dict.status != 'T' or row_dict.isdel != 'F'
    #     or row_dict.is
    pass


def poi_handler(row_dict: AttrDict):
    if not row_dict.hotelid:
        return
    return {
        "hotel_id": str(int(row_dict.hotelid)),
        "line_distance": row_dict.linedistance,
        "drive_distance": row_dict.drivedistance,
        "drive_duration": row_dict.driveduration,
        "walk_distance": row_dict.walkdistance,
        "walk_duration": row_dict.walkduration,
        "poi_name": row_dict.POIname,
        "poi_type": row_dict.poitype
    }

def hotel_name_handler(row_dict:AttrDict):
    if not row_dict.id:
        return
    return {
        "hotel_id": str(int(row_dict.id)),
        "hotel_name": row_dict.HotelName.strip()
    }

sheet_handler_dict = {
    "HotelName": hotel_name_handler,
    "Q&A": qa_handler,
    "点评": comments_handler,
    "面积楼层是否有窗户": room_basic_info_handler,
    "具体房型设施": room_facility_info_handler,
    "酒店设施": hotel_facility_info_handler,
    "宠物、儿童政策": pet_child_policy_handler,
    "入离时间": arrival_policy_handler,
    "酒店可用银行卡": payment_card_handler,
    "驾车步行": poi_handler
}

# Preload().preload_file_list()
try:
    allres = Preload().es_client.search_all()
    print(allres)
except Exception as e:
    pass