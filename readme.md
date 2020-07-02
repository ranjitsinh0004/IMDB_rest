## imdb_prj
1. For the backend `Django Rest Framework` is used.
2. `Pipenv` is used as a packaging tool.
3. API tesing is done with `POSTMAN`
4. Generated requirements.txt using `pipenv lock -r > requirements.txt`
5. Populated the database with the data provided in json format to mysql.

### How to run the project?
1. open the terminal change the directory to project.
        `cd imdb_rest_dir`
        `cd imdb_prj`
2. Run the virtual environment using following command
        `pipenv shell`
3. Install the dependencies
        `pip install -r requirements.txt`
4. Run the server
        `py manage.py runserver`
5. Open the browser and observe the lists of movies on it. No authentication needed.
        `http://127.0.0.1:8000/api/movielistgenerics/`

6. Provide token(`Token 8f94c1667a7f12565e91624713a98737cf5292fa`) to make the changes like put,patch,post, delete. Use the url `http://127.0.0.1:8000/api/movieviewset/`

7. Also done the above two functionalities using http based `APIView`. Follow the following urls to observe the response
        `http://127.0.0.1:8000/api/movielist/` no need of authentication
        `http://127.0.0.1:8000/api/moviecreate/` authentication needed
        `http://127.0.0.1:8000/api/movie/10` authentication needed

8. All the APIs are weldocumented using `swagger`. Follow the url `http://127.0.0.1:8000/swag/` to find the swagger ui. Then login for seesion login by providing the credentials of superuser i.e
        `username:admin`
        `password:admin`


### Heroku Deployment?
1. Used git as repository and version contorl
2. Committed the repository on `Bitbucket`
3. Deployed on Heroku. Follow the url `https://imdbeco88.herokuapp.com/`

### Tracking
1. backend functionality: 1 day
2. testing and deployment: 1 day


### added features
* swager
* pagination
* tokenauthentication