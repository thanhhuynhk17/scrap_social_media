import instaloader


class InstagramProfile:
    def __init__(self, username):
        self.username = username

    def scrap(self):
        # Creating an instance of the Instaloader class
        bot = instaloader.Instaloader()
        # Loading a profile from an Instagram handle
        profile = instaloader.Profile.from_username(bot.context, self.username)

        info = {
            'ig_id': profile.userid,
            'name': profile.username,
            'bio': profile.biography,
            'posts': profile.mediacount,
            'followers': profile.followers,
            'following': profile.followees,
            'avatar_url': profile.get_profile_pic_url()
        }

        return info
