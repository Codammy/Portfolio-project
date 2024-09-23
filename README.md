# Sellit backend

`Sellit`, I hope one day would be something every store owner, individual, marketers, promoters would chew in the mouth everyday... lol

## REST FRAMEWORK
This is the `v1` backend of the sellit project built with `python_django_rest_framework

### HOW TO USE
1. clone the repository or download as zip file.

2. cd into the repo like `cd  repo-name`

3. **run:**
```bash
pip install -r requirements.txt
./manage.py runserver # to start the server usually on port 8009
```
4. Launch your postman or any other rest api client.

**Available endpoints:**
BASE_URL = "/api/v1"
| endpoint | supported methods |
| :-------- | -----------------: |
| /token    | POST |
| /token-refresh | POST |

