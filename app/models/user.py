from enum import Enum


class UserProperties(str, Enum):
    ACCOUNT_ENABLED = "accountEnabled"
    DISPLAY_NAME = "displayName"
    MAIL = "mail"
    MOBILE_PHONE = "mobilePhone"
    GIVEN_NAME = "givenName"
    CITY = "city"
    DEPARTMENT = "department"
    BUSINESS_PHONES = "businessPhones"
    OFFICE_LOCATION = "officeLocation"
    JOB_TITLE = "jobTitle"
    OTHER_MAILS = "otherMails"
