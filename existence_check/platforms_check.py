from existence_check.platforms import *

def platforms_check(username):

    facebook.facebook_check(username)
    github.github_check(username)
    instagram.instagram_check(username)
    pinterest.pinterest_check(username)
    reddit.reddit_check(username)
    steam.steam_check(username)
    telegram.telegram_check(username)
    tumblr.tumblr_check(username)
    vkontakte.vkontakte_check(username)
    youtube.youtube_check(username) 
    mastodon.mastodon_check(username)
    snapchat.snapchat_check(username)