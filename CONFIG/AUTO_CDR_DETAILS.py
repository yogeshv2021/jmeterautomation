REMOTE_CDR_PATH= [ 
                   "/opt/product/testteam/Products/PPGW/SPRINT_1.0_P2/bin/INCOMING_TDR_PATH",
                   "/opt/product/testteam/Products/PPGW/SPRINT_1.0_P2/bin/OUTGOING_TDR_PATH"
                 ]

CDR_SERVER_ALIAS= [ "42_auto","44_auto"]

###########-->>File name prefix of each logger in the result path<--######################################

CDR_GREP_PREFIX=[["*"],["*"]]

##########-->> Prefix that needs to be prefixed before log file in the result path<<--####################

CDRS_PREFIX=[["EXGW"],["EXGW"]]

##############REFERENCE CDR PATH AND PATTERNS############################
######eg:-REF_CDR_PATH={ 
######                     "path1/":".txt",
######                     "path2/":".tdr" 
######                 }


REF_CDR_INPUT_ALIAS= [
                       "INCOMING_TDR",
                       "OUTGOING_TDR"
                     ]

REF_CDR_INPUT_EXT= [
                       ".tdr",
                       ".tdr"
                   ]

##############eg:-CDR_FIELDS= [ "1-3,6-9" , "1-5,10-30" ]##############
#####Should be in the order in which Reference CDR Path is Given#######


CDR_FIELDS= [
              "4-12,14-34",
              "9-29,31-37"
            ]

DELIMITERS= [",",","]

TOTAL_CDR_COUNT= [40,37]

MIGRATION_FLAG=0


########### REF_CDR_PATTERN_0 indicates CDR Field Description for First Reference CDR Path 
########### REF_CDR_PATTERN_1 indicates CDR Field Description for Second Reference CDR Path


REF_CDR_PATTERN_0=[
"ReqRouting",
"ProxyIP",
"ProxyProtocol",
"OriginatorIP",
"OriginatorProtocol",
"Entity",
"OriginatorTransId",
"ChannelRef",
"ApiName",
"MapGwOperId",
"Msisdn",
"Opco",
"AddReqData",
"Status",
"ErrorCode",
"ErrorDesc",
"DbErrorCode",
"DbErrorDesc",
"MemCacheDApiNode",
"MemCacheDApiErrorDesc",
"MemCacheDCellIdNode",
"MemCacheDCellIdErrorDesc",
"RemoteErrorCode",
"RemoteErrorDesc",
"NetworkId",
"Respondedfrom",
"CacheMissReason",
"ResponseData",
"Auth",
"AuthType",
"MapGwNode"

]

REF_CDR_PATTERN_1=[
"RequestType",
"RequestMsisdn",
"RequestImsi",
"Opco",
"MapOperation",
"ErrorCode",
"ErrorDesc",
"RequestSSCode",
"MapMsgName",
"MsgStatus",
"OpenCnfVersionRcvd",
"SSStatus",
"ForwardToNumber",
"VlrNumber",
"Longitude",
"Latitude",
"CellId",
"Mcc",
"Mnc",
"AreaCode",
"ResponseImsi",
"TransactionId",
"RemoteErrorCode",
"RemoteErrorDesc",
"FreeFormatData",
"OriginatingMapGwGT",
"DestinationHlrGT",
"OrigTransactionId",
"OrigEntity"

]

