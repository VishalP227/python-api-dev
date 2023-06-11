# Social Media API
## Project overview
In this project, a full scale working API for generic social media has been developed. This API has the following features:
- Uses FAST API framework 
- Support all CRUD functions
- Functions to create users, user login using authentication tokens and get user by id 
- Functions to create posts, get all posts, get posts by id, delete posts by id and update posts by id. 
  All these are allowed only for an authenticated user
- Functions to add and remove votes on posts, also not allowing multiple votes on same post. 
  All these are allowed only for an authenticated user

## Tech Stack  
API framework: FAST API  
Database: Postgresql  
Database tools: SQLAlchemy (sql mapper), Alembic (database migration)   
Testing: pytest library  
CI/CD: github actions  
Containerization: Docker  
Deployment: Tested local deployment on ubuntu server running on a vitrual machine  
