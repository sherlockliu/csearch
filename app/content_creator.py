from attrdict import AttrDict


def room_basic_info_creator(data: [AttrDict]):
    if not data:
        return ""
    prefix = "酒店房型："
    formatstring = "{index}. {room_name}, 面积为{room_area}平方米，位于{room_floor}层，{has_window}窗户"
    description_list = []
    for index, item in enumerate(data, 1):
        description_list.append(formatstring.format(index=index,
                                                room_name=item.room_name,
                                                room_area=item.room_area,
                                                room_floor=item.room_floor,
                                                has_window="有" if item.room_has_window == 2 else "无"
                                                ))
    return prefix + "；".join(description_list)

def room_facility_info_creator(data: [AttrDict]):
    if not data:
        return ""
    prefix = "酒店房间内设施："
    formatstring = "{index}. {facility_name}"
    description_list = set()
    for index, item in enumerate(data, 1):
        description_list.add(formatstring.format(index=index,
                                               facility_name=item.room_facility_name
                                               ))
    return prefix + "；".join(description_list)

creator_dict = {
    "room_basic_info": room_basic_info_creator,
    "room_facility_info": room_facility_info_creator,
    # "hotel_facility_info": hotel_facility_info_creator,
    # "pet_child_policy": pet_child_policy_creator,
    # "arrival_leaving": arrival_leaving_policy_creator,
    # "payment_card": payment_card_creator,
    # "poi_info": poi_creator
}
