# from pydantic import BaseModel, Field

# class User(BaseModel):
#     name: str
#     age:int
#     is_active: bool = True
    

# user = User(name="John Doe", age="30")
# print(user)
# print(user.is_active)


# class Product(BaseModel):
#     name: str
#     price: float = Field(gt=0, description="The price must be greater than 0")
#     tags: list[str] = []   
#     category: str = Field(default="General", description="The category of the product")
#     def __str__(self):
#         return f"Product(name={self.name}, price={self.price}, tags={self.tags}, category={self.category})" 

# product = Product(name="Laptop", price=999.99, tags=["electronics", "computers"])
# print(product)
# print(product.category)
# print(product.tags)
# print(product.price)
# print(product.name)
# print(product.dict())

from pydantic_settings import BaseSettings

class Settings(BaseSettings):  
    api_key: str
    secret_key: str
    db_url: str

settings = Settings() 