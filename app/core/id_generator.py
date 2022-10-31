ELEMENTS_DICT = {
    "floor": "EL001",
    "wall": "EL002",
    "door": "EL003",
    "window": "EL004"
}


def generate_id(id_type: str, *args):
    if id_type == "floor":
        fl_no = args[0]
        fl_id = ("N" + str(abs(fl_no)).zfill(3)) if fl_no < 0 else ("P" + str(fl_no).zfill(3))
        return "F" + fl_id
    elif id_type == "element":
        return "EL" + "001"
    else:
        return "UNK" + "001"
