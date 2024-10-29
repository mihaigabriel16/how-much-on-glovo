import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL_GLOVO = "https://api.glovoapp.com/v3/customer/orders-list?offset={0}&limit=100"
BASE_URL_PRESTO = "https://api.presto-pizza.ro/api/v2/get_history"
BASE_URL_TAZZ = "https://tazz.ro/account/orders"
BASE_URL_BOLT = "https://deliveryuser.live.boltsvc.net/deliveryClient/getOrderHistory"
BASE_URL_JERRYS = "https://app.jerryspizza.ro/api2/index.php/order/all?id={0}"


GLOVO_AUTH_TOKEN = os.getenv("GLOVO_AUTH_TOKEN")
TAZZ_COOKIE = os.getenv("TAZZ_COOKIE")
PRESTO_AUTH_UUID = os.getenv("PRESTO_AUTH_UUID")
BOLT_AUTH_TOKEN = os.getenv("BOLT_AUTH_TOKEN")
JERRYS_AUTH_TOKEN = os.getenv("JERRYS_AUTH_TOKEN")
JERRYS_X_API_KEY = os.getenv("JERRYS_X_API_KEY")
