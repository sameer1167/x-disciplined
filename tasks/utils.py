# # tasks/utils.py
# import pytz
# from django.utils import timezone


# #conversion 
# def convert_user_time_to_utc(local_dt, user_tz_str):
#     user_tz = pytz.timezone(user_tz_str)
#     localized = user_tz.localize(local_dt)
#     return localized.astimezone(pytz.utc)

# def convert_utc_to_user_time(utc_dt, user_tz_str):
#     user_tz = pytz.timezone(user_tz_str)
#     return utc_dt.astimezone(user_tz)