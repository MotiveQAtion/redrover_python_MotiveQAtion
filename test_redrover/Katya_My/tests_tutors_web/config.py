from dotenv import load_dotenv
import os
# Принудительно игнорировать системные переменные(не очень)
# load_dotenv(override=True)

load_dotenv()

WEB_USERNAME = os.getenv("WEB_USERNAME")
WEB_PASSWORD = os.getenv("WEB_PASSWORD")

T_NAME = os.getenv("TUTOR_NAME")
T_PASSWORD = os.getenv("TUTOR_PASSWORD")