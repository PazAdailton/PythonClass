""""
when datetime doesn't UTC is called naive == not timezone
"""


from datetime import datetime, timezone, timedelta

print(datetime.now())
print(datetime.now(timezone.utc)) #always do in this format

today = datetime.now(timezone.utc)

tomorrow = today + timedelta(days=1)
print(f"today: {today}")
print(f"tomorrow: {tomorrow}")