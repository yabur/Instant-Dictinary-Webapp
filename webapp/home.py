import justpy as jp

class Home:
    path = "/"

    @classmethod
    def serve(cls,req):
        wp = jp.QuasarPage(tailwind=True)
        # wp = jp.WebPage()

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)



        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="left",
                            bordered=True)

        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)
        a_classes = "p-2 n-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qlist, text="Home", href="/home", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        jp.Br(a=qlist)


        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        container = jp.QPageContainer(a=layout)

        div=jp.Div(a=container, classes='bg-gray-200 h-screen') #main div
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl-m-2")
        jp.Div(a=div, text="""Elementum condimentum dictumst suspendisse varius torquent volutpat suspendisse dictum 
                   diam fermentum orci proin litora ante etiam. In potenti bibendum conubia torquent viverra suscipit nisl cras 
                   integer sem. Metus consectetuer, nisl litora. Taciti, ut lectus magnis maecenas quam bibendum. Arcu accumsan 
                   sollicitudin convallis egestas ultricies cum faucibus nostra mi quisque aptent pretium eros nec sociis nisl 
                   mauris lobortis proin feugiat ante Placerat. Pretium metus.vivamus faucibus nulla pellentesque Nulla et 
                   tincidunt. Conubia augue. Luctus pretium egestas curae; feugiat senectus. Imperdiet Metus. Torquent odio orci 
                   dapibus fermentum auctor neque fusce vitae eget mus nisi habitasse aliquet, felis. Et accumsan.
                """, classes="text-lg")
        return wp


    @staticmethod
    def move_drawer(widget,msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
