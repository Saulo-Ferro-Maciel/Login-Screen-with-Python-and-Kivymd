tamaño_patalla_login = (400,420)

box = '''
        
<Tela1>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:

            title: "Nheenga"
            size_hint_y:0.11
            elevation:20
            opacity: .99

        ScrollView:

            do_scroll_x: False
            do_scroll_y: True
            
            MDGridLayout:

                rows: 1
                padding: 20, 20
                spacing: 50, 50
                size_hint_y: None
                height: self.minimum_height
                row_default_height: 300
                FloatLayout:
                    MDTextField:
                        id: user
                        font_size: 18
                        size_hint_x: 0.9
                        hint_text: str('email:'.capitalize()).center(5)
                        pos_hint: {'center_x':0.5, 'center_y':0.6}
                        icon_right: 'email-outline'
                        icon_right_color: app.theme_cls.primary_color
                        width:200
                        helper_text: str('Email registrado').center(5)
                        helper_text_mode: "on_focus"
                        required: True

                    MDTextField:
                        id: password
                        size_hint_x: 0.9
                        hint_text: str('senha:'.capitalize()).center(5)
                        password: True
                        pos_hint: {'center_x':0.5, 'center_y':0.45}
                        icon_right_color: app.theme_cls.primary_color
                        width:200
                        helper_text: str('Senha cadastrada').center(5)
                        helper_text_mode: "on_focus"
                        required: True

                    MDIconButton:
                        id: password_buttom
                        icon: 'eye-off'
                        pos_hint: {'center_x':0.9, 'center_y':0.485}
                        opacity: 0.60
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        on_release: root.show_password()

                    MDTextButton:
                        text: 'esqueçeu a senha?'.capitalize()
                        pos_hint: {'center_x':0.5, 'center_y':0.10}
                        font_size: 15
                        on_press:
                            root.manager.transition.direction = 'right'
                            root.manager.current = 'tela3'

                    MDTextButton:
                        text: 'criar uma conta'.capitalize()
                        pos_hint: {'center_x':0.5, 'center_y':0.20}
                        font_size: 15
                        on_press:
                            root.manager.transition.direction = 'left'
                            root.manager.current = 'tela2'

                    MDRectangleFlatIconButton:
                        text: str('login'.upper()).center(30)
                        font_size: 14
                        icon: 'login'
                        theme_text_color: "Custom"
                        pos_hint: {'center_x':0.5, 'center_y':0.32}
                        size_hint_x:0.5
                        size_hint_y:0.1
                        on_release: root.login_date(user.text, password.text)
            
<Tela2>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "tela de cadastro".title()
            size_hint_y:0.11
            elevation:20
            opacity: .99
        FloatLayout:

            MDTextField:
                id: mail_user
                font_seize: 18
                size_hint_x: 0.9
                hint_text: ' email:'.title()
                pos_hint: {'center_x':0.5, 'center_y':0.75}
                icon_right: 'email-outline'
                icon_right_color: app.theme_cls.primary_color
                width:200
                helper_text: str('Cadastre um email').center(5)
                helper_text_mode: "on_focus"
                required: True

            MDTextField:
                id: password_new
                size_hint_x: 0.9
                hint_text: str('Digite uma senha:'.title()).center(5)
                password: True
                pos_hint: {'center_x':0.5, 'center_y':0.60}
                width:200
                helper_text: str('Crie uma senha com até 6 digitos').center(5)
                helper_text_mode: "on_focus"
                required: True
                max_text_length: 6

            MDIconButton:
                id: password_buttom2
                icon: 'eye-off'
                pos_hint: {'center_x':0.9, 'center_y':0.62}
                opacity: 0.60
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_release: root.show_password2()
                

            MDTextField:
                id: password_new_confimation
                size_hint_x: 0.9
                hint_text: str('Confirme sua senha:'.title()).center(5)
                password: True
                pos_hint: {'center_x':0.5, 'center_y':0.45}
                width:200
                helper_text: str('Confirme a senha').center(5)
                helper_text_mode: "on_focus"
                required: True

            MDIconButton:
                id: password_buttom3
                icon: 'eye-off'
                pos_hint: {'center_x':0.9, 'center_y':0.48}
                opacity: 0.60
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_release: root.show_password3()

            MDRectangleFlatIconButton:
                text: str('cadastrar'.lower()).center(3)
                font_size: 14
                icon: 'account-check-outline'
                theme_text_color: "Custom"
                pos_hint: {'center_x':0.5, 'center_y':0.20}
                size_hint_x:0.29
                size_hint_y:0.1
                on_release: 
                    root.create_login(mail_user.text, password_new.text, password_new_confimation.text)

            MDRectangleFlatButton:
                text: 'voltar'
                font_size: 14
                theme_text_color: "Custom"
                pos_hint: {'center_x':0.2, 'center_y':0.20}
                size_hint_x:0.25
                size_hint_y:0.1
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'tela1'
                    
<Tela3>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "recuperar conta".title()
            size_hint_y:0.11
            elevation:20
            opacity: .99
        FloatLayout:
            MDTextField:
                id: email_recupera
                font_seize: 18
                size_hint_x: 0.9
                hint_text: ' email cadastrado:'.title()
                pos_hint: {'center_x':0.5, 'center_y':0.75}
                icon_right: 'account-circle-outline'
                icon_right_color: app.theme_cls.primary_color
                width:200
                helper_text: ' email cadastrado'
                helper_text_mode: "on_focus"
                helper_font_size: 0.19

            MDRectangleFlatIconButton:
                text: 'recuperar'.lower()
                font_size: 14
                icon: 'account-search'
                theme_text_color: "Custom"
                pos_hint: {'center_x':0.5, 'center_y':0.20}
                size_hint_x:0.27
                size_hint_y:0.1
                on_release: root.reset_password(email_recupera.text)
               
            MDRectangleFlatButton:
                text: 'voltar'
                font_size: 14
                theme_text_color: "Custom"
                pos_hint: {'center_x':0.8, 'center_y':0.20}
                size_hint_x:0.25
                size_hint_y:0.1
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'tela1'
                 
<TelaInterior>: 
    ScreenManager:
        MDScreen:
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "Nheenga"
                    size_hint_y:0.11
                    elevation:20
                    opacity: .99
                    left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                MDTextField:
                    id: email_recupera
                    font_seize: 18
                    size_hint_x: 0.9
                    hint_text: ' email cadastrado:'.title()
                    pos_hint: {'center_x':0.5, 'center_y':0.55}
                    icon_right: 'account-circle-outline'
                    icon_right_color: app.theme_cls.primary_color
                    width:200
                Widget:
    MDNavigationDrawer:
        id: nav_drawer
        NavigationDrawer:  
    
ScreenManager:
    Tela1:
        name: 'tela1'
    Tela2:
        name: 'tela2'
    Tela3:
        name: 'tela3'
    TelaInterior:
        name: 'tela4'

             
'''

