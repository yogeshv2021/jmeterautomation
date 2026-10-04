##############DB DETAILS######################

######Type of Database Used Eg:- cx_Oracle for ORACLE########
###### DB_TYPE = [ "cx_Oracle" , "mySQL" ] ######

DB_TYPE = ["cx_Oracle","cx_Oracle","cx_Oracle","cx_Oracle"]

postfix = "-end"



#################Enter ALIAS NAME FOR PRECONDITION OF EACH PRODUCTS Name##################################################
##########precondition= [ "DNGRRBS" , "PCRF" ]###############


precondition_input_alias = ["NIG","PCRF","HLR","EXIBS"]



#################Enter ALIAS NAME FOR ONCALLCONDITION OF EACH PRODUCTS Name##################################################
##########precondition= [ "DNGRRBS" , "PCRF" ]###############


oncallcondition_input_alias = ["NIG","PCRF","HLR","EXIBS"]



#################Enter ALIAS NAME FOR POSTCONDITION OF EACH PRODUCTS Name##################################################
##########precondition= [ "DNGRRBS" , "PCRF" ]###############


postcondition_input_alias = ["NIG","PCRF","HLR","EXIBS"]



#################Enter DB Connection String##################################################
##########DB_CONNECTION_STRING= [ "lycarrbsdb1/lyca@192.192.192.192/auto" , "lycarrbsdb2/lyca@192.192.192.192/auto" ]###############


DB_CONNECTION_STRING= [ "IMG_AUTO/LYCA@192.168.151.147:1521/ST11GDB" , "PCRF_AUTO_1/LYCA@192.168.151.147:1521/ST11GDB" , "HLR_BSS_AUTO/LYCA@192.168.151.147:1521/ST11GDB" , "TEST_BLUSCP/LYCA@192.168.151.147:1521/ST11GDB" ]



#################Enter the DB Queries that needs to be analysed when DB Post Condition Fails##################################################
####################PLACE HOLDER MSISDN needs to be placed in the DB Query & MSISDN needs to be passed in the testcase########################


DEBUGGING_QUERIES=["/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/NIG/INPUTS/itg_db_debug_query.txt"]

DUMMY_PLACE_HOLDERS=[ "MSISDN", "BUNDLE_CODE", "TARIFF_CODE", "NETWORK" ]



##############################1- Update System Time in DB ;0 - Do not Update System Time in DB######################
DB_UPDATE_TIME=1
