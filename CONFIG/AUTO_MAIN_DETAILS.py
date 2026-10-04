#############-->Model Type 0- OLD MODEL 1-NEW MODEL<--##############
MODEL_TYPE=1

#############-->succes result code<--################
RESULT_CODE=0

#############-->Enter the DUT release name<--################
AUTO_REL= "CPaas-1.0.0.0"

#############-->Enter the DUT revision<--################
AUTO_REV="Rev0"
APP_BINARY= "Cpass"
APP_AUTOLOGPATH= "/opt/product/testteam/Products/PPGW/SPRINT_1.0_P2/bin/LOGGER"


#############-->SSH Key Path<--################
####ID_RSA= "/opt/product/AUTOMATION/.ssh/id_rsa"
ID_RSA= "/root/.ssh/id_rsa"
#############-->>Enter Automation Result Path<<---##########################
RESULT_LOGPATH= "/opt/product/AUTOMATION/AUTOMATION_RESULTS/CPAAS/RESULTS"

TIMESTAMP_FILE_PATH = "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/"

AUTOMATION_PATH = "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/"
AUTOMATION_TEMP_PATH="/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/TEMP/"
AUTOMATION_FAILPATH = "/opt/product/AUTOMATION/AUTOMATION_RESULTS/CPAAS/FAILURE_LOGS"
AUTOMATION_RESULT_PATH= "/opt/product/AUTOMATION/AUTOMATION_RESULTS/CPAAS/"

INPUT_HIERARCHY = 1

PRE_POST_VALIDATE_PATH= "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/INPUTS/INPUT_PATH/"
BKP_INPUT_PATH= "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/INPUTS/BKP_INPUT_PATH/"

LATEST_REF_PATH= "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/INPUTS/LATEST_REF_PATH/"
BACKUP_REF_PATH= "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/INPUTS/BACKUP_REF_PATH/"

#############-->AUTOMATION START SLEEP TIME<--################
AUTO_START_SLEEP_TIME= "1"

#############-->DISK SPACE CHECKING BEFORE AUTOMATION<--################
DISK_SPACE_CHK= "df -h | grep -w '/' | cut -d'G' -f3"
MIN_DISK_SPACE=5

###############-->Do you want PCAP Validation?<--##############
PCAP_Validation=0
XML_DECODE_Validation=0

###############-->Do you want Shell Command Execution?<--##############
SHELL_COMMAND_VALIDATION=0
SHELL_PRE_CMD=0
SHELL_ON_CALL_CMD=0
SHELL_POST_CMD=0



###############-->Do you want Logger to be captured?<--##############
LOGGER_Validation=0
LOG_PATTERN_VALIDATION=0



###############-->Do you want State Machine Needs to be executed<--##################
SCENARIO_EXECUTION=0

###############-->Do you want Seagull State Machine Needs to be executed<--##################
SEAGULL_EXECUTION=0
##############--> 1 - TEST CASE ID EQUALS TO SCENARIO ID 2 - TEST CASE ID NOT EQUALS TO SCENARIO ID AND SCENARIO ID WILL BE GIVEN AT RUNTIME<--##########
SEAGULL_EXECUTION_TYPE=0

###############-->Do you want MGTS State Machine Needs to be executed<--##################
MGTS_EXECUTION=0

###############-->Do you want Kill old SIPP & SEAGULL Scenarios before execution<--##################
KILL_OLD_SIPP_SEAGULL_SCENARIOS=1




###############-->Do you want CDR Validation?<--##############
CDR_Validation=0

###############-->Do you want SOAP AND XML Validation?<--##############
XML_EXECUTION=0
HTTP_EXECUTION=0
SOAP_Validation=0
XML_Validation=0
JMETER_EXECUTION=1
SMS_REQUEST_EXECUTION=1
SCTT_SERVER_EXECUTION=1
SIPP_REMOTE_EXECUTION=1
PROTOCOL_VALIDATION=1
PROTOCOL_VALIDATION_TYPE=0



###############-->Do you want DB Validation?<--##############
DB_Validation=0
PRE_DB_Validation=0                        ########For PRE DB QUEIRES#########################
ON_CALL_DB_Validation=0                    ########For ON CALL DB QUEIRES#####################
POST_DB_QUERY_Validation=0                 ########For POST DB QUEIRES########################



###############-->Number of seconds To wait after post execution<--############
POST_SLEEP_EXECUTION=1

##############-->TEST CASE DEPENDANCY VALIDATION<---################
TC_DEPENDENCY_ENABLE=0

##############-->Consolidated Test Case Results<--#############################
CONSOLIDATED_RESULT_FILE="/opt/product/AUTOMATION/AUTOMATION_RESULTS/CPAAS/CONSOLIDATED_RESULTS/"


############-->RESULT VALUES<--#####################
SCEN_RESULT="NONE"
SIPP_RESULT="NONE"
JMETER_RESULT="NONE"
SMPP_SERVER_RESULT="NONE"
SMPP_CLIENT_RESULT="NONE"
WIREMOCK_RESULT="NONE"
cdr_status="NONE"
pcap_status="NONE"
autostop_status="NONE"
postdb_status="NONE"
http_status="NONE"
shellpre_status="NONE"
shelloncall_status="NONE"
shellpost_status="NONE"
xml_status="NONE"

TC_SCEN_STATUS="NONE"
TC_SIPP_STATUS="NONE"
TC_JMETER_STATUS="NONE"
TC_SMPP_SEVER_STATUS="NONE"
TC_SMPP_CLIENT_STATUS="NONE"
TC_WIREMOCK_STATUS="NONE"
TC_POSTDB_STATUS="NONE"
TC_CDR_STATUS="NONE"
TC_PCAP_STATUS="NONE"
TC_RESULT="NONE"
TC_SHELLPRE_STATUS="NONE"
TC_SHELLON_STATUS="NONE"
TC_SHELLPOST_STATUS="NONE"
TC_HTTP_STATUS="NONE"
