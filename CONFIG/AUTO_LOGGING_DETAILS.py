###########-->> Logger Paths used in each server,Logger Paths enclosed between a square bracket,Each set of logger paths of each server enclosed within outside square bracket<--#################

REMOTE_LOGPATH= [   "/opt/product/testteam/Products/AUTOMATION/NIG/release/bin/log/",
		    "/opt/product/testteam/Products/AUTOMATION/NIG/MAPGW/bin/log/"

                ]


SERVER_ALIAS= [ "42_auto","44_auto" ]


###########-->>File name prefix of each logger in the result path<--######################################

GREP_PREFIX=[["NIG_"],["MAPGW_"]]


##########-->> Prefix that needs to be prefixed before log file in the result path<<--####################

LOGGER_PREFIX=[["NIG_API"],["SIG_GW"]]

###########LOG PATTERN VALIDATION#################

log_pattern_input_alias= {
                           "NIG" : "MAPGW"
                         }
