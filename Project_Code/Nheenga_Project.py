from box import*

from kivy.lang import Builder as bd # cria o metódo construir 
from kivy.core.window import Window as tamaño_pantalla # regula o tamanho da janela
from kivy.uix.screenmanager import Screen # tela

from kivymd.app import MDApp as md_application # cria a janela
from kivymd.uix.boxlayout import BoxLayout as Box

tamaño_pantalla.size = tamaño_patalla_login 

class NavigationDrawer(Box):
    pass

class TelaInterior(Screen):
    pass

class Tela3(Screen):
   def reset_password(self, email_recupera ):
        import requests as rq

        apikey='AIzaSyD22LrjWiatu2O569QJA8G0Fl3Slmxuu2I'

        data={"requestType":"PASSWORD_RESET","email":email_recupera}
        r = rq.post('https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={}'.format(apikey), data=data)
        if 'error' in r.json().keys():
            return {'status':'error','message':r.json()['error']['message']}
        if 'email' in r.json().keys():
            self.ids.email_recupera.text = str('')
            self.manager.transition.direction = 'down'
            self.manager.current = 'tela1'
            return {'status':'success','email':r.json()['email']}

class Tela2(Screen):
    def show_password2(self):
        if self.ids.password_new.password is False:
            self.ids.password_buttom2.icon = 'eye-off'
            self.ids.password_new.password = True
        else:
            self.ids.password_buttom2.icon = 'eye'
            self.ids.password_new.password = False

    def show_password3(self):
        if self.ids.password_new_confimation.password is False:
            self.ids.password_buttom3.icon = 'eye-off'
            self.ids.password_new_confimation.password = True
        else:
            self.ids.password_buttom3.icon = 'eye'
            self.ids.password_new_confimation.password = False

    def create_login(self,mail_user, password_new, password_new_confimation):
        aroba, contador, s = '@', 0, 0
        if mail_user != " ":
            if mail_user.count(aroba) >= 1:
                if password_new == password_new_confimation:
                    contador = 5
                    import requests as rq

                    apikey='AIzaSyD22LrjWiatu2O569QJA8G0Fl3Slmxuu2I'

                    if contador == 5:
                        if password_new_confimation == password_new:
                            data = {
                                'email': mail_user,
                                'password':password_new,
                                'returnSecureToken': True
                            }
                            r=rq.post('https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={}'.format(apikey),data=data)
                            if 'error' in r.json().keys():
                                self.ids.password_new_confimation.text = str(''.title())
                                self.ids.password_new.helper_text = str('Senha Invalída/Ela deve ter 6 digitos').center(5)
                                self.ids.mail_user.helper_text = str('email inválido/já cadastrdo'.title()).center(5)
                                return {'status':'error','message':r.json()['error']['message']}
                            #if the registration succeeded
                            if 'idToken' in r.json().keys() :
                                self.ids.password_new_confimation.text = str(' '.title())
                                self.ids.mail_user.text = str(' '.title())
                                self.manager.transition.direction = 'down'
                                self.manager.current = 'tela1'
                                contador = 0
                                s = {'status':'success','idToken':r.json()['idToken']}
                                
                                s = s
                                
                                z = s['idToken']

                                idToken= z #token

                                headers = {
                                    'Content-Type': 'application/json',
                                }
                                data='{"requestType":"VERIFY_EMAIL","idToken":"'+idToken+'"}'
                                r = rq.post('https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={}'.format(apikey), headers=headers, data=data)
                                if 'error' in r.json().keys():
                                    return {'status':'error','message':r.json()['error']['message']}
                                if 'email' in r.json().keys():
                                    return {'status':'success','email':r.json()['email']}
                                return s

                else:
                    self.ids.password_new_confimation.helper_text = str('valores diferentes'.title()).center(5)
                    self.ids.password_new.helper_text = str('valores diferentes'.title()).center(5)
        else:
            self.ids.mail_user.helper_text = str('email inválido'.title()).center(5)
            if password_new != password_new_confimation:
                self.ids.password_new_confimation.helper_text = str('valores diferentes'.title()).center(5)
                self.ids.password_new.helper_text = str('valores diferentes'.title()).center(5)
          
class Tela1(Screen):
    def show_password(self):
        if self.ids.password.password is False:
            self.ids.password_buttom.icon = 'eye-off'
            self.ids.password.password = True
        else:
            self.ids.password_buttom.icon = 'eye'
            self.ids.password.password = False

    def login_date(self, user, password):
        import requests as rq

        apikey='AIzaSyD22LrjWiatu2O569QJA8G0Fl3Slmxuu2I'# the web api key
        aroba = '@'

        if user == " " or user == "":
            self.ids.user.helper_text = str('email inválido'.title()).center(5)
            self.ids.user.text = str("")
            if password == " " or password == "":
                self.ids.password.helper_text = str('senha inválida'.title()).center(5)
                self.ids.password.text = str("")
            elif user.count(aroba)!=1 and password == " ":
                self.ids.user.helper_text = str('email inválido'.title()).center(5)
                self.ids.password.helper_text = str('senha inválida'.title()).center(5)
                self.ids.password.text = str("")
                self.ids.user.text = str("")
        else:
            if user != "":
                if user.count(aroba)==1:
                    if password != "":
                        data={
                        'email':user,
                        'password':password,
                        'returnSecureToken': True
                        }
                        r=rq.post('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}'.format(apikey),data=data)
                        #check for errors
                        if 'error' in r.json().keys():
                            self.ids.user.helper_text = str('email inválido'.title()).center(5)
                            self.ids.password.helper_text = str('senha inválida'.title()).center(5)
                            self.ids.password.text = str("")
                            self.ids.user.text = str("")
                            return {'status':'error','message':r.json()['error']['message']}
                        #success
                        if 'idToken' in r.json().keys() :
                                self.manager.transition.direction = 'up'
                                self.manager.current = 'tela4'
                                return {'status':'success','idToken':r.json()['idToken']}
   
class App_principal(md_application):
    def build(self):
        App_principal.title = "Nheega"
        self.theme_cls.primary_palette = "Purple"
        app_layout= bd.load_string(box)
        return app_layout

if __name__ == '__main__':
    project = App_principal()
    project.run()
