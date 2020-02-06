import requests

class roblox:
    GET = "https://api.roblox.com"

    #returns json array of groups,
    #- if failed or no groups, returns empty body: '{}'
    def userid2groups(idd):
        userId = str(idd)
        r = requests.get(
            str(roblox.GET
                +"/users/{}/groups")
            .format(userId)
            )
        return dict(r.json())

    #returns json array of friends,
    #- if failed or no friends, returns empty body: '{}'
    def userid2friends(idd):
        userId = str(idd)
        r = requests.get(
            str(roblox.GET
                +"/users/{}/friends")
            .format(userId)
            )
        return dict(r.json())

    #Returns User id from username,
    #- if user doesnt exist then returns NoneType.
    def username2userid(username):
        username = str(username)
        r = requests.get(
            str(roblox.GET
                +"/users/get-by-username/{}")
            .format(username)
            )
        try:
            this = r.json()['Id']
        except:
            this = None
        return this

    # Can user manage asset
    #- returns Bool (or NoneType if failed)
    def Bool_userid_can_manage_asset(idd, assetId):
        userId = str(idd)
        assetId = str(assetId)
        r = requests.get(
            str(roblox.GET
                +"/users/{}/canmanage/{}")
            .format(userId, assetId)
            )
        succ = bool(r.json()['Success'])
        if succ != True:
            final = None
        else:
            final = bool(r.json()['CanManage'])
        return final


    
def test():
    print("User Can Manage Asset: \r", end="");print(str(roblox.Bool_userid_can_manage_asset(1061770704, 63690008)))    
    print("Username2id: \r", end="");print(roblox.username2userid('MirrorzCFW'))
    print("Username2groups: \r", end="");print(roblox.userid2groups(1061770704))
    print("Username2friends: \r", end="");print(roblox.userid2friends(1061770704))

#Uncomment Below To Test!#
#test()
