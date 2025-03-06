from database import dbConfig

# Inserir telefone na tabela phones
result = dbConfig.insertPhone('81989945697')
print(result)

# Inserir telefone na tabela current_service
result_current_service = dbConfig.insertPhoneToCurrentService('81989945697')
print(result_current_service)
