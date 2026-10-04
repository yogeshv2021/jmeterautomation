JMETER_BIN_PATH= "/opt/apache-jmeter-5.4.3/bin/jmeter.sh"

JMETER_JMX_PATH= [ "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/INPUTS/JMETER/SCENARIO/" ]

JMETER_REPORT_PARAMS= [ "-Jjmeter.save.saveservice.response_message=false -Jjmeter.save.saveservice.thread_name=true -Jjmeter.save.saveservice.data_type=true -Jjmeter.save.saveservice.successful=true -Jjmeter.save.saveservice.assertion_results_failure_message=false -Jjmeter.save.saveservice.bytes=true -Jjmeter.save.saveservice.sent_bytes=true -Jjmeter.save.saveservice.thread_counts=true -Jjmeter.save.saveservice.latency=true -Jjmeter.save.saveservice.idle_time=true -Jjmeter.save.saveservice.connect_time=true -Jjmeter.save.saveservice.sample_count=true -Jjmeter.save.saveservice.success=true -Jjmeter.save.saveservice.error_count=true -Jjmeter.save.saveservice.url=false -j "]

JMETER_LOG_FILE_PATH= [ "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/INPUTS/JMETER/LOG/CLIENT/" ]

JMETER_LOG_DIR_PATH= [ "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/INPUTS/JMETER/LOG/" ]

JMETER_SCENARIO_FILE_VARIABLE= ["-Jfilename="]

JMETER_CHECK_KEY= "JMETER_REQUEST_VALIDATION"

JMETER_LOG_LEVEL= "INFO"

JMETER_LOG_PRINT= "1"

JMETER_SMS_LOG_PRINT= "0"

JMETER_SUMMARY_RESULTS= "1"

JMETER_EXECUTION_TYPE= "1"

JMETER_PROTOCOL_EXECUTION= "2"

JMETER_TEMPLATES_FOLDER= "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/INPUTS/JMETER/SCENARIO/TEMPLATES"

JMETER_DEFAULT_FOLDER="/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/INPUTS/JMETER/SCENARIO/DEFAULT"

JMETER_VALUES_FOLDER= "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/CPAAS/INPUTS/JMETER/SCENARIO/VALUES"

URL= [ "http://192.168.151.143:4020" ]

HEADERS_CONTENT_TYPE= [ "application/json" ]

HEADERS_EXPECT= [ "100-continue" ]

HEADERS_SOAPAction= [ "/IS_VALID_NUMBER/" ]

HTTP_Host= [ "192.168.151.143:4020" ]

HTTP_XML_VALIDATE_PATH= [ "/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/NIG/INPUTS/HTTP_XML/" ]

SOAP_ALIAS= [ "NIG" ]

SOAP_NAMESPACE= [ " " ]

http_uri= "/NIG_AUTO/"

JSON_FLAG= 1

HMAC=1

hmac_appid="tester-ez2R3MBdCwIdfgrHSPYMo72azJFoEegA"

hmac_akey="testteam"

hmac_opco="LYCA001"

hmac_bearer="Bearer"

hmac_msisdn="${MSISDN}"