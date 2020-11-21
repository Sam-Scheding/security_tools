#########################################################################
# These are a bunch of tools I've needed in CTF tournaments.            #
# They are designed to be quick, simple implementations so they can be  #
# easily modified as needed.                                            #
#                                                                       #
# To use these tools, just uncomment the lines that you need and run    #
# the code.                                                             #
#                                                                       #
#########################################################################

# Crack MD5 passwords with optional salt using a word list
from md5_cracker import Md5Cracker

hashed_password = '4b8f105f370310ddc137d141d350cf12'
salt = 'as807135%#'
cracker = Md5Cracker(hashed_password, salt)  # Appends the salt. Modify Md5Cracker() to prepend instead
cracker.start()  # Optionally takes a filename argument so you can supply other word lists

##########################################################################

# # Discover sub-pages at a URL with common names using a word list
# from dirbust import DirBuster
#
# URL = 'https://54-193-48-38-bank.vulnerablesites.net/ShadowBank/'
#
#
# # Sometimes the HTTP Response status will still be a 200 even though it's displaying a 404 Page
# # So, we need to define a custom function that defines what failure looks like
# def failure(response):
#     return "We're sorry, something went wrong" in response.text
#
#
# buster = DirBuster(URL, failure=failure)
# buster.start()
