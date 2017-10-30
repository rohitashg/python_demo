# coding=utf-8
from django.core.validators import RegexValidator
# message define dictionary
email_from_name = "RETI"
status_key = {}
status_key = {'request_send':3}
message_key = {}

email_subject = {
                1: "Confirm your email",
                2: "Forgot your email",
                3: "Property Invite",
                4: "Admin account has been removed.",
                5: "Remove from Property.",
                6: "Property Delete",
                7: "Event Invite",
                8: "Event Updated",
                9: "Event Deleted",
                10: "Removed from Event",
                11: "RETI Pre-Registration Confirmed"
                 }

push_message = {
    1: "Remove from Property.",
    2: "Property Request Accepted",
    3: "Property Request Rejected"
}

delete_msg = " has been deleted successfully."

common_msg = {1:"Your feedback has been successfully ", 2: "Offer has been successfully "}

message_key = {1: "We couldn't find your account.",
               2: "Enter Valid Password.",
               3: "Sign in Successfully.",
               4: "Your account has been successfully created.",
               5: "Please provide valid token.",
               6: "Token Missing.",
               7: "Your email has been sent successfully    .",
               8: "Your email has not been sent.",
               9: "Requested user not found.",
               10: "Token authentication error.",
               11: "Sign out successfully.",
               12: "Current Password does not match.",
               13: "Password has been changed successfully.",
               14: "Sorry! Your password has not been changed.",
               15: "User profile data.",
               16: "OTP has been sent to your registered Mobile number.",
               17: "An error has occurred while sending the OTP.",
               18: "Try sending an SMS containing only 'RETI' to ",
               19: "This field may not be blank.",
               20: "Your phone verification has been done successfully.",
               21: "Please provide valid code.",
               22: "Only numbers are allowed.",
               23: "Your email ID has been successfully veriﬁed. You can now receive notiﬁcations on your registered email ID.",
               24: "Your email ID has been already verified. You can now receive notiﬁcations on your registered email ID.",
               25: "Your Profile Details have been successfully updated!",
               26: "Email has been sent to your registered email ID.",
               27: "Your mobile number has been already verified.",
               28: "Please enter valid mobile no.",
               29: "Please enter valid Email Id.",
               30: "Please enter valid Email/Mobile no.",
               31: "Invalid User-ID",
               32: "Email field is required.",
               33: "Code has been sent to your registered Mobile number and will expires within 30 minutes.",
               34: "There are some error for sending message on your register mobile number. please try after some time.",
               35: "There are some error for sending email on your register email. please try after some time.",
               36: "Code has been sent to your registered email Id and will expires within 30 minutes.",
               37: " as your 4-digit code to reset your password.",
               38: "Please provide valid state.",
               39: "forgot_code field is required",
               40: "Great! You have successfully rest your password.",
               41: "Please provide valid code.",
               42: "Code verified successfully.",
               43: " wants to add you on a property Accept the invite to become a Seller on this property",
               44: " wants to add you on a property Accept the invite to become a Agent on this property",
               45: "Your email ID is not verify.",
               46: "Email ID is already registered.",
               47: "Mobile number is already registered.",
               48: "Please provide valid property.",
               49: "You are not valid user for edit this property.",
               50: "You are not valid user for delete this property.",
               51: "Property not found.",
               52: "Request success.",
               53: 'Record Not found.',
               54: " has been removed from property",
               55: " has sent you an invitation for",
               56: " has assigned you as ",
               57: " has assign you as ",
               58: " has remove you as ",
               59: " has removed you as ",
               60: "Please provide id",
               61: "Notification has been deleted successfully.",
               62: "Please provide valid date.",
               63: "Representation end date should be greater than start date.",
               64: "Total fee amount should be less than sale price amount.",
               65: "Email not verified yet.",
               66: "Price should be greater than Gross Income & Net Income.",
               67: "Record Not found.",
               68: "Please enter valid Agent Email Id.",
               69: "Please enter valid Agent mobile no.",
               70: "please enter valid Agent fee percentage.",
               71: "Please enter valid Seller Email Id.",
               72: "Please enter valid Seller mobile no.",
               73: "Only characters are allowed.",
               74: "Minimum 2 characters are allowed.",
               75: "Maximum 20 characters are allowed.",
               76: "Please provide valid fee percentage.",
               77: "Characters limit is ",
               78: "Please provide valid zipcode.",
               79: "Please provide valid state.",
               80: "limit is 50.",
               81: "Property Price amount should be greater than or equal to 1.",
               82: " should no more than 2 decimal places.",
               83: "Please provide fee percentage. minimum fee percentage should be 0.01",
               84: "You have already created Admin Account.",
               85: "Admin account has been created successfully.",
               86: "Admin dashboard should be True or False.",
               87: "Admin account has been removed successfully.",
               88: "Invalid file.Only jpg, jpeg, png image files allowed.",
               89: "Logo has been uploaded successfully.",
               90: "Logo has been removed successfully.",
               91: "Profile image has been uploaded successfully.",
               92: "Profile image has been removed successfully.",
               93: "Admin account has been updated successfully.",
               94: "Please provide valid data.",
               95: "Your Admin account has been removed successfully.",
               96: "You can not do this event because you are admin.",
               97: " has removed you from a property as a seller on this property.",
               98: " has removed you from a property as an agent on this property.",
               99: "Property request has been successfully accepted.",
               100: "Property request has been successfully rejected.",
               101: "First Name cannot be left empty.",
               102: "Last Name cannot be left empty.",
               103: "Mobile Number cannot be left empty.",
               104: "Address cannot be left empty.",
               105: "We have removed the property from your list.",
               106: " has deleted this property ",
               107: " has accepted your invitation as a seller.",
               108: " has rejected your property invitation as a seller.",
               109: " invites you as ",
               110: "Please provide valid property.",
               111: "Your event has been successfully created!",
               112: " name should not exceed 100 characters.",  # used for validation
               113: "Please enter valid attendees Email Id.",
               114: "Please provide valid start time & end time.",
               115: "You are not authorized user to create event for this property.",
               116: "Please provide other event name.",
               117: "Please provide event.",
               118: "Event has been deleted successfully.",
               119: " has invited you to an event.",  # this is used for notification message
               120: " should not exceed 500 characters.",  # used for validation
               121: " name should not exceed 30 characters.",  # used for validation,
               122: "Your event has been successfully updated!",
               123: " has updated event.",
               124: "Please provide event id.",
               125: "Please provide valid property.",
               126: "Your marketing detail has been successfully ",
               127 : "You are not authorized to access this.",
               128 : " has deleted event.",
               129: "You can not edit past event.",
               130: " has removed you from an event.",
               131: "created!",
               132: "updated!",
               133: "Event duration time limit should be atleast 15 minutes.",
               134: "Your account is not active. Please contact to RETI Admin.",
               135: common_msg[1] + "submitted!",
               136: "Please provide valid property event.",
               137: "Your feedback has been already submitted.",
               138: "You can not submit feedback before complete this event.",
               139: "Please provide rating.",
               140: "Feedback" + delete_msg,
               141: common_msg[1] + "updated!",
               142: common_msg[2] + "Created.",
               143: "Rating should be less than or equal to 5.",
               144: "Offer" + delete_msg,
               145: "Offer has been reset successfully."
               }

property_status = {
    1: "Do you want to continue with the Marketing Details?",  # this message for properties
    2: "Please add contract under this property.",  # This message related to properties
    3: "",
    4: ""
}
web_message ={
    1: "Please select property type",
    2: "Please select property status",
    3: "Please select state",
    4: "Street Address can not blank",
    5: "City name can not blank",
    6: "Zip code can not blank",
    7: "Price can not blank",
}
source_type = {
    'property':1,
    'tour':2,
}
# RegexValidator define for sign-up & login
alphabetChar = RegexValidator(r'^[a-z A-Z]*$', "Only characters are allowed.")

alphaNumericChar = RegexValidator(r'^[a-zA-Z0-9 ]+$', "Only alpha numeric are allowed.")

rulePassword = RegexValidator(r'^(?=.*[a-z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]*$',"Minimum 6 characters atleast 1 Alphabet"+\
                              ", 1 Number and 1 Special Character.")

phoneNumber =  RegexValidator(r'^[0-9]*$', "Only numbers are allowed.")
zipCode = RegexValidator(r'^\d{6}$', "Enter valid zip code.")

email_validation =  RegexValidator(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", "Please enter valid email address.")
email_regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
mobile_regx = "^[0-9]{10,10}$"
number_check = "^[0-9]+$"
decimal_number_check = "^(?=.*?\d)\d*[.]?\d*$"
alphabetChar_check = "^[a-z A-Z]*$"
alphanumeric_check = '^[a-zA-Z0-9 ]+$'
#default image for property
DEFAULT_PROPERTY_IMAGE = 'c59735901ddb4c93a198905bd323e00d.jpeg'
#DEFAULT_PROPERTY_IMAGE = '908d0de2873b4e0eaa26dc7c9af5e7f2.jpeg'

DEFAULT_PAGE = 1

DEFAULT_PER_PAGE = 20

DEFAULT_PER_PAGE_EVENT = 100

DATE_TIME_FORMATE = "%Y-%m-%d %H:%M:%S"

TIME_FORMATE = "%H:%M:%S"

TIME_FORMATE_VIEW = "%I:%M %p"

DATE_FORMATE = "%Y-%m-%d"

DATE_FORMATE_VIEW = "%b %d, %Y"

PHONE_CODE = '+91'

ITUNE_LINK = "https://www.apple.com/itunes"

PLAY_STORE_LINK = "https://play.google.com"

ASSIGN_AGENT = 'agent'

ASSIGN_SELLER = 'seller'

LOT_SIZES_UNIT = (
    ('sf', 'Square Foot'),
    ('acre', 'Acres'),
)

PROPERTY_NUMBER_DATA_KEY = ['sale_price', 'sale_cap_rate', 'gross_income', 'net_income', 'price_per_unit', 'price_per_sf',
                  'occupancy', 'building_size', 'lot_size', 'year_built', 'total_fee', 'fee_percentage' , 'portfolio_listing',
                  'latitude', 'longitude']

PORTFOLIO_LIMIT = 50

DURATION_LIMIT = 15

# set source type for event feedback send
FEEDBACK_SOURCE_TYPE = 2

CAMPAIGN_FEEDBACK_SOURCE_TYPE = 1

FEEDBACK_END_MINUTE = 1

FEEDBACK_SECOND = 60

ADMIN_REDIRECT_URL = '/administrator/user_dashboard'

SITE_REDIRECT_URL = '/property/properties'