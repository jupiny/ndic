
def parse_zh_json(zh_json):
    """

    :param zh_json:
    :return:
    """

    if type(zh_json) not in (dict, ):
        raise ValueError(
            "parse_zh_json() got wrong parameter zh_json"
            "expected dict type but got {} type".format(type(zh_json))
        )

    items = zh_json["searchResults"]["searchEntryList"]["items"]

    ret = []
    for item in items:
        card = {
            "entryNameTTS" : item["entryNameTTS"],
            "meanList": [
                {
                    "meaning": mean["mean"],
                    "poomsa": mean["partsLabel"]
                }
                for mean in item["meanList"]
            ],
            "pinyin": item["pinyin"],
        }
        ret.append(card)

    return ret
