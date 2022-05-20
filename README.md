## Navigation
![image](https://user-images.githubusercontent.com/101140452/169602500-cd269430-73f0-4c22-a1fc-0946c547c8f5.png)

***
## Task description 🍪
- User registration;
- Authorization of the user;
- Personal account of the user;
- List of users.

In the personal cabinet you can add / delete skills as a Tag.
Tags and values can be chosen from those available in the database or you can add your own.
The added tags and values must also be included in the database and offered for to choose in the future.


Example of the personal account:

Ivanov Ivanovich
Skills: Python, Django, SQL, Async, REST
Languages: English, Chinese
Hobbies - music
 + Add Skill

***
## Basic run 🍪
Create a virtual environment
>python -m venv env


Activate the venv
>env\scripts\activate.bat


Open the project folder
>cd team


Install all modules
>pip install -r requirements.txt


Starting the server
>python manage.py

***
## Tips 🍪

You can add or delete a skill, CTRL + left button. Added skills will be highlighted.
If you save fields without highlighting, they are removed from the profile


***
## API 🍪 (In progress)
-     /basic_skill || POST
      Some text
>      
>      Parameters:                         Response:
>                                             
>                                          
>      
>      test_requests: {"email": "test@gmail.com","password": "Никита,сДР!"}
----

-      /profile || POST
       Some text
>      
>       Parameters:                         Response:
>       
>                        
>           
>      
>      test_requests: {'name': 'juice', 'email': 'test@test.com', 'password': 'test'}
----

-      /sign_in || POST
       Some text
>      
>       Parameters:                         Response:
>       
>       
>                                         
>                                      
>                                                       
>      
>      test_requests: {'messages': 'АБРАКАДАБРА'}
----

-      /sign_up || GET
       Some text
>      
>       Parameters:                         Response:
>      
>
>                                           
>                                           
>                                                            
>      
----
-      /sign_out || GET
       Some text
>      
>       Parameters:                         Response:
>      
>
>                                           
>                                           
>                                                            
>      
>               
***
   
