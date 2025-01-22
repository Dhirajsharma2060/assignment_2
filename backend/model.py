from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    content: str
    author: Optional[str] = "Anonymous"
    blog_id: int = None

class UpdateBlog(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
