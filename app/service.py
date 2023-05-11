import httpx
DEVICES_FILTERS = ["name:E2_"]
URL_DEVICES = "https://makesens.aws.thinger.io/v1/users/MakeSens/devices"
TOKEN_DEVICE = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJBbGxfZGV2aWNlcyIsInN2ciI6Im1ha2VzZW5zLmF3cy50aGluZ2VyLmlvIiwidXNyIjoiTWFrZVNlbnMifQ.zVWayH47ZcBWET-FjO5pR1vtkkVnPM3YDV121oAeJkk"
HEADERS_DEVICES = {"Authorization": "Bearer " + TOKEN_DEVICE}
BUCKET_URL_TEMPLATE = (
    "https://makesens.aws.thinger.io/v1/users/MakeSens/buckets/B{}/data?items=5"
)
TOKEN_BUCKET_DEVICES = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJBbGxfYnVja2V0cyIsInN2ciI6Im1ha2VzZW5zLmF3cy50aGluZ2VyLmlvIiwidXNyIjoiTWFrZVNlbnMifQ.Y7iXy0PKxJ0U6LM6tSdxUZVzpmGVjQLG596pjMD0cM4"
HEADERS_BUCKET_DEVICES = {"Authorization": "Bearer " + TOKEN_BUCKET_DEVICES}
def get_devices():
    url = URL_DEVICES + "?" + DEVICES_FILTERS[0]
    print(url)
    devices = httpx.get(url, headers=HEADERS_DEVICES).json()
    return devices

def process_device_data(device_data, device_id, asset_type):
    log = {
        "Dimensions": [
            {"Name": "deviceid", "Value": device_id},
            {"Name": "type_logs", "Value": "logs"},
        ]
    }
    metricas = {
        "Dimensions": [
            {"Name": "deviceid", "Value": device_id}
        ]
    }

    log_records, metric_records = [], []
    for data in device_data:
        ts = data["ts"]
        data_logs=[{"Name": "VBat" if key in ["Voltaje_Batería", "Voltaje_Bateria"] else str(key),"Value": str(data.get("val").get(key)),"Type": "DOUBLE"} for key in data.get('val') if key in ["RSSID","VBat","VIn","PGOOD","CHG","Voltaje_Batería","Voltaje_Bateria","Voltaje Bateria"] ]          
        data_metricas = [{"Name": "humedad"if key == "Humedad_Ambiente" else "humedad_suelo"if key == "Humedad_Suelo" else "temperatura" if key == "Temperatura_Ambiente" else "iluminancia"if key == "Iluminancia"else "presion"if key == "Presion_Ambiente"else str(key),"Value": str(data.get("val").get(key)),"Type": "DOUBLE"}for key in data.get('val') if key not in ["RSSID","VBat","VIn","PGOOD","CHG","Voltaje_Batería","Voltaje_Bateria","Voltaje Bateria"] ]
        if data_logs:
            log_records.append(
                {
                    "Time": str(int(ts)),
                    "Dimensions": log["Dimensions"],
                    "MeasureName": asset_type,
                    "MeasureValueType": "MULTI",
                    "MeasureValues": data_logs,
                }
            )
        if data_metricas:
            metric_records.append(
                {
                    "Time": str(int(ts)),
                    "Dimensions": metricas["Dimensions"],
                    "MeasureName": asset_type,
                    "MeasureValueType": "MULTI",
                    "MeasureValues": data_metricas,
                }
            )
    return log_records,metric_records

        


def get_device_data(device_id,asset_type):
    url = BUCKET_URL_TEMPLATE.format(device_id)
    response = httpx.get(url, headers=HEADERS_BUCKET_DEVICES, timeout=None)
    return process_device_data(response.json(),device_id,asset_type) if response.status_code == 200 else  None