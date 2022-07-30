import requests as rq

apikey='AIzaSyD22LrjWiatu2O569QJA8G0Fl3Slmxuu2I'# the web api key

# Nesse vídeo, eu, mostro como o projeto ficou com a implementação do firebase

s, idToken = 0,0
def NewUser(email,password):
    details={
        'email':email,
        'password':password,
        'returnSecureToken': True
    }
    s = 0
    # send post request
    r=rq.post('https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={}'.format(apikey),data=details)
    #check for errors in result
    if 'error' in r.json().keys():
        return print({'status':'error','message':r.json()['error']['message']})
    #if the registration succeeded
    if 'idToken' in r.json().keys() :
        s = {'status':'success','idToken':r.json()['idToken']}
        idToken = s['idToken']
        details={
        'idToken':idToken
        }
        r=rq.post('https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={}'.format(apikey),data=details)
        if 'error' in r.json().keys():
            return print({'status':'error','message':r.json()['error']['message']})
        if 'users' in r.json():
            return print({'status':'success','data':r.json()['users']})
        
        return print(s)
    

NewUser('maciel.ferro@acad.ifma.edu.br', '123456')



def SignIn(email,password):
    details={
        'email':email,
        'password':password,
        'returnSecureToken': True
    }
    #Post request
    r=rq.post('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}'.format(apikey),data=details)
    #check for errors
    if 'error' in r.json().keys():
        print("NOt blz")
        return {'status':'error','message':r.json()['error']['message']}
    #success
    if 'idToken' in r.json().keys() :
            print("Blz")
            return {'status':'success','idToken':r.json()['idToken']}

SignIn('maciel.ferro@acad.ifma.edu.br', '123456')

def SendResetEmail(email):
    headers = {
        'Content-Type': 'application/json',
    }
    data={"requestType":"PASSWORD_RESET","email":email}
    r = rq.post('https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={}'.format(apikey), data=data)
    if 'error' in r.json().keys():
        return {'status':'error','message':r.json()['error']['message']}
    if 'email' in r.json().keys():
        return {'status':'success','email':r.json()['email']}

SendResetEmail('maciel.ferro@acad.ifma.edu.br')

def GetData(idTokent):
    details={
        'idToken':idTokent
    }
    r=rq.post('https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={}'.format(apikey),data=details)
    if 'error' in r.json().keys():
        return print({'status':'error','message':r.json()['error']['message']})
    if 'users' in r.json():
        return print({'status':'success','data':r.json()['users']})
GetData(idToken)
