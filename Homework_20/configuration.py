BASE_URL = 'https://petstore3.swagger.io/api/v3'
ABOUT_PET = '/pet'
FIND_BY_STATUS = '/findByStatus?status='

# get
AVAILABLE = f'{BASE_URL}{ABOUT_PET}{FIND_BY_STATUS}available'
PENDING = f'{BASE_URL}{ABOUT_PET}{FIND_BY_STATUS}pending'
SOLD = f'{BASE_URL}{ABOUT_PET}{FIND_BY_STATUS}sold'

# post/put
PET = f'{BASE_URL}{ABOUT_PET}'
