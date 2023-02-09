import requests
import json

# """"""""""""""""""""""""""""""""""""""""""""""""""

status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}',
    headers = {'accept': 'application/json'})

print(f'Статус ответа от сервера на GET запрос:{res.status_code}')
print(res.json())


# """"""""""""""""""""""""""""""""""""""""""""""""""
info = {
"id": 9223372036854264999,
"category": {"id": 0,"name": "Dog"},
"name": "Boby",
"photoUrls": ["no foto"],
"tags": [{"id": 0,"name": "string"}],
"status": "available"
}
res_post_addNewPet = requests.post(f'https://petstore.swagger.io/v2/pet',
    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
    data = json.dumps(info, ensure_ascii=False))

print(f'Статус ответа от сервера на POST запрос добавление питомца: {res_post_addNewPet.status_code}')
print(res_post_addNewPet.json())


# """"""""""""""""""""""""""""""""""""""""""""""""""

new_info = {
"id": 9223372036854264999,
"category": {"id": 0,"name": "Cat"},
"name": "Gaga",
"photoUrls": ["no foto"],
"tags": [{"id": 0,"name": "string"}],
"status": "available"
}

res_put_rename_pet = requests.put(f'https://petstore.swagger.io/v2/pet',
    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
    data=json.dumps(new_info, ensure_ascii=False))
print(f'Статус ответа от сервера на PUT изменение данных питомца: {res_put_rename_pet.status_code}')
print(res_put_rename_pet.json())

# """""""""""""""""""""""""""""""""""""""""""""""

petId = 9223372036854264999
res_delet_pet = requests.delete(f'https://petstore.swagger.io/v2/pet/{petId}',
      headers={'accept': 'application/json'})
print(f'Статус ответа от сервера на DELETE удаление питомца: {res_delet_pet.status_code}')
print(res_delet_pet.json())
