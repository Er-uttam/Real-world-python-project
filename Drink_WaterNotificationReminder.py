import time
from plyer import notification


if __name__ == "__main__":
    while True:
     notification.notify(
         title = "**Plese Drink Water Now!",
         message = "Drinking water is vital for health as it regulates body functions, aids digestion, flushes out toxins, and promotes overall well-being.",
         app_icon = "E:\Real world python project\icon.ico",
         timeout = 10

    )
     time.sleep(60*60)
     