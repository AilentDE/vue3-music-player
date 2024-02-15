from bson import ObjectId

async def convert_object_id_to_str(data):
    if isinstance(data, list):
        return [await convert_object_id_to_str(item) for item in data]
    elif isinstance(data, dict):
        if '_id' in data:
            data['id'] = str(data.pop('_id'))
        return {key: await convert_object_id_to_str(value) for key, value in data.items()}
    elif isinstance(data, ObjectId):
        return str(data)
    else:
        return data
        