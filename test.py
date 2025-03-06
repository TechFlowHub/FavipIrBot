from database import dbConfig

result = dbConfig.insertPhone('k9083091')
print(result)

result_current_service = dbConfig.insertPhoneToCurrentService('23262i3091i025')
print(result_current_service)

get = dbConfig.getAllPhonesFromCurrentService()
print(get)

delete_result = dbConfig.deletePhoneFromCurrentService('123')
print(delete_result)