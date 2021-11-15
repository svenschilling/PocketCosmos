#           POCKETCOSMOS
import kivy
from kivy import config
kivy.require('2.0.0')
from kivy.app import App
from kivy.lang import Builder

from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.config import Config

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


config.window_icon = 'media/icons/main.png'

# define screens
class WindowManager(ScreenManager):
    pass

class MainScreen(Screen):
    # change image according to its state || can i have dynamic id ?
    def play_on(self, instance):
        #self.ids.play_img.source = ''
        WindowManager.current = "play"
    def play_off(self, instance):
        self.ids.play_img.source = 'media/buttons/play_pressed.png'
    

class PlayScreen(Screen):
    snd = SoundLoader.load('media/sound/music/Beta1.ogg')
    snd.loop = True
    snd.play()
    pass

class OptionsScreen(Screen):
    pass

class SavegameScreen(Screen):
    pass

class LoadgameScreen(Screen):
    pass

class CreditsScreen(Screen):
    
    def logo_ascii(self):
        return print(r"""
                                                                                                                                                                                                                                                               
                                                                                                                                                          .oOxol:,..                                                                                                                                        
                                                                                                                                                          ;KMMMMMWX0kl.                                                                                                                                     
                                                                                                                                                          lNMMMMMMMMWk.                                                                                                                                     
                                                                                                                                                         .kMMMMMMMMM0,                                                                                                                                      
                                                                                                                                                         ,KMMMMMMMMX:                                                                                                                                       
                                                                                                                                                         cNMMMMMMMNl.                                                                                                                                       
                                                                                                                                                        .dWMMMMMMWx.                                                                                                                                        
                                                                                                                                                        'OMMMMMMWO'                                                                                                                                         
                                                                                                                                                        :XMMMMMMK;                                                                                                                                          
                                                                                                                             ..........   ....         .dWMMMMMXc                                                                                                                                           
                                                                                                                       ......'''''''''''.'',,,'..      .OMMMMMNo.                                                                                                                                           
                                                                                                              ...........'''''''.....',,,,,,'..,'.     ;KMMMMWk.                                                                                                                                            
                                                                                                          ............''........'''.',,....''....'.  ..lNMMMM0,                                                                                                                                             
                                                                                                       ......... ...''...........',;;;'.    .,'. .'. .;kMMMMK:    ...''...                                                                                                                                  
                                                                                                     .......    ...'''...',,,,,,,;;;;;;;,.   .''..'. ;xKMMMNl.  .'''..'',,..                                                                                                                                
                                                                                                   ......      ..'''''''........;;'...';::,.  .''....lKNMMWd. ..... ...',,,,''.....                                                                                                                         
                                                                                                 ......       ..'''''..       .,;.     ..';;'. .'....xWWMWO'.... ..'''....','...'''..                                                                                                                       
                                                                                                .....        .''''..         .;;....',,,,',;:,. .'..;0MMM0;.....''..      .,,......''..                                                                                                                     
                                                                                               .....        .'''..          .;;,',;;,'....',:c;.....lXMMXl....'..  ...''',,,;,'''.''''...                                                                                                                   
                                                                                              .....        .'''..          .,:::;'.         .':,..',kWMNd'..'....,;:::;;;;;;;,'......'''..                                                                                                                  
                                                                                             .....        ..''.           .,::;..             .;'.':0WNO;.'..';ccc:,'......';;,,'... ...'....                                                                                                               
                    .:lllllllllllllc:,.                                            .clllll;. ....        ..''.            '::,.                .,''oX0dc'',,;;,',:dkOOkOOOkxxl,..','.. .''......                                                                                                            
                    ;XMMMMMMMMMMMMMMMWKd'                                          ;XMMMMMO'.....        .''.            .;cllccccc'            ',;xKo;;;;,.. .;dKWMMMMMMMMMMWKd,..','...'.......                                                                                                           
                    ;XMMMMMMN0O0XWMMMMMM0,      .';::::;'.            .';:::;'.    :XMMMMMO'........... ..',;;clllc;'.  .,:;xWMMMMWd.           .:lkxccc;.   'xNMMMMMWXOOkxxKNMWO, ..',,;loolllc;'.         .;:ccc:,.      .......  .,:::,.    .;:::,.          .';::::;'.          .,:cccc;.               
                    ;XMMMMMMO.  'xWMMMMMWd.  .ckKNWMMMMWN0x:.      .ckKNWMMMWN0x;  ;XMMMMMO'..'o0KXX0d' .:x0NWMMMMMWX0o,':llOWMMMMWOc;.         .cddl:;'    ,OWMMMMMNd'.':,,:ldl,.  .:kKNWWMMMMWNKx:.    .lOXWMMWWWNXx;   'kKKKKKxlxXWMMMWKd,:kXWMMMWXx'     .ckKNWMMMMWNKx:.    .:kXWMMMWWNXk:.            
                    ;XMMMMMMk.   cNMMMMMWo .lKWMMMWOoo0WMMMW0;   .cKWMMMMN0xdx0NNo.;XMMMMMO'.:OWMMWKl. .lXWMMMXkodKWMMWXxlxNMMMMMMMMWWo.      .',oxo:.     .xWMMMMMWd.  .,:::.     'xNMMMMNOdxXMMMMNk,  .kWMMMM0c,,:x0d.  ,KMMMMMWXKXWMMMMMWNXXXWMMMMMMk.  .cKWMMMWOoo0WMMMW0;  .dNMMMMXo,,:d0x'            
                    ;XMMMMMM0;.'l0MMMMMWO'.oNMMMMWx.  .OMMMMMX:  oNMMMMM0:.   .,c' ;XMMMMMO:oXMMMNx'   :XMMMMNo...cKMMMMNdckXMMMMMMXOk:     .':k0KXkl'.    ;KMMMMMMK;    .:c;.    'OWMMMMNx,..:XMMMMMO' :XMMMMM0c'....    ,KMMMMM0:..dNMMMMMXc..lXMMMMMK,  oNMMMMWx.  .kMMMMMX: '0MMMMMXo,.. .              
                    ;XMMMMMMWXXNWMMWNKkc. ,KMMMMMN:    oWMMMMMk.,0MMMMMNc          ;XMMMMMNXWMMMWk.   .xWMMMMWK000KNMMMMMk..dWMMMMWd.       ,xKWMMWWO:..   :XMMMMMMK;    .;c,.    lNMMMMMKc.. .OMMMMMWo..kWMMMMMWNX0xc.   ,KMMMMMk.  ,KMMMMMO.  '0MMMMMK, ,0MMMMMNc    lWMMMMMk..dNMMMMMMWX0kl'             
                    ;XMMMMMMKdlccc:;'.    ;XMMMMMX:    lWMMMMMO.;KMMMMMX;          ;XMMMMMWWMMMMMNd.  .kMMMMMMNKKKKKKKXXXx..dWMMMMWd.      .:kNMMMMW0c;'.  'OMMMMMMWx.   .;:'    .oWMMMMMKc.. .kMMMMMWd. .ckKNWMMMMMMWKc  ,KMMMMMk.  ,KMMMMMO.  '0MMMMMK, ;KMMMMMN:    lWMMMMMO. .:x0XWMMMMMMMXl.           
                    ;XMMMMMMk.            .OMMMMMWo   .xWMMMMWo .kMMMMMWd.      .  ;XMMMMM0xKMMMMMWx. .lNMMMMWk,......:do, .dWMMMMWd.       .oKNWWW0d;..    cXMMMMMMNk;. .::,;ox:.:XMMMMMXo'. ,0MMMMMXc.    ..;ckNMMMMM0' ,KMMMMMk.  ,KMMMMMO.  '0MMMMMK, .kMMMMMWo   .dWMMMMWo     ..,cxXMMMMMK;           
                    ;XMMMMMMk.             ,0WMMMMKl',oXMMMMNd.  ,OWMMMMNk:'',ck0l.;XMMMMMO,;0WMMMMWk' 'xNMMMMNOl;,,;o0NO:. oWMMMMM0:'.     .;oO0kk:....    .:0WMMMMMMNKkk0KKNMMK:.lXMMMMWKo;:kWMMMMXo..ckkc.. .cKMMMMWk. ,KMMMMMk.  ,KMMMMMO.  '0MMMMMK,  ,0WMMMMXl',oXMMMMNx. ,xkl'. .;0MMMMM0'           
                    ;XMMMMMMk.              .oKWMMMWNNWMMWNO:.    .l0WMMMMWNNNWXx' ;XMMMMMO. ,kWMMMMWO,.,o0NWMMMMWNNWWXOo:. 'kWMMMMMNXO,    .:loo:'.          .l0NWMMMMMMMMMMWKd;. .;kXWMMMWNWMMMWXk:...;kNWXK0KNMMMWXx.  ,KMMMMMk.  ,KMMMMMO.  '0MMMMMK,   .o0WMMMWNNWMMMNO:.  .dXWNK00NWMMMNk,            
                    .coolloo;                 .;ldkOOOkxo:'         .;lxkOOOxo:.   .coollo:.  .:odddxd:..',cokOOkkkdoll,';;. .:okOOOko:.  .,:cxo::.             .,cdxOO0KKOdl;.      .'cxO00OOkxo:'....   'cdkOOOkxo:'    .cooooo;   .cooooo:.  .:oollo:.     .;ldkOOOkxoc'       .:oxkOOOxdc'              
                                                                                                  ........''.',,..   .;'..;;.    ...    ..,;;d0l;c.                   .,c;.            .''....     ....                                                                                                     
                                                                                                    ......''...','...';'  .';,..      ..''''lX0;,c,                   .::.            ..'..       .....                                                                                                     
                                                                                                      ....'''. ..','',;'.   ..',,,,,,'.....;0Wx..;;.                .':coddddddddddddoooodddddddddoodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddo'           
                                                                                                        ....''......',;,'''.''',,,,.......'kWXl..'',.             ..;::;dNXKKKXNXkd0X0OOKNWWNXXNNXKKXXWMMMMMMWXKKWMMMMMMMMMMMMMMMMMMMMMMWNXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl           
                                                                                                           ..''''''.',;;,;;,,''...  ......oNMO;..'.';'..       ..';;;:;.oKc.,,'cx:'lxloooclOx,,oddOKXNWKkxkKNx''dNMWKOxkKWMMW0kk0WW0kxOXXc'xX0kxONXOOO0WMWKkk0KOOXXOK0kk0XklxXWKkxOXN00OkO0kkKWNl           
                                                                                                             ..'''....,,...      ..... ..cXMWx'. '..':cc;''''',;,'..,;..o0; ., 'o'.;, .c,  cl..,. cKNNd.'c'.l, .kWMXo:'.,0MMO'.,oOo.,c.,o, lkc;..cl..lkNMO'.'lk:.::,c'.,ox, .xd..'.:l..:..;;.,0Nl           
                                                                                                               ..'''..','..........  ...;0MMNl.. .'. .,;:;'.....  .,,.  l0; .,..,. ;, :Xx..lo..l, :XWNl ,d'.c: ;XMWx..' .kMM0c,..o: ;o..l, ::.'. ,: ,KMMM0l,..xO, .xOl,..dc ,kl .;;:c.'x; ld..ONl           
                                                                                                                 .....',,,''....   ....'kWMM0,..  .'.  .';;'..   .,,.   lKd:;;;col:ddlkNXdcodclkdlkNMMXxoookXOokNMMKoododKMMXkdodKKdlooOXkokklodlkkoxNMMMXkdod00;.dNXkdodK0olOKxlox00dxKkoO0odXNl           
                                                                                                                       .','..   ..... .dWMMMx....  .'.   .';:;,'',;'....cdddooddddodxkkkkkxxxddxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd;'cxkkkkkkkkkkkkkkkkkkkkkkkkkkkkx,           
                                                                                                                        ..',''.....  .lNMMMNc  ..   .''.   ..,;;;,''''.......'''... ..........                                                                                                              
                                                                                                                          ......     ;KMMMMK;  .'.   ..''.. .',,'''.........''............                                                                                                                  
                                                                                                                                    'OMMMMMk.   .'..   ..'''','....'''''''''...........                                                                                                                     
                                                                                                                                   .xWMMMMWo.    .''.....',''''''''''''.........                                                                                                                            
                                                                                                                                  .oNMMMMMX:      ...'''.... ..........                                                                                                                                     
                                                                                                                                  cXMMMMMMO.                                                                                                                                                                
                                                                                                                                 ;0MMMMMMWd.                                                                                                                                                                
                                                                                                                                .kWMMMMMMNc                                                                                                                                                                 
                                                                                                                               .dWMMMMMMM0,                                                                                                                                                                 
                                                                                                                              .lNMMMMMMMWx.                                                                                                                                                                 
                                                                                                                              :KMMMMMMMMNc                                                                                                                                                                  
                                                                                                                             'OMMMMMMMMMK;                                                                                                                                                                  
                                                                                                                             ,x0XWMMMMMMk.                                                                                                                                                                  
                                                                                                                               ..;codkO0c                                                                                                                                                                   
                                                                                                                                       .                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                            
                                                                                                                                                      
        
        
        
        
        
        
        """)

    def creditlines(self):
        return [
            
            '#### Credits ####',
            '',
            '## Devs ##',
            'gandie -- main developer -- lars@bergmann82.de',
            'https://github.com/gandie',
            '',
            'sven -- uix developer -- sven.schilling@gmail.com',
            'https://github.com/svenschilling',
            '',
            '## Artists ##',
            'sven -- layout, graphics --',
            'https://www.artstation.com/svenschilling',
            '',
            'dude -- layout, graphics, music --',
            'https://www.instagram.com/ikone.official/',
            '',
            'rafikibeats -- music --',
            'https://soundcloud.com/rafikibeats',
            '',
            '## Testers ##',
            'McStorm',
            'mattis',
            'nichtpeter',
            'jean_borrow',
            'Peter Oswald',
            'Uedii',
            'and many many more people from FLAFLA',
            '',
            '## Thanks to ##',
            'Everyone else i forgtot to mention'
        ]

# load that kv file
kv = Builder.load_file('PocketCosmos.kv')

class PocketCosmosApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainScreen())
        sm.add_widget(PlayScreen())
        sm.add_widget(OptionsScreen())
        sm.add_widget(SavegameScreen())
        sm.add_widget(LoadgameScreen())
        sm.add_widget(CreditsScreen())
        Window.size = (800,600)
        self.title = "Pocket Cosmos - Birth of a solar system"
        self.icon = '/media/icons/main.png'
        return sm
    

PocketCosmosApp().run()