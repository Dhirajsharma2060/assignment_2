from fastapi import FastAPI, HTTPException, status
from cors import add_cors_middleware
from model import Blog, UpdateBlog
from db import blog_collection
from schema import format_blog
from bson import ObjectId

app = FastAPI()

# Add CORS middleware
add_cors_middleware(app)

@app.post("/blogs", status_code=status.HTTP_201_CREATED)
def create_blog(blog: Blog):
    last_blog = blog_collection.find_one(sort=[("blog_id", -1)])
    blog_id = (last_blog.get("blog_id", 0) + 1) if last_blog else 1
    blog_data = blog.dict()
    blog_data["blog_id"] = blog_id

    new_blog = blog_collection.insert_one(blog_data)
    created_blog = blog_collection.find_one({"_id": new_blog.inserted_id})
    return format_blog(created_blog)

@app.get("/blogs/{blog_id}")
async def get_blog_by_id(blog_id: int):
    blog = blog_collection.find_one({"blog_id": blog_id})
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return format_blog(blog)

@app.get("/blogs/author/{author}")
async def get_blogs_by_author(author: str):
    blogs = blog_collection.find({"author": author})
    return [format_blog(blog) for blog in blogs]

@app.get("/blogs/_id/{_id}")
async def get_blog_by_object_id(_id: str):
    blog = blog_collection.find_one({"_id": ObjectId(_id)})
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return format_blog(blog)

@app.get("/blogs")
async def get_all_blogs():
    blogs = blog_collection.find()
    return [format_blog(blog) for blog in blogs]

@app.delete("/blogs/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(blog_id: int):
    result = blog_collection.delete_one({"blog_id": blog_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog deleted successfully"}

@app.delete("/blogs", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_blogs():
    blog_collection.delete_many({})
    return {"message": "All blogs deleted successfully"}

@app.patch("/blogs/{blog_id}", status_code=status.HTTP_200_OK)
async def update_blog(blog_id: int, blog: UpdateBlog):
    updated_blog = blog_collection.find_one_and_update(
        {"blog_id": blog_id},
        {"$set": blog.dict(exclude_unset=True)},
        return_document=True
    )
    if updated_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return format_blog(updated_blog)
