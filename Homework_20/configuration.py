BASE_URL = 'https://petstore3.swagger.io/api/v3'
ABOUT_PET = '/pet'
FIND_BY_STATUS = '/findByStatus'

# post/put
PET = f'{BASE_URL}{ABOUT_PET}'

# get
AVAILABLE = f'{PET}{FIND_BY_STATUS}?status=available'
PENDING = f'{PET}{FIND_BY_STATUS}?status=pending'
SOLD = f'{PET}{FIND_BY_STATUS}?status=sold'


