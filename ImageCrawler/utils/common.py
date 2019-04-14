def get_dict(obj):
    res = {}
    if not obj:
        return None
    for item in obj.items():
        if item[0][0] is not '_':
            res.update({item[0]: item[1]})
    return res
