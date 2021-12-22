<<<<<<< HEAD
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    birthdate: Optional[str]
    profile_image_url: Optional[str]
    username: str
    website: Optional[str]
    pronouns: Optional[list[str]]
    biography: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    gender: Optional[str]


    database = []


    def new_user(user: User):
        database.append(user)

        return {
            'message': 'A new user was saved to the database',
            '_id': database.index(user)
        }

=======
# for Tierra
>>>>>>> c599837be3779b24a195b99285273ea1bff5221c
