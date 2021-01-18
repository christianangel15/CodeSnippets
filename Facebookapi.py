import facebook
token = 'Your token here'
fbobj = facebook.GraphAPI(access_token=token)

# fbobj.put_object('me', 'feed', message='Posted using Graph API')
fbobj.put_photo(image=open('photo-1522364723953-452d3431c267.jpg', 'rb'),
                message='Photo posted using Graph API..Cool!')

print('Posted')
