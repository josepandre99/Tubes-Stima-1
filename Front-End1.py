import time
import random
import kivy
kivy.require('1.10.1')
 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.properties import StringProperty, ObjectProperty
from kivy.config import Config
from kivy.core.audio import SoundLoader
from functools import partial

import greedy

Config.set('graphics', 'width', '850')          #Windows size
Config.set('graphics', 'height', '300')
Config.write()

# make a deck of cards
numbers = list(['1','2','3','4','5','6','7','8','9','10','11','12','13'])
symbols = list(['Spade','Heart','Diamond','Club'])
deck = list()
CardInput= list() # buat masukan ke solver

for i in numbers :
    for j in symbols :
        deck.append(i+','+j)

# shuffle the cards
random.shuffle(deck)
sound = SoundLoader.load('data/shuffle.wav')
sound.play()

class CustomWidget(Widget):
    bt1 = ObjectProperty(None)

    def draw(self) :
        if (self.ids.draw.count < 13) :
            #Draw animation
            self.ids.card1.x=0
            self.ids.card2.x=0
            self.ids.card3.x=0
            self.ids.card4.x=0

            animate1= Animation(x=200+self.ids.card1.x, y= self.ids.card1.y,duration=0.5,t='out_expo')
            animate2= Animation(x=350+self.ids.card2.x, y= self.ids.card2.y,duration=0.5,t='out_expo')
            animate3= Animation(x=500+self.ids.card3.x, y= self.ids.card3.y,duration=0.5,t='out_expo')
            animate4= Animation(x=650+self.ids.card4.x, y= self.ids.card4.y,duration=0.5,t='out_expo')

            #Deck handling            
            self.ids.card1.background_normal = 'data/card.png'
            self.ids.card2.background_normal = 'data/card.png'
            self.ids.card3.background_normal = 'data/card.png'
            self.ids.card4.background_normal = 'data/card.png'

            CardInput.clear()
            self.ids.card1.background_normal = 'data/' + deck[0] + '.png'
            self.ids.card1.col = .88, .88, .88, 1
            CardInput.append(''.join(x for x in deck[0] if x.isdigit()))       
            deck.remove(deck[0])
            self.ids.card2.background_normal = 'data/' + deck[0] + '.png'
            self.ids.card2.col = .88, .88, .88, 1
            CardInput.append(''.join(x for x in deck[0] if x.isdigit()))     
            deck.remove(deck[0])
            self.ids.card3.background_normal = 'data/' + deck[0] + '.png'
            self.ids.card3.col = .88, .88, .88, 1
            CardInput.append(''.join(x for x in deck[0] if x.isdigit()))       
            deck.remove(deck[0])
            self.ids.card4.background_normal = 'data/' + deck[0] + '.png'
            self.ids.card4.col = .88, .88, .88, 1
            CardInput.append(''.join(x for x in deck[0] if x.isdigit()))       
            deck.remove(deck[0])
            self.ids.draw.count += 1
            if (self.ids.draw.count == 13) :
                self.ids.deckaku.background_color = 0, 0, 0, 0
                self.remove_widget(self.bt1)       #remove button Draw

            #Start Animation
            animate1.start(self.ids.card1)
            animate2.start(self.ids.card2)
            animate3.start(self.ids.card3)
            animate4.start(self.ids.card4)

        else :
            self.ids.card1.background_color = 0, 0, 0, 0
            self.ids.card2.background_color = 0, 0, 0, 0
            self.ids.card3.background_color = 0, 0, 0, 0
            self.ids.card4.background_color = 0, 0, 0, 0 
            
        self.ids.jawaban.text = ""             #remove answer 
        self.ids.value.text = ""

    def solve(self):
        if len(CardInput) != 0 :
            self.ids.jawaban.text = greedy.hasil(CardInput)
            self.ids.value.text = str(eval(self.ids.jawaban.text))

class Kartu24App(App): 
    def build(self):
        return CustomWidget()
 
customWidget = Kartu24App()
 
customWidget.run()  