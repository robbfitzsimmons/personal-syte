# -*- coding: utf-8 -*-

DEPLOYMENT_MODE = 'dev'
COMPRESS_REVISION_NUMBER = '5.0'

BLOG_PLATFORM = 'tumblr'  # Wordpress or tumblr

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'robbfitzsimmons.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'uvh0xPM0qB88yKq56qFSLYE43QPdMfcKar01xbWCWR2WiROYN6'

#Blog Integration: Wordpress
WORDPRESS_BLOG_URL = '[ENTER WORDPRESS BLOG URL] ex. gordonkoo.wordpress.com'
WORDPRESS_API_URL = 'https://public-api.wordpress.com/rest/v1/sites/{0}'.format(WORDPRESS_BLOG_URL)

#RSS Feed Integration: (by default use Tumbrl rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'https://api.twitter.com/'
TWITTER_CONSUMER_KEY = 'ldeFUNw17oXJBOULcCjA'
TWITTER_CONSUMER_SECRET = 'RCLjIP9zuUfJf51A0vGsdUqvi2ZYwZGvOMgENpDQMHw'
TWITTER_USER_KEY = '239618187-mx8zFLiLXPISnsls2185TznRSzxFuH7YrUeZLMY4'
TWITTER_USER_SECRET = 'rt7Q3mLulL1GmMxfqEoqpJhz1vSySwL9thkab1cSxg'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = 'ecabd996362408521822cc46d12d9859d62d4d7e'

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = 'eab61f7dffc1f0e6da7a'
GITHUB_CLIENT_SECRET = 'c5a2769ac36302a904b527ff337af3328195ad1b'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'

#Stack Overflow Integration
STACKOVERFLOW_INTEGRATION_ENABLED = True
STACKOVERFLOW_API_URL = 'http://api.stackoverflow.com/1.1/'

#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '21373670.0b14525.7c498c68155b4d22857dcd223b3178f3'
INSTAGRAM_USER_ID = '21373670'

INSTAGRAM_OAUTH_ENABLED = False
INSTAGRAM_CLIENT_ID = '0b14525228aa4cbf8ef86fd165f2da91'
INSTAGRAM_CLIENT_SECRET = '651c1a1e5f454f55bdb431a742b5ee62'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Foursquare Integration
FOURSQUARE_INTEGRATION_ENABLED = True
FOURSQUARE_API_URL = 'https://api.foursquare.com/v2/'
FOURSQUARE_ACCESS_TOKEN = 'OYVW2CNRA0EN4ZO0OY3YKBRTW4YOG0M1UHHOD01FWRXB45SE'
FOURSQUARE_SHOW_CURRENT_DAY = True

FOURSQUARE_OAUTH_ENABLED = True
FOURSQUARE_CLIENT_ID = 'UJQGXKEPTFARBL2WBZ1ZBHLKMSPYQPL00D0SPX3VEN3WFBZF'
FOURSQUARE_CLIENT_SECRET = 'OTW4A42OJDX4J5WUFLHFPWADTGTK0AKAYOPJ2FJW2OTNXYU0'
FOURSQUARE_OAUTH_AUTHORIZE_URL = 'https://foursquare.com/oauth2/authenticate'
FOURSQUARE_OAUTH_ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = 'UA-34179169-1'

#ShareThis
SHARETHIS_PUBLISHER_KEY = ''


#Woopra
WOOPRA_TRACKING_DOMAIN = ''
WOOPRA_TRACKING_IDLE_TIMEOUT = 300000  # 5 minutes
WOOPRA_TRACKING_INCLUDE_QUERY = False


#Disqus Integration
DISQUS_INTEGRATION_ENABLED = False
DISQUS_SHORTNAME = 'robbfitzsimmons'


#Lastfm Integration
LASTFM_INTEGRATION_ENABLED = True
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = '89dc5f710874faaa1e86464996b208e7'
LASTFM_USERNAME = 'robbfitzsimmons'


#SoundCloud Integration
SOUNDCLOUD_INTEGRATION_ENABLED = False
SOUNDCLOUD_API_URL = 'https://api.soundcloud.com/'
SOUNDCLOUD_CLIENT_ID = '[ENTER SOUNDCLOUD APPLICATION CLIENT_ID HERE]'
SOUNDCLOUD_SHOW_ARTWORK = False
SOUNDCLOUD_PLAYER_COLOR = 'ff912b'


#Bitbucket Integration
BITBUCKET_INTEGRATION_ENABLED = False
BITBUCKET_API_URL = 'https://api.bitbucket.org/1.0/'
# Forks count require one connection for each repository,
# set BITBUCKET_SHOW_FORKS to false to disable
BITBUCKET_SHOW_FORKS = False

#Tent.io Integration
TENT_INTEGRATION_ENABLED = False
TENT_ENTITY_URI = '[ENTER YOUR ENTITY URI HERE] ex. https://yourname.tent.is'
TENT_FEED_URL = '[ENTER A URL TO YOUR FEED] ex. https://yourname.tent.is'


#Steam Integration
STEAM_INTEGRATION_ENABLED = False
STEAM_API_URL = 'http://api.steampowered.com/ISteamUser'
STEAM_API_KEY = '[ENTER YOUR STEAM API KEY HERE, SEE STEAM SETUP INSTRUCTIONS]'

#Flickr Integration
FLICKR_INTEGRATION_ENABLED = True
FLICKR_ID = '[ENTER YOUR FLICKR ID (NOT USERNAME) HERE]' # You do your username->ID lookup here: http://idgettr.com/

#LinkedIn Integration
LINKEDIN_INTEGRATION_ENABLED = True
LINKEDIN_API_KEY = '78i4h1usker2lz'
LINKEDIN_API_SECRET = 'DFyiDfymBviUpDiY'
LINKEDIN_TOKEN = 'AQUc_e_JD2_9AiM4YTOXF-DT1UvWPhGQWvHULdYNj0LHLR8Nfg_Xssjtuj5HGTB9r9tIE0OdHZQyQ5bmgfJedgYXuGxpegRNy7vhiVsbwa23A4_oCiEDBuoKsM9gQKDuZdEwVs-wtSPHBItT-VahUjBdMcLrZ7UTOg07wdO-FhXEqY0KNbM'

SITEMAP_ENABLED = True

if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    ALLOWED_HOSTS = ['*']
    DEBUG = True
else:
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    SITE_ROOT_URI = 'https://robb-personal-site.herokuapp.com/'
