import json
from service import get_devices,get_device_data
def getDataEva(event, context):
    try:
        devices = get_devices()
        data=[]
        for device in devices:
            asset_type=device.get("asset_type", device.get("device"))  
            logs,metricas=get_device_data(device.get("device"),asset_type)
            data.append({
                "device_id" :device.get("device"),
                "asset_type" : asset_type,
                "logs":logs,
                "metricas":metricas,
                "connection" : device.get("connection"),
                })
    except:
        pass
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }

