def format_blog(blog):
    if blog is None:
        return None
    blog["_id"] = str(blog["_id"])
    return blog
