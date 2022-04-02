from waybackpy import WaybackMachineSaveAPI
import signal
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
url_list = [
    "https://api.cps.edu/health/help",
    "https://api.cps.edu/health/Help/Api/GET-cps-district2021weeklycovidactionable_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-cps-district2021dailycovidactionable_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-cps-school2021weeklycovidactionable_SchoolID_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-DistrictNoAdmittanceSummary_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-SchoolNoAdmittanceSummary_SchoolID_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-SchoolWeeklyCOVIDActionable_SchoolID_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-DistrictWeeklyCOVIDActionable_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-District2021WeeklyCOVIDTesting_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-District2021DailyCOVIDTesting_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-School2021DailyCOVIDActionable_SchoolID_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-SchoolDailyCOVIDSurveillance_SchoolID_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-NetworkDailyCOVIDSurveillance_NetworkName_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-DistrictDailyCOVIDSurveillance_StartDate_EndDate",
    "https://api.cps.edu/health/Help/Api/GET-CPS-SchoolCOVIDStudentVaccinationRate_SchoolID",
    "https://api.cps.edu/health/Help/Api/GET-CPS-DistrictCOVIDStudentVaccinationRate",
    "https://www.cps.edu/services-and-supports/covid-19-resources/covid-19-readiness-data/",
]

def handler(sigum, frame):
    raise Exception("Request Sent")

def lambda_handler(event, context):
    signal.signal(signal.SIGALRM, handler)

    for url in url_list:
        signal.alarm(5) # resets alarm
        try:
            save_api = WaybackMachineSaveAPI(url, user_agent)
            save_api.save()
        except Exception:
            logger.info("Request Sent: {}".format(url))
            continue
    