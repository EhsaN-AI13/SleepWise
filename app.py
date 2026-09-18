# تبدیل زمان به دقیقه
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


def time_to_minutes(time):
    parts = time.split(":")
    hour = int(parts[0])
    minute = int(parts[1])

    return hour * 60 + minute


# تبدیل دقیقه به زمان
def minutes_to_time(minutes):
    hour = minutes // 60
    minute = minutes % 60

    return f"{hour:02d}:{minute:02d}"


def calculate_time(minutes, hours):
    return (minutes + hours * 60) % (24 * 60)


def is_previous_day(minutes, hours):
    return minutes + hours * 60 < 0


def is_valid_time(time):
    parts = time.split(":")

    if len(parts) != 2:
        return False

    try:
        hour = int(parts[0])
        minute = int(parts[1])
    except ValueError:
        return False

    if hour < 0 or hour > 23:
        return False

    if minute < 0 or minute > 59:
        return False

    return True

# محاسبه زمان خواب و تشخیص شب قبل


def get_sleep_time(wake_minutes, hours):
    previous_day = wake_minutes - hours * 60

    sleep_minutes = calculate_time(wake_minutes, -hours)
    sleep_time = minutes_to_time(sleep_minutes)

    return sleep_time, previous_day < 0


def get_wake_time(sleep_minutes, hours):
    wake_minutes = calculate_time(sleep_minutes, hours)
    wake_time = minutes_to_time(wake_minutes)

    return wake_time


def calculate_wake_times(sleep_time):

    sleep_minutes = time_to_minutes(sleep_time)

    wake_7_time = get_wake_time(sleep_minutes, 7)

    wake_8_time = get_wake_time(sleep_minutes, 8)

    return wake_7_time, wake_8_time


def calculate_sleep_times(wake_time):

    wake_minutes = time_to_minutes(wake_time)

    sleep_7_time, sleep_7_previous = get_sleep_time(wake_minutes, 7)

    sleep_8_time, sleep_8_previous = get_sleep_time(wake_minutes, 8)

    return (
        sleep_7_time,
        sleep_7_previous,
        sleep_8_time,
        sleep_8_previous
    )


app = FastAPI()
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/calculate")
def calculate(mode: str, time: str):

    if not is_valid_time(time):
        return {
            "error": "زمان وارد شده نامعتبر است."
        }

    if mode == "sleep":

        wake_7_time, wake_8_time = calculate_wake_times(time)

        return {
            "mode": "sleep",
            "time": time,
            "result_7": wake_7_time,
            "result_8": wake_8_time
        }

    elif mode == "wake":

        sleep_7_time, sleep_7_previous, sleep_8_time, sleep_8_previous = calculate_sleep_times(time)

        return {
            "mode": "wake",
            "time": time,
            "result_7": sleep_7_time,
            "result_7_previous": sleep_7_previous,
            "result_8": sleep_8_time,
            "result_8_previous": sleep_8_previous
        }

    return {
        "error": "حالت انتخاب شده نامعتبر است."
    }
