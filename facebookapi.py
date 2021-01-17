from re import error
import facebook
token = 'EAAKOQbimtGMBAENTVMfSiTjcYFwtIkF25POSN5oeyM3vCRpujD8IaUaxlf1wvzYXa8ji5BBJISgTeFD47SiJYvSdcZCTUAX2xufFX46Jtdk7Pt362XzHjWFOzmBGBeU157C3notq0MD0AKgs1418yAxDoiRtMtY9hKNvNxLFZBZAnH0RiXaDTZB7dgivNSAZD'
fbobj = facebook.GraphAPI(access_token=token)
# try:
# fbobj.put_object('me', 'feed', message='Posted using Graph API')
fbobj.put_photo(image=open('photo-1522364723953-452d3431c267.jpg', 'rb'),
                message='Photo posted using Graph API..Cool!')
# ca:
print('Posted')
