from datetime import datetime

date = lambda : datetime.now().strftime("%Y-%m-%d")
def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False