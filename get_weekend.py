from datetime import datetime, timedelta

def getNextWeekend():
    # Get the current time in UTC
    now = datetime.now()

    # Calculate the number of days until Saturday (weekday 5 in Python: Monday=0, Sunday=6)
    days_until_saturday = (5 - now.weekday()) % 7
    saturday = now + timedelta(days=days_until_saturday)

    # If today is Saturday, the weekend is already happening
    if now.weekday() == 5:
        saturday = now
    
    # Set the start time to 00:00:00 on Saturday
    start_of_weekend = saturday.replace(hour=0, minute=0, second=0, microsecond=0)

    # Calculate the end of the weekend, which is 23:59:59 on Sunday
    end_of_weekend = start_of_weekend + timedelta(days=1, hours=23, minutes=59, seconds=59)

    # Format the start and end times in ISO 8601 format
    startDateTime = start_of_weekend.strftime("%Y-%m-%dT%H:%M:%SZ")
    endDateTime = end_of_weekend.strftime("%Y-%m-%dT%H:%M:%SZ")

    return startDateTime, endDateTime