# Music-App-Development
Music Webapp as a part of MAD2 project.

This web app offers a comprehensive set of features:
- Users can listen to songs, albums, create playlists, read lyrics, and rate songs.
- Creators can upload songs and albums, enriching the music collection with lyrics.
- Admin functionalities include viewing application statistics, flagging songs and albums, and managing user accounts.

- The backend is built with Flask, SQLAlchemy serves as the ORM, and Vue powers the frontend. Integration with Flask-RESTful API facilitates smooth communication between frontend and backend. Additionally, Redis and Celery automate tasks like sending daily reminders and generating monthly reports for a seamless user experience.
  
- ## Technologies Used
- Flask: Micro framework for web applications.
- Flask-SQLAlchemy: ORM for working with databases using Python.
- Flask-Security: Authentication and session management.
- Bootstrap: Frontend toolkit for responsive design.
- Flask-Restful: Simplifies the development of RESTful APIs.
- Flask-RBAC: Role-based access control.
- Vue: Declarative, component-based UI development.
- Celery: Task queue for background processing.
- Redis: In-memory database used as a message broker.

  The database schema consists of 7 tables with various relationships:
1. Users
2. Roles
3. Roles_Users
4. Songs
5. Albums
6. Playlists
7. Association

## API Design
The `api` directory contains Flask-Restful API applications for user, song, album, and playlist management. JSON serialization is employed for outputs.

## Project Video
You can watch a demo of the project in the video: [[mad2projectvideo.mov](mad2projectvideo.mov)](https://drive.google.com/file/d/1LBjn08chxFJRslft4fVASMMtrh0EKMp1/view)






