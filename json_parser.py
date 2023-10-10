import json


def find_values(json_str, target_key):
    """
    Парсит JSON и возвращает все значения для заданного ключа.
    json_str: строка с JSON для парсинга
    target_key: ключ, который нужно найти
    """

    def extract_values(obj, key):
        arr = []

        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    arr.append(v)
                arr += extract_values(v, key)
        elif isinstance(obj, list):
            for item in obj:
                arr += extract_values(item, key)
        return arr

    try:
        data = json.loads(json_str)
        return extract_values(data, target_key)
    except json.JSONDecodeError:
        return []
