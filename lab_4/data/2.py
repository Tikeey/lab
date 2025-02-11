from datetime import datetime, timedelta

current_date = datetime.today()

tomorrow_date = current_date + timedelta(days=1)

yesterday_date = current_date - timedelta(days=1)

print("Current Date:", current_date.strftime("%Y-%m-%d"))

print("Tomorrow Date: ", tomorrow_date.strftime("%Y-%m-%d"))

print("Yesterday Date: ", yesterday_date.strftime("%Y-%m-%d"))