
## job vacancy 

### installation process

```http
  download/clone file
  activate env : source ./bin/activate
  install packages: pip install requirements.txt
  
  run server:
  cd src/backend/
  python manage.py runserver 8000
```

#### get a list of all applicants who are qualified

```http
  GET /api/qualified/
```

#### get a list of all vacancy position opened currently

```http
  GET /api/vacancy/
```

#### get a list of all people who have applied fot the position

```http
  GET /api/applicant/ 
```

#### add a new job vacancy position
```http
  POST /api/vacancy/add-position/
  {
    "job_title": "string"
  }
```

| Parameter   | Type     | Description                       |
| :---------- | :------- | :-------------------------------- |
| `job_title` | `string` | **Required**.|


#### add Required skills to the opened job vacancy position
```http
  POST /api/vacancy/add-position/
  {
    "job_id": FK int:job,
    "skill_name": "string"
  }
```

| Parameter   | Type     | Description                       |
| :---------- | :------- | :-------------------------------- |
| `job_id`    | `FK int:job` | **Required**.|
| `skill_name`| `string` | **Required**.|

#### add first and last name of the applicant tp register to the position
```http
  POST /api/applicant/add-info/
  {
    "first_name": "string",
    "last_name": "string"
  }
```

| Parameter   | Type     | Description                       |
| :---------- | :------- | :-------------------------------- |
| `first_name`    | `string` | **Required**.|
| `last_name`| `string` | **Required**.|


#### add skills of the applicant who applied for the job
```http
  POST /api/applicant/add-skills/
  {
    "job_id": FK int:applicant,
    "skill_name": "string"
  }
```

| Parameter   | Type     | Description                       |
| :---------- | :------- | :-------------------------------- |
| `candidate_id`    | `FK int:applicant` | **Required**.|
| `skill_name`| `string` | **Required**.|

