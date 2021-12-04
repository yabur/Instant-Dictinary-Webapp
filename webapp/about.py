import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage()
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page", classes="text-4xl m-2")
        jp.Div(a=div, text="""Elementum condimentum dictumst suspendisse varius torquent volutpat suspendisse dictum 
            diam fermentum orci proin litora ante etiam. In potenti bibendum conubia torquent viverra suscipit nisl cras 
            integer sem. Metus consectetuer, nisl litora. Taciti, ut lectus magnis maecenas quam bibendum. Arcu accumsan 
            sollicitudin convallis egestas ultricies cum faucibus nostra mi quisque aptent pretium eros nec sociis nisl 
            mauris lobortis proin feugiat ante Placerat. Pretium metus.vivamus faucibus nulla pellentesque Nulla et 
            tincidunt. Conubia augue. Luctus pretium egestas curae; feugiat senectus. Imperdiet Metus. Torquent odio orci 
            dapibus fermentum auctor neque fusce vitae eget mus nisi habitasse aliquet, felis. Et accumsan.
         """, classes="text-lg")
        return wp
