from django.shortcuts import render

def posts_list(request):
    # Pass post data here as context if you have posts in a database
    posts = [
        {'title': 'Post 1', 'content': 'Content of post 1...'},
        {'title': 'Post 2', 'content': 'Content of post 2...'},
    ]
    
    return render(request, 'posts/posts_list.html', {'posts': posts})
