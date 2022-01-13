from datetime import datetime,  timezone


def Timestamp() -> int:
    dt = datetime.now()
    timestamp = int(round(dt.replace(tzinfo=timezone.utc).timestamp()*1000))
    return timestamp
