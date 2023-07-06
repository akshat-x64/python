import time



# import win10toast
from win10toast import ToastNotifier

# create an object to ToastNotifier class
n = ToastNotifier()



while True:

    n.show_toast("GEEKSFORGEEKS", "Drink_Water", duration = 5,
    icon_path ="download.jpeg")

    time.sleep(5)
