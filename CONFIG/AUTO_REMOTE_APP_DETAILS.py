#############-->>Remote Server Details for Old Model <--################ 
APP_HOST = "192.168.151.112"
APP_USERNAME = "testteam"
APP_PASSWORD = "testteam"
APP_PROMPT = "$"
AUTO_PROMPT = "AUTO$"
APP_ALIAS = "PPGW_SERVER"
ENCODING = "iso-8859-2"

############-->>Remote Servers Details for New Model<--####################
SERVERS = [
           {"HOST"               : "192.168.151.97",
           "USERNAME"            : "root",
           "PASSWORD"            : "root123",
           "PROMPT"              : "#",
           "ALIAS"               : "97_root",
           "PLATFORM"            : "LINUX",
           "ENCODING"            : "UTF-8",
           "LOGIN_TYPE"          : "PUBLICKEY",
           "APP_PRODUCTS"        : "CPaaS_App"
          },
           {"HOST"               : "192.168.151.112",
           "USERNAME"            : "root",
           "PASSWORD"            : "D1f0r@pbs1",
           "PROMPT"              : "#",
           "ALIAS"               : "112_root",
           "PLATFORM"            : "LINUX",
           "ENCODING"            : "UTF-8",
           "LOGIN_TYPE"          : "PUBLICKEY",
           "APP_PRODUCTS"        : "CPaaS_App"
          }
	]



PRODUCT_SERVER_DICTIONARY = {
                               "CPaaS_App"          :  "97_root"
                            }


PRODUCT_SCRIPT_DICTIONARY = {
                               "CPaaS_App"             :  "/opt/product/ :bash start_itg.sh 1"
                            }

GRACE_EXIT_DICTIONARY = {
                               "CPaaS_App"          :  "kill -2"
                        }

REMOTE_DISK_SPACE_CHK= {
                             "97_root"               : "df -h | grep -w '/'| cut -d'G' -f3",
                             "112_root"               : "df -h | grep -w '/'| cut -d'G' -f3"

                       }


CONFIG_ALIASES = {
                    
                 }


SLEEP_TIME = 10
REMOTE_START_TYPE = 0

