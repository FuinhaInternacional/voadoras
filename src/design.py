__author__ = 'FuinhaInternacional'
FACE = 'http://thumbs.dreamstime.com/z/joker-playing-card-19231679.jpg'
CH = CV = 50


class Celula:
    def __init__(self, html, xy, grade):
        self.ecelula=html.DIV("-")
        self.ecelula.style.backgroundColor="black"
        self.ecelula.style.width="9%"
        self.ecelula.style.margin="9%"
        self.ecelula.style.float="left"
        grade.egrade<=self.ecelula

    def voa(self, evento):
        self.deque.voa()

    def voar(self, delta):
        dx, dy = delta
        x, y = self.pos
        xy = self.pos = x + dx, y + dy
        ct = self.e_carta
        ct.style.left, ct.style.top = xy


class Grade:
    def __init__(self, html, tela):
        self.tela = tela
        self.egrade= html.DIV()
        tela<=self.egrade
        self.grade = [Celula(html, (x*4, 10), self) for x in range(81)]


    def voa(self):
        [carta.voar((100, 100)) for carta in self.deque]

    def __le__(self, other):
        self.tela <= other


def tabuleiro(tela, html):
    tabul = html.DIV()
    tela <= tabul


def embaralha(tela, html):
    pass


def voa(tela, html):
    pass


def main(html, doc):
    tela = doc["main"]
    #html = gui.html
    splash = html.DIV(" ")
    tela <= splash
    tela.style.backgroundColor="black"
    #tabuleiro(tela, html)
    #embaralha(tela, html)
    #voa(tela, html)
    grade=Grade(html, tela)