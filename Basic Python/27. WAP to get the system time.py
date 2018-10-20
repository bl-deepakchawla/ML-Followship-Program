from datetime import datetime


def system_time():
    return datetime.utcnow()


result = system_time()
print("System Time is", result)
