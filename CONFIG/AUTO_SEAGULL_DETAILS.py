#############-->>Enter the path to save automation report <--################
REMOTE_AUTOPATH = "/opt/product/testteam/Products/AUTOMATION/PCRF/Automation_folder/delcom-script"
REMOTE_AUTOSCRIPT = "startstopscript.sh"



#############-->>SEAGULL path Details <--################
LD_LIBRARY_PATH= "/usr/local/bin"
SEAGULL_confpath= "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/PCRF/INPUTS/SEAGULL/PCRF-CONF"
SEAGULL_DICO= "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/PCRF/INPUTS/SEAGULL/PCRF-CONF/DIAMETER-S6A-S6D-GX-GY.xml"
SEAGULL_SCENPATH= "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/PCRF/INPUTS/SEAGULL/PCRF-SECNARIOS"
SEAGULL_LOGPATH= "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/PCRF/PCRF_LOG"
SEAGULL_COMPLOGPATH= "/opt/product/AUTOMATION/AUTOMATION_RESULTS/PCRF/COMPLETED_PCRF_LOG"
SEG_PROCESS="SEAGULL_PCRF"
SEAGULL_SLEEP=2
SEAGULL_TIMEOUT=60
SEAGULL_PIDGREP = "Background"
SEAGULL_STDERR_FILE = "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/PCRF/stderr"



############-->>STATUS FLAGS-->>#############
PASS= "DONE"
FAIL= "FAIL"
NOPREDB= "NULL"



############LD Library path#############
SEGENV= "export LD_LIBRARY_PATH=/usr/local/bin"
##############-msgchecK Validation#############
msgchk = "NO"
msgno = " "
##############-msgchecK Validation#############
PROGDIR = "/usr/local/bin"
SEG_WORKPATH = "/opt/product/AUTOMATION/PCRF/Master_script"
CMD_PASSFAIL = "ls -rt ${log_path}${/}${SCENARIO_FILE}* | tail -1"
GREP_STRING = "Scenario [TD]?????? passed"
TESTCASE_FILE = "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/PCRF/seagull_automation-pcrf-delcom-cases.conf"
TEST_CASE_RESULT = "TEST"
