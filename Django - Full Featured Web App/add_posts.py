from random import choice    
from django.contrib.auth.models import User    
from blog.models import Post
import json

# Load the JSON data
with open('posts.json') as f:        
    posts_json = json.load(f)   

    # Get a list of all the IDs present in the database, that way, we wont
    # get into trouble when trying to assign an ID that doesnt exist in the database
    # to a post. 
    ids = [d.id for d in User.objects.all()]    

    # Add a group of posts and save them onto the database
    for post in posts_json:        
        Post(title=post['title'], content=post['content'], author_id=choice(ids)).save()

# To add these entries, just run the "add_posts" script in the
# django shell.
#   exec(open("add_posts.py").read())




    
