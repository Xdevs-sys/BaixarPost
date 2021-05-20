from datetime import datetime	
import instaloader


L = instaloader.instaloader()
L.Login("* Nome de Usuário *, * Senha *")

post = instaloader.Profile.from_username(L.context, "Frutinha56").get_posts()

SINCE = datetime(2021, 5, 20)
UNTIL = datetime(2021, 4, 18)

for post in posts:
	if (post.date >= SINCE) and (post.date <= UNTIL):
		print(date.post)
        
		L.download_post(post, "insta-post-downloads")