from datetime import datetime,  timezone
dt = datetime.now()
timestamp = int(round(dt.replace(tzinfo=timezone.utc).timestamp()*1000))
