pip install -r requirements.txt

# ДЗ 20. Прості тести на PetStore API
Для REST API Service Swagger UI написати тести на PyTest на наступні end-points:

- /pet/findByStatus
- /pet (POST METHOD)
- /pet (PUT METHOD)

Не забувати правильні перед- і пост-умови оформляти у фікстури. 
Оформити тести через параметризацію тестових методів (функцій) буде підвищувати оцінку. 
Спосіб написання тестів "на коліні" (тобто без фікстур та параметризації) буде зменшувати оцінку.

## What have been done
1. 'tests' folder has been created that contains the following files with tests:
- 'test_get_by_status.py' file that tests task: '/pet/findByStatus'
- 'test_post_put_pet.py' file that tests '/pet (POST METHOD)' and '/pet (PUT METHOD)'tasks
2. 'src' -> 'enums' -> 'global_enums.py' file contains enum with error messages for tests
3. 'configuration.py' file contains base url, endpoints and parameters for tests