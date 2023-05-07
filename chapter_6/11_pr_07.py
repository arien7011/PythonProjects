#Write a program to find out whether a post is talking about 'Arian' or not

# post = '''Arian is doing fine right now in software development but needless to say that he really needs to hone their 
# development skills '''

posts = input('Enter your post here : ')
posts = posts.lower()
if( 'arian' in posts) :
    print('Yes , Arian is mention in the post')
else :
    print('sadly not')
