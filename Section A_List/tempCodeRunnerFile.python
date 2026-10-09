'''
Question 5: Social Media Likes
A social media platform stores the number of likes received by five posts in a list. 
Write a function to find the post with the highest likes, calculate total likes, and display posts that received at least 100 likes.
'''

def soc_media_likes(likes):
    top_post = likes.index(max(likes)) + 1
    total = sum(likes)
    popular = [f"Post {i + 1}: {count} likes"
               for i, count in enumerate(likes) if count >= 100]

    print(f"Post with highest likes: Post {top_post} ({max(likes)} likes) \n Total likes: {total} \n  Posts with at least 100 likes:")

    for posts in popular:
        print(" ", posts)

soc_media_likes([120, 45, 230, 99, 310, 560, 74, 96])
print()