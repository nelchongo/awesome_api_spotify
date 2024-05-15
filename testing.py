from lib.request.AuthorizationManager import AuthorizationManagerClass as auth_class
from lib.request.UserManager import UserManagerClass as user_class
from lib.aws.SecretManager import SecretsManagerClass

#Secrets
client_token = SecretsManagerClass('dev/awesome_api_spotify/client_token')
client_credentials = SecretsManagerClass('dev/awesome_api_spotify/client_credentials')

print("Initializing Auth Process...\n")
auth = auth_class(client_token, client_credentials)
print("\nInitializing Profile Request...\n")
user = user_class(auth = auth)
#user.get_me()

user.get_top(type = 'artists', time_range = 'short_term')