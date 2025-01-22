# Backend Project

This is a backend project built with FastAPI and MongoDB. It provides CRUD operations for managing blog posts.

## Features

- Create a new blog post
- Get a blog post by `blog_id`
- Get all blog posts
- Get blog posts by author
- Get a blog post by `_id`
- Update a blog post by `blog_id`
- Delete a blog post by `blog_id`
- Delete all blog posts

## Requirements

- Python 3.8+
- MongoDB

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Dhirajsharma2060/assignment_2.git
cd assignment_2/backend
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a .env file in the backend directory with your MongoDB URI:

```bash
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/
#Replace <username>, <password>, and <cluster> with your actual MongoDB credentials and cluster name.
```

## Running the Application
### Start the FastAPI server:
```bash
uvicorn main:app --reload
```