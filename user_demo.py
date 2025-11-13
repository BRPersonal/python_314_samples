from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int = Field(ge=18)

user = User(name="Maria", age="21")  # auto-converts str → int
print(f"user={user}")

