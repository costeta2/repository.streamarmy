import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , datetime , time , shutil , urlresolver , random , liveresolver , hashlib
from resources . libs . common_addon import Addon
from resources . libs . modules import regex
import base64
from metahandler import metahandlers
import os
if 64 - 64: i11iIiiIii
#################################################################
#                     STREAM ARMY BASE CODE                     # 
#                                                               #
#                                                               #
#                                                               #
#################################################################
#                     MODDED BY @NEMZZY668                      # 
#                              &                                #
#                           @_Manc_                             #
#                                                               #
#################################################################
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
I1IiI = 'plugin.video.streamarmy'
o0OOO = Addon ( I1IiI , sys . argv )
iIiiiI = xbmcaddon . Addon ( id = I1IiI )
Iii1ii1II11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'fanart.jpg' ) )
iI111iI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'fanart.jpg' ) )
IiII = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'icon.png' ) )
iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'search.jpg' ) )
i1i1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'next.png' ) )
O0oo0OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' , 'plugin.video.sportsdevil' ) )
I1i1iiI1 = base64 . b64decode ( b'aHR0cDovL3d3dy5zdHJlYW1hcm15LmNvLnVrL01haW4vTWVudS54bWw=' )
iiIIIII1i1iI = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='
o0oO0 = '&maxResults=50&key=AIzaSyCebQaY3SIk6VlFNzDlYy4nqNva9c9N4CI'
oo00 = 'https://www.googleapis.com/youtube/v3/playlistItems?pageToken='
o00 = '&part=snippet&playlistId='
Oo0oO0ooo = '&maxResults=50&key=AIzaSyCebQaY3SIk6VlFNzDlYy4nqNva9c9N4CI'
o0oOoO00o = iIiiiI . getSetting ( 'password' )
i1 = iIiiiI . getSetting ( 'Conspiracy Password' )
oOOoo00O0O = iIiiiI . getSetting ( 'enable_meta' )
i1111 = 'http://pastebin.com/raw/4B2BhvJz'
i11 = base64 . b64decode ( b'aHR0cDovL2dldGFmbGl4LnVzL2FkZG9uL3lvdXR1YmUucGhw' )
I11 = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmcgui . DialogProgress ( )
oOo0oooo00o = 'http://www.streamarmy.co.uk/Main/Exceptions/Exceptions.xml'
oO0o0o0ooO0oO = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"
oo0o0O00 = [ "aliez" , "alldebrid" , "allvid" , "anistream" , "anyfiles" , "apnasave" , "blazefile" , "castamp" , "clicknupload" , "cloudmailru" , "cloudy" , "daclips" , "dailymotion" , "divxstage" , "ecostream" , "estream" , "exashare" , "facebook" , "fastplay" , "filepup" , "fileweed" , "flashx" , "googlevideo" , "gorillavid" , "grifthost" , "hugefiles" , "indavideo" , "jetload" , "kingfiles" , "letwatch" , "letwatch" , "mailru" , "megadebrid" , "megamp" , "mersalaayitten" , "movdivx" , "movpod" , "movshare" , "mpengine" , "mpstream" , "mpupload" , "myvidstream" , "nosvideo" , "novamov" , "nowvideo" , "ok" , "ol_gmu" , "ol_openload" , "play_net" , "play_playedto" , "playhd" , "playwire" , "premiumize_me" , "purevid" , "putload" , "rapidvideo" , "rapidvideocom" , "realdebrid" , "rpnet" , "rutube" , "simplydebrid" , "speedplay" , "speedvideo" , "stagevu" , "streamcloud" , "streamenet" , "streaminto" , "streamplay" , "teramixer" , "thevid" , "thevideo" , "thevideos" , "trollvid" , "tudou" , "tunepk" , "tusfiles" , "twitch" , "uploadaf" , "uploadx" , "uploadz" , "uptobox" , "userscloud" , "usersfiles" , "veeHD" , "veeHD" , "oveoh" , "vidabc" , "vidcrazynet" , "videa" , "videobee" , "videocloud" , "videoget" , "videohut" , "videoraj" , "videorev" , "videoweed" , "videowood" , "videozoo" , "vidlox" , "vidmad" , "vidme" , "vidto" , "vidtodo" , "vidup_me" , "vidup_vidup_org" , "vidup_vidzi" , "vimeo" , "vivosx" , "vk" , "vshare" , "vshareeu" , "watchers" , "watchonline" , "watchpass" , "watchvideo" , "weshare" , "xvidstage" , "yourupload" , "youtube" , "youwatch" , "zevera" , "zstream" ]
if 68 - 68: o00oo . iI1 + OoOooOOOO
if 45 - 45: OoOO + I1iiiiI1iII
def IiIi11i ( link , splitting = '\n' ) :
 iIii1I111I11I = urllib2 . Request ( link )
 try :
  OO00OooO0OO = urllib2 . urlopen ( iIii1I111I11I )
 except IOError :
  return [ ]
  if 28 - 28: iIii1
 else :
  oOOoO0 = OO00OooO0OO . read ( )
  return oOOoO0 . split ( splitting )
  if 59 - 59: oO * O0OOooO % I1IiiI . OoO0O00 % OoooooooOO
iiIIiIiIi = IiIi11i ( oOo0oooo00o )
if 38 - 38: OoOO / Oo0Ooo
try :
 OooO0 = xbmc . getInfoLabel ( "System.BuildVersion" )
 II11iiii1Ii = float ( OooO0 [ : 4 ] )
 if 70 - 70: o00oo / iIii1I11I1II1 % O0OOooO % i11iIiiIii . I1IiiI
 if II11iiii1Ii >= 17.0 and II11iiii1Ii <= 17.9 :
  if 68 - 68: OoOooOOOO + iI1 . iIii1I11I1II1 - iIii1 % iIii1I11I1II1 - O0OOooO
  oOOO00o = [ "special://cache" ,
 "special://temp/" ,
 "/private/var/mobile/Library/Caches/AppleTV/Video/Other" ,
 "/private/var/mobile/Library/Caches/AppleTV/Video/LocalAndRental" ]
  if 97 - 97: OoOooOOOO % OoOooOOOO + II111iiii * I1iiiiI1iII
  for o0o00o0 in oOOO00o :
   if "special" in o0o00o0 :
    o0o00o0 = xbmc . translatePath ( o0o00o0 )
   if os . path . exists ( o0o00o0 ) :
    iIi1ii1I1 = os . path . join ( o0o00o0 , "archive_cache" )
    if not os . path . exists ( iIi1ii1I1 ) :
     os . makedirs ( iIi1ii1I1 )
except : pass
if 71 - 71: oO . O0
def o0OO0oo0oOO ( input_data , key ) :
 if 54 - 54: I1IiiI % II111iiii % II111iiii
 iI1i11Iiii = ""
 for iI in input_data :
  iI1i11Iiii += chr ( ord ( iI ) ^ key )
  if 28 - 28: iI1 - iIii1 . iIii1 + OoOoOO00 - OoooooooOO + O0
 return iI1i11Iiii
 if 95 - 95: OoO0O00 % o00oo . O0
def I1i1I ( input_data , password ) :
 if 80 - 80: OoOoOO00 - OoO0O00
 OOO00 = 0
 for iI in password :
  OOO00 ^= ( ( 2 * ord ( iI ) + 3 ) & 0xff )
  if 21 - 21: OoooooooOO - OoooooooOO
 return o0OO0oo0oOO ( input_data , OOO00 )
 if 8 - 8: OoOoOO00
def o00O ( input_data , password = base64 . b64decode ( b"bGl2ZXJwb29s" ) ) :
 if 69 - 69: o00oo % oO - o0oOOo0O0Ooo + oO - O0 % OoooooooOO
 return I1i1I ( input_data , password )
 if 31 - 31: II111iiii - iI1 . oO % OoOoOO00 - O0
def iii11 ( text ) :
 if 58 - 58: iI1 * i11iIiiIii / OoOoOO00 % oO - I1ii11iIi11i / o00oo
 text = str ( text )
 text = text . replace ( '\\r' , '' )
 text = text . replace ( '\\n' , '' )
 text = text . replace ( '\\t' , '' )
 text = text . replace ( '\\' , '' )
 text = text . replace ( '<br />' , '\n' )
 text = text . replace ( '<hr />' , '' )
 text = text . replace ( '&#039;' , "'" )
 text = text . replace ( '&quot;' , '"' )
 text = text . replace ( '&rsquo;' , "'" )
 text = text . replace ( '&amp;' , "&" )
 text = text . replace ( '&#8211;' , "&" )
 text = text . replace ( '&#8217;' , "'" )
 text = text . replace ( '&#038;' , "&" )
 text = text . lstrip ( ' ' )
 text = text . lstrip ( '	' )
 if 50 - 50: I1IiiI
 return text
 if 34 - 34: I1IiiI * II111iiii % I1iiiiI1iII * OoOoOO00 - I1IiiI
def II1III ( ) :
 if 19 - 19: o00oo % i1IIi % o0oOOo0O0Ooo
 oo0OooOOo0 = xbmc . translatePath ( 'special://home/addons/' + I1IiI + '/addon.xml' )
 o0O = open ( oo0OooOOo0 ) . read ( )
 O00oO = o0O . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 I11i1I1I = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( O00oO ) )
 for oO0Oo in I11i1I1I :
  oOOoo0Oo = oO0Oo
  if 78 - 78: OoOooOOOO
 OO00Oo = "https://raw.githubusercontent.com/nemesis668/repository.streamarmy/master/addons.xml"
 if 51 - 51: iIii1 * o0oOOo0O0Ooo + OoOooOOOO + OoO0O00
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<addon id="' + I1IiI + '" name=".+?" version="(.+?)" provider-name=".+?">' ) . findall ( o0O0O00 ) [ 0 ]
 if 7 - 7: O0OOooO * OoO0O00 % o00oo . iIii1
 Ii1iIiII1ii1 ( '[B][COLOR lime]Your Current Version: ' + str ( oOOoo0Oo ) + '[/COLOR] | [COLOR yellow]Our Latest Version: ' + I11i1I1I + '[/COLOR][/B]' , 'url' , 999 , IiII , iI111iI )
 if 62 - 62: iIii1I11I1II1 * OoOoOO00
 i1OOO ( )
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 OO00Oo = I1i1iiI1
 o0O0O00 = Oo0oOOo ( I1i1iiI1 )
 I11i1I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0O00 )
 if 58 - 58: II111iiii * iI1 * I1ii11iIi11i / iI1
 for oO0Oo in I11i1I1I :
  try :
   if '<m3u>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 11 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<changelog>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<changelog>(.+?)</changelog>' ) . findall ( oO0Oo ) [ 0 ]
    Ii1iIiII1ii1 ( oO0o0OOOO , OO00Oo , 45 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<cmovies>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<cmovies>(.+?)</cmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 62 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<mflixcats>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<mflixcats>(.+?)</mflixcats>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 75 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<mflixpop>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<mflixpop>(.+?)</mflixpop>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 78 , O0O0OoOO0 , Iii1ii1II11i )
    if 49 - 49: I1IiiI % O0OOooO . O0OOooO . OoOooOOOO * O0OOooO
   elif '<cam>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<cam>(.+?)</cam>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 70 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<multisearch>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<multisearch>(.+?)</multisearch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 91 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<porncom>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<porncom>(.+?)</porncom>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 65 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<shighlights>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 68 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<pornscrape>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<pornscrape>(.+?)</pornscrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 16 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<sockshare>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<sockshare>(.+?)</sockshare>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 60 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<soccerstreams>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<soccerstreams>(.+?)</soccerstreams>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 55 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<afdah>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<afdah>(.+?)</afdah>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 52 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<vodly>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<vodly>(.+?)</vodly>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 60 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<top40>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<top40>(.+?)</top40>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 46 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<pornhd>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<pornhd>(.+?)</pornhd>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 41 , O0O0OoOO0 , Iii1ii1II11i , '' )
   elif '<docs>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<docs>(.+?)</docs>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 24 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<anime>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<anime>(.+?)</anime>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 32 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<cartoons>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 35 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<comics>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<comics>(.+?)</comics>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 38 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<filmon>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<filmon>(.+?)</filmon>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 26 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<music>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<music>(.+?)</music>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 28 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<hdmovies>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<hdmovies>(.+?)</hdmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 49 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<channel>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 6 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<tvput>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<tvputsput>(.+?)</tvput>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 13 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<watch>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<watch>(.+?)</watch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 30 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<moviescrape>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<moviescrape>(.+?)</moviescrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 15 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<moviescrapenorm>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<moviescrapenorm>(.+?)</moviescrapenorm>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 22 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<sportsdevil>' in oO0Oo :
    O0oOO0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     OO00Oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo ) [ 0 ]
     O0ooo0O0oo0 = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oO0Oo ) [ 0 ]
     oo0oOo = O0ooo0O0oo0
     o000O0o = "/"
     if not oo0oOo . endswith ( o000O0o ) :
      iI1iII1 = oo0oOo + "/"
     else :
      iI1iII1 = oo0oOo
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + OO00Oo
     OO00Oo = o0O0O00 + '%26referer=' + iI1iII1
     Ii1iIiII1ii1 ( oO0o0OOOO , OO00Oo , 4 , O0O0OoOO0 , Iii1ii1II11i )
    elif len ( O0oOO0 ) > 1 :
     oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     Ii1iIiII1ii1 ( oO0o0OOOO , oO0OOoo0OO , 8 , O0O0OoOO0 , Iii1ii1II11i )
     if 65 - 65: OoOO . iIii1I11I1II1 / O0 - OoOO
   elif '<folder>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    oO0OOoo0OO = re . compile ( '<folder>(.+?)</folder>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    if 21 - 21: I1IiiI * iIii1I11I1II1
    if oO0OOoo0OO in iiIIiIiIi :
     iiiI1I11i1 ( oO0o0OOOO , oO0OOoo0OO , 1 , O0O0OoOO0 , Iii1ii1II11i )
    else :
     iiiI1I11i1 ( oO0o0OOOO , oO0OOoo0OO , 20 , O0O0OoOO0 , Iii1ii1II11i )
   else :
    if 91 - 91: iIii1
    O0oOO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     iiIii = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     ooo0O = len ( I11i1I1I )
     for oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i in iiIii :
      if 'youtube.com/playlist' in OO00Oo :
       iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 2 , O0O0OoOO0 , Iii1ii1II11i )
      else :
       oOoO0o00OO0 ( oO0o0OOOO , OO00Oo , 2 , O0O0OoOO0 , Iii1ii1II11i )
    elif len ( O0oOO0 ) > 1 :
     oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     oOoO0o00OO0 ( oO0o0OOOO , oO0OOoo0OO , 3 , O0O0OoOO0 , Iii1ii1II11i )
     if 7 - 7: iI1 + oO + O0
     if 9 - 9: II111iiii . o0oOOo0O0Ooo - O0OOooO / o0oOOo0O0Ooo
  except : pass
  if 46 - 46: OoOooOOOO . iI1 * OoOooOOOO % i1IIi
  iIIiII ( )
  if 38 - 38: oO
def Ii1 ( url ) :
 if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / iI1 + OoOO
 OOOOoOoo0O0O0 = OOOo00oo0oO ( url )
 IIiIi1iI ( '[B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B] [B][COLOR lime]I[/COLOR][COLOR white]nformation[/COLOR][/B]' , OOOOoOoo0O0O0 )
 if 35 - 35: OoOO % O0 - O0
def i1OOO ( ) :
 OOOOoOoo0O0O0 = OOOo00oo0oO ( i1111 )
 if len ( OOOOoOoo0O0O0 ) > 1 :
  IiIIIi1iIi = xbmcaddon . Addon ( ) . getAddonInfo ( 'path' )
  ooOOoooooo = os . path . join ( os . path . join ( IiIIIi1iIi , '' ) , 'compare.txt' )
  II1I = open ( ooOOoooooo )
  O0i1II1Iiii1I11 = II1I . read ( )
  if O0i1II1Iiii1I11 == OOOOoOoo0O0O0 : pass
  else :
   IIiIi1iI ( '[B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B] [B][COLOR lime]I[/COLOR][COLOR white]nformation[/COLOR][/B]' , OOOOoOoo0O0O0 )
   IIII = open ( ooOOoooooo , "w" )
   IIII . write ( OOOOoOoo0O0O0 )
   IIII . close ( )
   if 32 - 32: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
def o00oooO0Oo ( name , url , iconimage , fanart ) :
 oO0OOoo0OO = url
 o0O0O00 = o000o ( url )
 if 'XXX>yes</XXX' in o0O0O00 :
  if o0oOoO00o == '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Adult Content' , 'You have opted to show adult content' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Set Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1 = iiIiI . getText ( )
    iIiiiI . setSetting ( 'password' , I1 )
   else : quit ( )
   if 86 - 86: OoOoOO00 - OoOO - OoO0O00 * I1iiiiI1iII
 if 'XXX>yes</XXX' in o0O0O00 :
  if o0oOoO00o <> '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Adult Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Enter Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1 = iiIiI . getText ( )
   if I1 <> o0oOoO00o :
    quit ( )
  else : quit ( )
  if 66 - 66: OoooooooOO + O0
 if 'con>yes</con' in o0O0O00 :
  if i1 == '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Conspiracy Content' , 'You have opted to show Conspiracy content' , '' , 'Due to the Nature of Content ,Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Set Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1IiiIIIi = iiIiI . getText ( )
    iIiiiI . setSetting ( 'Conspiracy Password' , I1IiiIIIi )
   else : quit ( )
   if 41 - 41: OoOO - O0 - O0
 if 'con>yes</con' in o0O0O00 :
  if i1 <> '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Conspiracy Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Enter Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1IiiIIIi = iiIiI . getText ( )
   if I1IiiIIIi <> i1 :
    quit ( )
  else : quit ( )
  if 68 - 68: iI1 % oO
 I11i1I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0O00 )
 if 88 - 88: iIii1I11I1II1 - O0OOooO + iI1
 if 40 - 40: I1IiiI * OoOO + iI1 % I1iiiiI1iII
 if 74 - 74: o00oo - Oo0Ooo + OoooooooOO + oO / OoOoOO00
 for oO0Oo in I11i1I1I :
  try :
   if 23 - 23: O0
   if '<regex>' in oO0Oo :
    o00oO0oOo00 = re . compile ( '(<regex>.+?</regex>)' , re . MULTILINE | re . DOTALL ) . findall ( oO0Oo )
    o00oO0oOo00 = '' . join ( o00oO0oOo00 )
    oO0oOo0 = re . compile ( '(<listrepeat>.+?</listrepeat>)' , re . MULTILINE | re . DOTALL ) . findall ( o00oO0oOo00 )
    o00oO0oOo00 = urllib . quote_plus ( o00oO0oOo00 )
    if 45 - 45: I1iiiiI1iII / I1iiiiI1iII + oO + O0OOooO
    iI111i = hashlib . md5 ( )
    for IIi11i1i1iI1 in o00oO0oOo00 : iI111i . update ( str ( IIi11i1i1iI1 ) )
    iI111i = str ( iI111i . hexdigest ( ) )
    if 23 - 23: i11iIiiIii + o0oOOo0O0Ooo . i1IIi
    oO0Oo = oO0Oo . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '&nbsp;' , '' )
    oO0Oo = re . sub ( '<regex>.+?</regex>' , '' , oO0Oo )
    oO0Oo = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , oO0Oo )
    oO0Oo = re . sub ( '<link></link>' , '' , oO0Oo )
    if 100 - 100: oO . o00oo * OoOO
    name = re . sub ( '<meta>.+?</meta>' , '' , oO0Oo )
    try : name = re . findall ( '<title>(.+?)</title>' , name ) [ 0 ]
    except : name = re . findall ( '<name>(.+?)</name>' , name ) [ 0 ]
    if 14 - 14: iI1 % iIii1I11I1II1
    try : oo = re . findall ( '<date>(.+?)</date>' , oO0Oo ) [ 0 ]
    except : oo = ''
    if re . search ( r'\d+' , oo ) : name += ' [COLOR red] Updated %s[/COLOR]' % oo
    if 26 - 26: OoOooOOOO - iIii1I11I1II1 - I1IiiI / OoO0O00 . OoOoOO00 % iIii1I11I1II1
    try : OO = re . findall ( '<thumbnail>(.+?)</thumbnail>' , oO0Oo ) [ 0 ]
    except : OO = IiII
    if 25 - 25: OoO0O00
    try : oOo0oO = re . findall ( '<fanart>(.+?)</fanart>' , oO0Oo ) [ 0 ]
    except : oOo0oO = iI111iI
    if 51 - 51: Oo0Ooo - o00oo + II111iiii * OoOO . OoOooOOOO + o00oo
    try : OoO0o = re . findall ( '<meta>(.+?)</meta>' , oO0Oo ) [ 0 ]
    except : OoO0o = '0'
    if 78 - 78: o00oo % O0 % OoOO
    try : url = re . findall ( '<link>(.+?)</link>' , oO0Oo ) [ 0 ]
    except : url = '0'
    url = url . replace ( '>search<' , '><preset>search</preset>%s<' % OoO0o )
    url = '<preset>search</preset>%s' % OoO0o if url == 'search' else url
    url = url . replace ( '>searchsd<' , '><preset>searchsd</preset>%s<' % OoO0o )
    url = '<preset>searchsd</preset>%s' % OoO0o if url == 'searchsd' else url
    url = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , url )
    if 46 - 46: OoooooooOO . i11iIiiIii
    if not o00oO0oOo00 == '' :
     hash . append ( { 'regex' : iI111i , 'response' : o00oO0oOo00 } )
     url += '|regex=%s' % o00oO0oOo00
     if 94 - 94: o0oOOo0O0Ooo * OoOO / Oo0Ooo / OoOO
    oO0 ( name , url , 10 , OO , oOo0oO , "" )
    if 75 - 75: O0OOooO + OoOoOO00 + o0oOOo0O0Ooo * OoOooOOOO % o00oo . I1iiiiI1iII
   elif '<sportsmamachans>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sportsmamachans>(.+?)</sportsmamachans>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 12 , iconimage , fanart )
   elif '<sportsmamagames>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sportsmamagames>(.+?)</sportsmamagames>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 44 , iconimage , fanart )
   elif '<porncom>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<porncom>(.+?)</porncom>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 65 , iconimage , fanart )
   elif '<multisearch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<multisearch>(.+?)</multisearch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 91 , iconimage , fanart )
   elif '<mflixcats>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<mflixcats>(.+?)</mflixcats>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 75 , iconimage , fanart )
   elif '<mflixpop>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<mflixpop>(.+?)</mflixpop>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 78 , iconimage , fanart )
    if 55 - 55: iI1 . I1IiiI
   elif '<cam>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cam>(.+?)</cam>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 70 , iconimage , fanart )
   elif '<cmovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cmovies>(.+?)</cmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 62 , iconimage , fanart )
   elif '<vodly>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<vodly>(.+?)</vodly>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 60 , iconimage , fanart )
   elif '<shighlights>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 68 , iconimage , fanart )
   elif '<sockshare>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sockshare>(.+?)</sockshare>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 60 , iconimage , fanart )
   elif '<hdmovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<hdmovies>(.+?)</hdmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 49 , iconimage , fanart )
   elif '<afdah>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<afdah>(.+?)</afdah>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 52 , iconimage , fanart )
   elif '<watch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<watch>(.+?)</watch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 30 , iconimage , fanart )
   elif '<soccerstreams>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<soccerstreams>(.+?)</soccerstreams>' ) . findall ( oO0Oo ) [ 0 ]
   elif '<top40>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<top40>(.+?)</top40>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 46 , iconimage , fanart )
   elif '<pornhd>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<pornhd>(.+?)</pornhd>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 41 , iconimage , fanart , '' )
   elif '<m3u>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 11 , iconimage , fanart )
   elif '<anime>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<anime>(.+?)</anime>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 32 , iconimage , fanart )
   elif '<comics>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<comics>(.+?)</comics>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 38 , iconimage , fanart )
   elif '<cartoons>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 35 , iconimage , fanart )
   elif '<docs>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<docs>(.+?)</docs>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 24 , iconimage , fanart )
   elif '<filmon>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<filmon>(.+?)</filmon>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 26 , iconimage , fanart )
   elif '<music>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<music>(.+?)</music>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 28 , iconimage , fanart )
   elif '<pornscrape>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<pornscrape>(.+?)</pornscrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 16 , iconimage , fanart )
   elif '<tvput>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<tvput>(.+?)</tvput>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 13 , iconimage , fanart )
   elif '<moviescrape>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<moviescrape>(.+?)</moviescrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 15 , iconimage , fanart )
   elif '<moviescrapenorm>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<moviescrapenorm>(.+?)</moviescrapenorm>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 22 , iconimage , fanart )
   elif '<channel>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 6 , iconimage , fanart )
   elif '<image>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , iconimage , 9 , iconimage , fanart )
   elif '<sportsdevil>' in oO0Oo :
    O0oOO0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo ) [ 0 ]
     O0ooo0O0oo0 = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oO0Oo ) [ 0 ]
     oo0oOo = O0ooo0O0oo0
     o000O0o = "/"
     if not oo0oOo . endswith ( o000O0o ) :
      iI1iII1 = oo0oOo + "/"
     else :
      iI1iII1 = oo0oOo
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = o0O0O00 + '%26referer=' + iI1iII1
     Ii1iIiII1ii1 ( name , url , 4 , iconimage , fanart )
    elif len ( O0oOO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     Ii1iIiII1ii1 ( name , oO0OOoo0OO , 8 , iconimage , fanart )
     if 61 - 61: Oo0Ooo % iIii1 . Oo0Ooo
   elif '<folder>' in oO0Oo :
    iiIii = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
    for name , url , iconimage , fanart in iiIii :
     if url in iiIIiIiIi :
      iiiI1I11i1 ( name , url , 1 , iconimage , fanart )
     else :
      iiiI1I11i1 ( name , url , 20 , iconimage , fanart )
      if 100 - 100: oO * O0
   else :
    O0oOO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     iiIii = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     ooo0O = len ( I11i1I1I )
     for name , url , iconimage , fanart in iiIii :
      if 'youtube.com/playlist' in url :
       iiiI1I11i1 ( name , url , 2 , iconimage , fanart )
      else :
       oOoO0o00OO0 ( name , url , 2 , iconimage , fanart )
    elif len ( O0oOO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     oOoO0o00OO0 ( name , oO0OOoo0OO , 3 , iconimage , fanart )
  except : pass
 iIIiII ( )
 if 64 - 64: iI1 % iIii1I11I1II1 * o00oo
def o0 ( name , url , iconimage , fanart ) :
 if 37 - 37: o00oo - oO % Oo0Ooo
 if 77 - 77: Oo0Ooo - i1IIi - OoOooOOOO . OoOoOO00
 oO0OOoo0OO = url
 o0O0O00 = Oo0oOOo ( url )
 if 39 - 39: II111iiii / O0OOooO + oO / OoOoOO00
 if 13 - 13: iIii1 + O0 + I1iiiiI1iII % I1IiiI / o0oOOo0O0Ooo . iIii1
 if 86 - 86: o00oo * o0oOOo0O0Ooo % i1IIi . OoOO . i11iIiiIii
 if 'XXX>yes</XXX' in o0O0O00 :
  if o0oOoO00o == '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Adult Content' , 'You have opted to show adult content' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Set Password' )
    iiIiI . doModal ( )
   else : quit ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1 = iiIiI . getText ( )
    iIiiiI . setSetting ( 'password' , I1 )
   else : quit ( )
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
 if 'XXX>yes</XXX' in o0O0O00 :
  if o0oOoO00o <> '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Adult Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Enter Password' )
    iiIiI . doModal ( )
   else : quit ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1 = iiIiI . getText ( )
   if I1 <> o0oOoO00o :
    quit ( )
  else : quit ( )
  if 100 - 100: OoOO - O0 % o00oo * iI1 + I1IiiI
 if 'con>yes</con' in o0O0O00 :
  if i1 == '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Conspiracy Content' , 'You have opted to show Conspiracy content' , '' , 'Due to the Nature of Content ,Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Set Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1IiiIIIi = iiIiI . getText ( )
    iIiiiI . setSetting ( 'Conspiracy Password' , I1IiiIIIi )
   else : quit ( )
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
 if 'con>yes</con' in o0O0O00 :
  if i1 <> '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Conspiracy Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Enter Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1IiiIIIi = iiIiI . getText ( )
   if I1IiiIIIi <> i1 :
    quit ( )
  else : quit ( )
  if 33 - 33: oO + I1iiiiI1iII * o00oo / iIii1I11I1II1 - I1IiiI
 I11i1I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0O00 )
 for oO0Oo in I11i1I1I :
  try :
   if 54 - 54: oO / iI1 . o00oo % I1iiiiI1iII
   if '<regex>' in oO0Oo :
    o00oO0oOo00 = re . compile ( '(<regex>.+?</regex>)' , re . MULTILINE | re . DOTALL ) . findall ( oO0Oo )
    o00oO0oOo00 = '' . join ( o00oO0oOo00 )
    oO0oOo0 = re . compile ( '(<listrepeat>.+?</listrepeat>)' , re . MULTILINE | re . DOTALL ) . findall ( o00oO0oOo00 )
    o00oO0oOo00 = urllib . quote_plus ( o00oO0oOo00 )
    if 57 - 57: i11iIiiIii . I1ii11iIi11i - OoOO - o00oo + OoOoOO00
    iI111i = hashlib . md5 ( )
    for IIi11i1i1iI1 in o00oO0oOo00 : iI111i . update ( str ( IIi11i1i1iI1 ) )
    iI111i = str ( iI111i . hexdigest ( ) )
    if 63 - 63: OoOoOO00 * I1iiiiI1iII
    oO0Oo = oO0Oo . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '&nbsp;' , '' )
    oO0Oo = re . sub ( '<regex>.+?</regex>' , '' , oO0Oo )
    oO0Oo = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , oO0Oo )
    oO0Oo = re . sub ( '<link></link>' , '' , oO0Oo )
    if 69 - 69: O0 . OoO0O00
    name = re . sub ( '<meta>.+?</meta>' , '' , oO0Oo )
    try : name = re . findall ( '<title>(.+?)</title>' , name ) [ 0 ]
    except : name = re . findall ( '<name>(.+?)</name>' , name ) [ 0 ]
    if 49 - 49: I1IiiI - OoOooOOOO
    try : oo = re . findall ( '<date>(.+?)</date>' , oO0Oo ) [ 0 ]
    except : oo = ''
    if re . search ( r'\d+' , oo ) : name += ' [COLOR red] Updated %s[/COLOR]' % oo
    if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
    try : OO = re . findall ( '<thumbnail>(.+?)</thumbnail>' , oO0Oo ) [ 0 ]
    except : OO = IiII
    if 62 - 62: OoooooooOO * I1IiiI
    try : oOo0oO = re . findall ( '<fanart>(.+?)</fanart>' , oO0Oo ) [ 0 ]
    except : oOo0oO = iI111iI
    if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
    try : OoO0o = re . findall ( '<meta>(.+?)</meta>' , oO0Oo ) [ 0 ]
    except : OoO0o = '0'
    if 50 - 50: oO . o0oOOo0O0Ooo
    try : url = re . findall ( '<link>(.+?)</link>' , oO0Oo ) [ 0 ]
    except : url = '0'
    url = url . replace ( '>search<' , '><preset>search</preset>%s<' % OoO0o )
    url = '<preset>search</preset>%s' % OoO0o if url == 'search' else url
    url = url . replace ( '>searchsd<' , '><preset>searchsd</preset>%s<' % OoO0o )
    url = '<preset>searchsd</preset>%s' % OoO0o if url == 'searchsd' else url
    url = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , url )
    if 97 - 97: O0 + OoOoOO00
    if not o00oO0oOo00 == '' :
     hash . append ( { 'regex' : iI111i , 'response' : o00oO0oOo00 } )
     url += '|regex=%s' % o00oO0oOo00
     if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * OoOooOOOO * OoOO
    oO0 ( name , url , 10 , OO , oOo0oO , "" )
    if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
   elif '<sportsmamachans>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sportsmamachans>(.+?)</sportsmamachans>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 12 , iconimage , fanart )
   elif '<sportsmamagames>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sportsmamagames>(.+?)</sportsmamagames>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 44 , iconimage , fanart )
   elif '<hdmovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<hdmovies>(.+?)</hdmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 49 , iconimage , fanart )
   elif '<multisearch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<multisearch>(.+?)</multisearch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 91 , iconimage , fanart )
   elif '<cmovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cmovies>(.+?)</cmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 62 , iconimage , fanart )
   elif '<mflixcats>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<mflixcats>(.+?)</mflixcats>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 75 , iconimage , fanart )
   elif '<mflixpop>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<mflixpop>(.+?)</mflixpop>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 78 , iconimage , fanart )
    if 77 - 77: iI1 * iIii1I11I1II1
   elif '<shighlights>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 68 , iconimage , fanart )
   elif '<porncom>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<porncom>(.+?)</porncom>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 65 , iconimage , fanart )
   elif '<cam>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cam>(.+?)</cam>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 70 , iconimage , fanart )
   elif '<sockshare>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sockshare>(.+?)</sockshare>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 60 , iconimage , fanart )
   elif '<pornhd>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<pornhd>(.+?)</pornhd>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 41 , iconimage , fanart , '' )
   elif '<vodly>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<vodly>(.+?)</vodly>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 60 , iconimage , fanart )
   elif '<soccerstreams>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<soccerstreams>(.+?)</soccerstreams>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 55 , iconimage , fanart )
   elif '<watch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<watch>(.+?)</watch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 30 , iconimage , fanart )
   elif '<afdah>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<afdah>(.+?)</afdah>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 52 , iconimage , fanart )
   elif '<top40>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<top40>(.+?)</top40>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 46 , iconimage , fanart )
   elif '<m3u>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 11 , iconimage , fanart )
   elif '<docs>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<docs>(.+?)</docs>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 24 , iconimage , fanart )
   elif '<anime>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<anime>(.+?)</anime>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 32 , iconimage , fanart )
   elif '<comics>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<comics>(.+?)</comics>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 38 , iconimage , fanart )
   elif '<cartoons>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 35 , iconimage , fanart )
   elif '<music>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<music>(.+?)</music>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 28 , iconimage , fanart )
   elif '<filmon>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<filmon>(.+?)</filmon>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 26 , iconimage , fanart )
   elif '<tvput>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<tvput>(.+?)</tvput>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 13 , iconimage , fanart )
   elif '<pornscrape>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<pornscrape>(.+?)</pornscrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 16 , iconimage , fanart )
   elif '<moviescrape>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<moviescrape>(.+?)</moviescrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 15 , iconimage , fanart )
   elif '<moviescrapenorm>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<moviescrapenorm>(.+?)</moviescrapenorm>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 22 , iconimage , fanart )
   elif '<moviessearch>yes</moviessearch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , 'url' , 23 , iconimage , fanart )
   elif '<channel>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 6 , iconimage , fanart )
   elif '<image>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , iconimage , 9 , iconimage , fanart )
   elif '<sportsdevil>' in oO0Oo :
    O0oOO0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo ) [ 0 ]
     O0ooo0O0oo0 = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oO0Oo ) [ 0 ]
     oo0oOo = O0ooo0O0oo0
     o000O0o = "/"
     if not oo0oOo . endswith ( o000O0o ) :
      iI1iII1 = oo0oOo + "/"
     else :
      iI1iII1 = oo0oOo
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = o0O0O00 + '%26referer=' + iI1iII1
     Ii1iIiII1ii1 ( name , url , 4 , iconimage , fanart )
    elif len ( O0oOO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     Ii1iIiII1ii1 ( name , oO0OOoo0OO , 8 , iconimage , fanart )
     if 98 - 98: I1IiiI % OoOO * OoooooooOO
   elif '<folder>' in oO0Oo :
    iiIii = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
    for name , url , iconimage , fanart in iiIii :
     if url in iiIIiIiIi :
      iiiI1I11i1 ( name , url , 1 , iconimage , fanart )
     else :
      iiiI1I11i1 ( name , url , 20 , iconimage , fanart )
   else :
    O0oOO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     iiIii = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     ooo0O = len ( I11i1I1I )
     for name , url , iconimage , fanart in iiIii :
      if 'youtube.com/playlist' in url :
       iiiI1I11i1 ( name , url , 2 , iconimage , fanart )
      else :
       oOoO0o00OO0 ( name , url , 2 , iconimage , fanart )
    elif len ( O0oOO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     oOoO0o00OO0 ( name , oO0OOoo0OO , 3 , iconimage , fanart )
  except : pass
 iIIiII ( )
 if 51 - 51: iIii1I11I1II1 . OoOoOO00 / o00oo + o0oOOo0O0Ooo
def I11iI1i1I11I11 ( name , url , iconimage ) :
 if 69 - 69: OoOoOO00
 II1I , OO0OoOO0o0o = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 II1I += urllib . unquote_plus ( OO0OoOO0o0o )
 url = regex . resolve ( II1I )
 if 95 - 95: i11iIiiIii
 iI1111iiii ( name , url , iconimage )
 if 67 - 67: OoooooooOO / I1IiiI * OoOO + OoOooOOOO
def OooOo0ooo ( name , url , iconimage ) :
 if 71 - 71: oO + OoOO
 iI1111ii1I = urllib2 . Request ( url )
 iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' )
 OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
 o0O0O00 = OO00OooO0OO . read ( )
 OO00OooO0OO . close ( )
 OO00OooO0OO = o0O0O00
 OO00OooO0OO = OO00OooO0OO . replace ( '#AAASTREAM:' , '#A:' )
 OO00OooO0OO = OO00OooO0OO . replace ( '#EXTINF:' , '#A:' )
 iiI11iI = re . compile ( '^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall ( OO00OooO0OO )
 oOOoO0o0oO = [ ]
 for o0Oo0oO0oOO00 , oo00OO0000oO , url in iiI11iI :
  I1II1 = { "params" : o0Oo0oO0oOO00 , "display_name" : oo00OO0000oO , "url" : url }
  oOOoO0o0oO . append ( I1II1 )
 list = [ ]
 for oooO in oOOoO0o0oO :
  I1II1 = { "display_name" : oooO [ "display_name" ] , "url" : oooO [ "url" ] }
  iiI11iI = re . compile ( ' (.+?)="(.+?)"' , re . I + re . M + re . U + re . S ) . findall ( oooO [ "params" ] )
  for i1I1i111Ii , ooo in iiI11iI :
   I1II1 [ i1I1i111Ii . strip ( ) . lower ( ) . replace ( '-' , '_' ) ] = ooo . strip ( )
  list . append ( I1II1 )
 for oooO in list :
  name = i1i1iI1iiiI ( oooO [ "display_name" ] )
  url = i1i1iI1iiiI ( oooO [ "url" ] )
  url = url . replace ( '\\r' , '' ) . replace ( '\\t' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( ' ' , '' ) . replace ( 'm3u8' , 'm3u8' )
  oOoO0o00OO0 ( name , url , 2 , IiII , Iii1ii1II11i , '' )
  if 51 - 51: I1IiiI % oO . o00oo / iIii1I11I1II1 / OoOooOOOO . o00oo
def IIIii11 ( name , url , iconimage ) :
 iiIiIIIiiI = [ ]
 iiI1IIIi = [ ]
 II11IiIi11 = [ ]
 o0O0O00 = Oo0oOOo ( url )
 II = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( II ) [ 0 ]
 O0oOO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( II )
 IIi11i1i1iI1 = 1
 for OOO0O00O0OOOO in O0oOO0 :
  I1iiii1I = OOO0O00O0OOOO
  if '(' in OOO0O00O0OOOO :
   OOO0O00O0OOOO = OOO0O00O0OOOO . split ( '(' ) [ 0 ]
   OOo0 = str ( I1iiii1I . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iiIiIIIiiI . append ( OOO0O00O0OOOO )
   iiI1IIIi . append ( OOo0 )
  else :
   iiIiIIIiiI . append ( OOO0O00O0OOOO )
   iiI1IIIi . append ( 'Link ' + str ( IIi11i1i1iI1 ) )
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
 name = '[COLOR lime]' + name + '[/COLOR]'
 I11 = xbmcgui . Dialog ( )
 oO00ooooO0o = I11 . select ( name , iiI1IIIi )
 if oO00ooooO0o < 0 :
  quit ( )
 else :
  url = iiIiIIIiiI [ oO00ooooO0o ]
  if 75 - 75: i1IIi / O0 * o0oOOo0O0Ooo
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : IiI1iiiIii = liveresolver . resolve ( url )
  else : IiI1iiiIii = url
  I1III1111iIi = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  I1III1111iIi . setPath ( IiI1iiiIii )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1III1111iIi )
  if 38 - 38: I1iiiiI1iII + OoOooOOOO / oO % O0OOooO - I1ii11iIi11i
def iI11 ( name , url , iconimage ) :
 if 10 - 10: II111iiii / o00oo % OoooooooOO * OoOooOOOO % I1ii11iIi11i
 if 48 - 48: O0OOooO / oO . iIii1I11I1II1 * OoOoOO00 * o00oo / i1IIi
 OOOOoOOo0O0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 iiIiIIIiiI = [ ]
 iiI1IIIi = [ ]
 II11IiIi11 = [ ]
 oOooo0 = [ ]
 o0O0O00 = o000o ( url )
 II = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 O0oOO0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( II )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( II ) [ 0 ]
 IIi11i1i1iI1 = 1
 if 58 - 58: I1IiiI . I1iiiiI1iII + OoOoOO00
 for OOO0O00O0OOOO in O0oOO0 :
  I1iiii1I = OOO0O00O0OOOO
  if '(' in OOO0O00O0OOOO :
   OOO0O00O0OOOO = OOO0O00O0OOOO . split ( '(' ) [ 0 ]
   OOo0 = str ( I1iiii1I . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iiIiIIIiiI . append ( OOO0O00O0OOOO )
   iiI1IIIi . append ( OOo0 )
   oOooo0 . append ( 'Stream ' + str ( IIi11i1i1iI1 ) )
  else :
   iiIiIIIiiI . append ( OOO0O00O0OOOO )
   iiI1IIIi . append ( 'Link ' + str ( IIi11i1i1iI1 ) )
   if 66 - 66: I1iiiiI1iII / o00oo * OoooooooOO + OoooooooOO % OoOooOOOO
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 I11 = xbmcgui . Dialog ( )
 oO00ooooO0o = I11 . select ( name , iiI1IIIi )
 if oO00ooooO0o < 0 :
  quit ( )
 else :
  oo0oOo = iiI1IIIi [ oO00ooooO0o ]
  o000O0o = "/"
  if not oo0oOo . endswith ( o000O0o ) :
   iI1iII1 = oo0oOo + "/"
  else :
   iI1iII1 = oo0oOo
  url = OOOOoOOo0O0 + iiIiIIIiiI [ oO00ooooO0o ] + "%26referer=" + iI1iII1
  print url
  if 49 - 49: o00oo - i11iIiiIii . oO * OoOO % I1iiiiI1iII + i1IIi
  xbmc . Player ( ) . play ( url )
  if 71 - 71: o0oOOo0O0Ooo
  if 38 - 38: o00oo % OoOoOO00 + I1ii11iIi11i . i11iIiiIii
  if 53 - 53: i11iIiiIii * I1iiiiI1iII
  if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
  if 38 - 38: O0OOooO - iI1 / I1iiiiI1iII
  if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoOO + I1ii11iIi11i
  if 86 - 86: o0oOOo0O0Ooo
def i1Iii11Ii1i1 ( ) :
 if 59 - 59: Oo0Ooo % OoooooooOO . I1iiiiI1iII / iIii1 + I1IiiI
 OO00Oo = 'http://www.animetoon.org/dubbed-anime'
 if 76 - 76: O0OOooO
 o0O0O00 = o000o ( OO00Oo )
 OoO0O00O0oo0O = re . compile ( '<td>(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 if 36 - 36: iI1 + O0 - OoOO - O0 % OoOooOOOO . o00oo
 for O0oOO0 in OoO0O00O0oo0O :
  try :
   OO00Oo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   oooiiI = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + oooiiI + "[/COLOR]" , OO00Oo , 33 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
def ii111I ( url ) :
 if 17 - 17: I1IiiI . O0 + OoO0O00
 o0O0O00 = o000o ( url )
 O0O0OoOO0 = re . compile ( 'img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 2 ]
 I11i1I1I = re . compile ( '<div id="videos">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OoO0O00O0oo0O = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 43 - 43: II111iiii . o00oo / I1ii11iIi11i
 for i1iI1 in OoO0O00O0oo0O :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( i1iI1 ) [ 0 ]
   url = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( i1iI1 ) [ 0 ]
   oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 34 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 33 - 33: iIii1 % iIii1I11I1II1 * I1IiiI
def o00o0 ( name , url , iconimage ) :
 if 50 - 50: Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 o0O0O00 = o000o ( url )
 O0O0Oo00 = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 oOoO00o ( name , O0O0Oo00 , iconimage )
 if 100 - 100: o0oOOo0O0Ooo + iI1 * o0oOOo0O0Ooo
 if 80 - 80: o0oOOo0O0Ooo * O0 - OoOO
 if 66 - 66: i11iIiiIii - iI1 * Oo0Ooo
 if 76 - 76: i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - OoO0O00 - OoOO + I1ii11iIi11i
 if 51 - 51: iIii1I11I1II1 . O0OOooO + iIii1I11I1II1
 if 95 - 95: I1IiiI
 if 46 - 46: OoOoOO00 + OoO0O00
def o0o0O ( ) :
 if 68 - 68: O0OOooO
 OO00Oo = 'http://www.toonget.net/cartoon'
 if 25 - 25: I1ii11iIi11i . O0OOooO
 o0O0O00 = o000o ( OO00Oo )
 OoO0O00O0oo0O = re . compile ( '<td>(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 if 24 - 24: o00oo / i11iIiiIii + o00oo
 for O0oOO0 in OoO0O00O0oo0O :
  try :
   OO00Oo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   oooiiI = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + oooiiI + "[/COLOR]" , OO00Oo , 36 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 20 - 20: OoOooOOOO + OoOO / O0 % iIii1I11I1II1
  if 88 - 88: OoOoOO00 / II111iiii
  if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - I1iiiiI1iII + o00oo
def OOooo ( url ) :
 if 31 - 31: o0oOOo0O0Ooo % OoO0O00
 o0O0O00 = o000o ( url )
 O0O0OoOO0 = re . compile ( 'img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 2 ]
 I11i1I1I = re . compile ( '<div id="videos">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OoO0O00O0oo0O = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 14 - 14: o00oo / o00oo % O0OOooO
 for i1iI1 in OoO0O00O0oo0O :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( i1iI1 ) [ 0 ]
   url = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( i1iI1 ) [ 0 ]
   oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 37 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 56 - 56: I1IiiI . O0 + Oo0Ooo
 try :
  i1II1I1Iii1 = re . compile ( '<li><a href=\"([^"]*)\">Next' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , i1II1I1Iii1 , 36 , IiII , iI111iI , '' )
 except : pass
 if 30 - 30: OoooooooOO - OoOoOO00
def Ooo00O0o ( name , url , iconimage ) :
 if 72 - 72: iIii1I11I1II1 * OoOO % O0OOooO / OoO0O00
 o0O0O00 = o000o ( url )
 O0O0Oo00 = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 oOoO00o ( name , O0O0Oo00 , iconimage )
 if 35 - 35: O0OOooO + i1IIi % I1ii11iIi11i % OoOooOOOO + o00oo
 if 17 - 17: i1IIi
 if 21 - 21: Oo0Ooo
 if 29 - 29: OoOooOOOO / II111iiii / O0OOooO * iI1
 if 10 - 10: oO % iIii1 * iIii1 . OoOooOOOO / OoOO % iI1
 if 49 - 49: OoO0O00 / o00oo + O0 * o0oOOo0O0Ooo
 if 28 - 28: O0OOooO + i11iIiiIii / OoOooOOOO % OoOoOO00 % Oo0Ooo - O0
def ooo0OOO ( ) :
 if 49 - 49: i11iIiiIii % OoOO . OoOoOO00
 OO00Oo = 'http://www.readcomics.tv/comic-list'
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<div class="serie-box" id="others">(.+?)<h2>Read Comics Online</h2>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OoO0O00O0oo0O = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - II111iiii * iI1
 for O0oOO0 in OoO0O00O0oo0O :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   OO00Oo = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 39 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 26 - 26: OoooooooOO * I1IiiI + iI1
def IiIii1i111 ( url ) :
 if 43 - 43: O0
 o0O0O00 = o000o ( url )
 Ii1Ii1iIiII1Ii = re . compile ( '<div class="manga-image"><img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 oO0o0OOOO = re . compile ( '<h2>(.+?)</h2>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ] . replace ( 'Read ' , '' ) . replace ( 'Online' , '' )
 Iii1II1iiiiI = re . compile ( '<a class="stread" href="(.+?)">' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 o0O = Iii1II1iiiiI . split ( '/' ) [ - 1 ]
 O00oO = o0O . replace ( 'chapter-' , ' ' )
 O00oO = int ( O00oO )
 iiiI1I11i1 ( "[COLOR lime]Issue " + str ( O00oO ) + "[/COLOR]" , Iii1II1iiiiI , 40 , Ii1Ii1iIiII1Ii , iI111iI , '' )
 I11i1I1I = re . compile ( '<ul class="ml-list">(.+?)</ul>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OoO0O00O0oo0O = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 for O0oOO0 in sorted ( OoO0O00O0oo0O ) :
  O00oO = O00oO + 1
  url = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]Issue " + str ( O00oO ) + "[/COLOR]" , url , 40 , Ii1Ii1iIiII1Ii , iI111iI , '' )
  if 61 - 61: iI1 % iI1 * o0oOOo0O0Ooo / o0oOOo0O0Ooo
def o0oOO ( url ) :
 if 53 - 53: oO * iIii1 . Oo0Ooo - OoOO % OoOO * i11iIiiIii
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' )
 ii = re . compile ( '<div class="label">of (.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 if 79 - 79: o0oOOo0O0Ooo - OoOooOOOO + o0oOOo0O0Ooo . o00oo
 ii = int ( ii )
 ii1III11 = re . compile ( '<img id="main_img" src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 o0O = ii1III11 . replace ( '.jpg' , '' ) . replace ( 'http://' , '' )
 O00oO = o0O . split ( '/' )
 I1iiIIIi11 = len ( O00oO )
 Ii1I11ii1i = I1iiIIIi11 - 1
 O0iIiIIIIIii = 1
 OOo0ii11I1 = ""
 for oO0oo in O00oO :
  if O0iIiIIIIIii <= Ii1I11ii1i :
   OOo0ii11I1 = OOo0ii11I1 + "/" + oO0oo
   O0iIiIIIIIii = O0iIiIIIIIii + 1
   if 38 - 38: OoooooooOO * O0OOooO % O0 * OoOoOO00
 IIiiI = 1
 OOo0ii11I1 = "http://" + OOo0ii11I1 + "/"
 if 31 - 31: I1ii11iIi11i + OoOO + oO / OoOO
 while IIiiI <= ii :
  url = OOo0ii11I1 + str ( IIiiI ) + ".jpg"
  oO0 ( "[COLOR lime]Page " + str ( IIiiI ) + "[/COLOR]" , url , 9 , url , url , '' )
  IIiiI = IIiiI + 1
  if 25 - 25: OoO0O00
  if 24 - 24: iIii1 * i11iIiiIii * iI1
  if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / O0OOooO . O0 % oO
  if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . I1iiiiI1iII
  if 8 - 8: O0OOooO + II111iiii / I1iiiiI1iII / OoOooOOOO
  if 74 - 74: O0 / i1IIi
  if 78 - 78: OoooooooOO . OoO0O00 + O0OOooO - i1IIi
def ii1 ( url ) :
 if 83 - 83: I1iiiiI1iII . O0 / Oo0Ooo / iI1 - II111iiii
 if 100 - 100: OoO0O00
 o0O0O00 = o000o ( url ) . replace ( '&amp;' , 'and' )
 if 46 - 46: OoOoOO00 / iIii1I11I1II1 % I1iiiiI1iII . iIii1I11I1II1 * I1iiiiI1iII
 if 38 - 38: I1ii11iIi11i - I1iiiiI1iII / O0 . oO
 I11i1I1I = re . compile ( '<li.+?href="(.+?)".+?>(.+?)</a.+?li>' ) . findall ( o0O0O00 )
 for oO0OOoo0OO , i1iiIiI1Ii1i in I11i1I1I :
  if oO0OOoo0OO . find ( 'categ' ) != - 1 :
   i1iIi = url + oO0OOoo0OO
   iiiI1I11i1 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , i1iIi , 25 , IiII , iI111iI , '' )
   if 30 - 30: O0 - iIii1I11I1II1 / OoooooooOO
def O0000OOO0 ( url ) :
 if 51 - 51: I1IiiI / iIii1 / OoOO
 I111iIi1 = o000o ( url ) . replace ( '&#8217;' , "'" )
 oo00O00oO000o = re . compile ( '<div class="post-thumbnail".+?<a href="(.+?)".+?src="(.+?)".+?alt="(.+?)"' , re . DOTALL ) . findall ( I111iIi1 )
 for url , OOo00OoO , oO0o0OOOO in oo00O00oO000o :
  iIi1 = o000o ( url )
  i11iiI1111 = re . compile ( '<div class=\'video\'><iframe width=".+?" height=".+?" src="(.+?)"' ) . findall ( iIi1 )
  for oOoooo000Oo00 in i11iiI1111 :
   try :
    OOoo = oOoooo000Oo00 . split ( "/embed/" ) [ 1 ]
    o00O00oO00 = "plugin://plugin.video.youtube/play/?video_id=" + OOoo
    oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , o00O00oO00 , 7 , OOo00OoO , iI111iI , '' )
   except : pass
   if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * iIii1
 try :
  i1II1I1Iii1 = re . compile ( '<link rel="next" href="(.+?)" />' , re . DOTALL ) . findall ( I111iIi1 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , i1II1I1Iii1 , 25 , IiII , iI111iI , '' )
 except : pass
 if 9 - 9: iIii1 - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
 if 39 - 39: iIii1 * Oo0Ooo + iIii1I11I1II1 - iIii1 + iI1
 if 69 - 69: O0
 if 85 - 85: O0OOooO / O0
 if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
 if 62 - 62: oO . iIii1 . OoooooooOO
 if 11 - 11: iI1 / OoOooOOOO
def oooO0 ( ) :
 if 16 - 16: II111iiii + o00oo - OoooooooOO
 OO00Oo = 'http://www.filmon.com/tv/bbc-news'
 if 3 - 3: O0 / I1iiiiI1iII
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '{"group_id"(.+?)channels_count' ) . findall ( o0O0O00 )
 for iIiIi1I in I11i1I1I :
  oO0o0OOOO = re . compile ( 'title":"(.+?)"' ) . findall ( iIiIi1I ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , iIiIi1I , 27 , IiII , iI111iI , '' )
  if 45 - 45: i1IIi + II111iiii
def IiII1II11I ( url ) :
 if 54 - 54: iIii1 + O0 + OoOooOOOO * oO - iI1 % o00oo
 I11i1I1I = re . compile ( '{"id"(.+?)}' ) . findall ( url )
 for I111 in I11i1I1I :
  oO0o0OOOO = re . compile ( ':.+?big_logo":".+?".+?title":"(.+?)".+?alias":".+?"' ) . findall ( I111 ) [ 0 ]
  O0O0OoOO0 = re . compile ( ':.+?big_logo":"(.+?)".+?title":".+?".+?alias":".+?"' ) . findall ( I111 ) [ 0 ]
  url = re . compile ( ':.+?big_logo":".+?".+?title":".+?".+?alias":"(.+?)"' ) . findall ( I111 ) [ 0 ]
  O0O0OoOO0 = O0O0OoOO0 . replace ( '\\' , '' )
  oO0OOoo0OO = 'https://www.filmon.com/tv/' + url
  oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , oO0OOoo0OO , 2 , O0O0OoOO0 , iI111iI , '' )
  if 13 - 13: OoO0O00 * o00oo * I1iiiiI1iII
  if 26 - 26: O0 * Oo0Ooo + II111iiii / iIii1 + o00oo % o0oOOo0O0Ooo
  if 42 - 42: I1ii11iIi11i . oO % oO
  if 57 - 57: II111iiii
  if 54 - 54: Oo0Ooo + o00oo + i11iIiiIii
  if 28 - 28: o00oo
  if 70 - 70: iIii1
def i11i1iiI1i ( url ) :
 if 87 - 87: O0OOooO
 IIIii = 1
 url = 'http://hdvidmusic.com'
 O00OooOo00o = o000o ( url )
 IiI11i1IIiiI = re . compile ( '<a href="([^"]*)">>></a></div>' , re . DOTALL ) . findall ( O00OooOo00o ) [ 0 ]
 IiI11i1IIiiI = IiI11i1IIiiI . replace ( '?page=' , '' )
 oOOo000oOoO0 = int ( IiI11i1IIiiI )
 if 86 - 86: II111iiii % i11iIiiIii + OoOO % i11iIiiIii
 url = 'http://hdvidmusic.com/?page=' + str ( IIIii )
 while IIIii <= oOOo000oOoO0 :
  if 92 - 92: i11iIiiIii - I1iiiiI1iII / O0OOooO / o00oo
  url = 'http://hdvidmusic.com/?page=' + str ( IIIii )
  if 43 - 43: II111iiii + iI1 + I1iiiiI1iII
  o0O0O00 = o000o ( url )
  I11i1I1I = re . compile ( '<div class="cell_container">(.+?)<!--div class="video_rating">' , re . DOTALL ) . findall ( o0O0O00 )
  if 40 - 40: o0oOOo0O0Ooo
  for O0oOO0 in I11i1I1I :
   i1iiIiI1Ii1i = re . compile ( '<a title="(.+?)" href=".+?">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   o0O0O00 = re . compile ( '<a title=".+?" href="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   OOo00OoO = re . compile ( 'src="(.+?)"/>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   OOOooo = re . compile ( '<div class="video_quality">(.+?)</div>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   I111iIi1 = 'http://hdvidmusic.com' + o0O0O00
   Oo00oo0000OO = 'http://hdvidmusic.com' + OOo00OoO
   oO0 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , I111iIi1 , 29 , Oo00oo0000OO , iI111iI , '' )
  IIIii = IIIii + 1
  if 69 - 69: O0OOooO - OoO0O00 / i11iIiiIii + I1ii11iIi11i % OoooooooOO
def o000O000 ( url ) :
 if 19 - 19: iIii1I11I1II1
 I111iIi1 = o000o ( url ) . replace ( '?' , '' )
 Ii1IiI1i1ii = re . compile ( '<iframe id\=.+?www(.+?)aut' ) . findall ( I111iIi1 ) [ 0 ]
 id = Ii1IiI1i1ii . split ( '/' ) [ - 1 ]
 url = 'plugin://plugin.video.youtube/play/?video_id=' + id
 xbmc . Player ( ) . play ( url )
 if 30 - 30: iIii1 + oO - iIii1 . iIii1 - II111iiii + O0
def oOO0 ( ) :
 OO00Oo = 'http://www.bigtop40.com/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '&amp;' , 'and' ) . replace ( '&#39;' , "'" ) . replace ( '&quot;' , '"' )
 I11i1I1I = re . compile ( '<li data-chart-position=".+?"(.+?)</em>' , re . DOTALL ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  try :
   i1IIiIii1i = re . compile ( '<a name="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ] . replace ( 'number' , 'Number' ) . replace ( '_' , ' ' )
   Ii1Ii1iIiII1Ii = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   ooOOO0OooOo = re . compile ( 'alt="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   OO00Oo = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   if not 'http' in OO00Oo :
    oO0OOoo0OO = 'http://www.bigtop40.com' + OO00Oo
    oO0 ( "[COLOR red]" + i1IIiIii1i + "[/COLOR]" + ' -- ' + "[COLOR lime]" + ooOOO0OooOo + "[/COLOR]" , oO0OOoo0OO , 47 , Ii1Ii1iIiII1Ii , iI111iI , '' )
  except : pass
  if 33 - 33: iI1 / i1IIi - I1IiiI % Oo0Ooo . I1ii11iIi11i
def Ii1II ( url ) :
 I111iIi1 = o000o ( url ) . replace ( '?' , '' )
 Ii1IiI1i1ii = re . compile ( '<iframe width=".+?" height="348" src="(.+?)"' ) . findall ( I111iIi1 ) [ 0 ]
 id = Ii1IiI1i1ii . split ( '/' ) [ - 1 ]
 url = 'plugin://plugin.video.youtube/play/?video_id=' + id
 xbmc . Player ( ) . play ( url )
 if 89 - 89: oO + OoooooooOO + oO * i1IIi + iIii1I11I1II1 % OoOooOOOO
 if 59 - 59: iI1 + i11iIiiIii
 if 88 - 88: i11iIiiIii - O0OOooO
 if 67 - 67: iI1 . Oo0Ooo + OoOoOO00 - OoooooooOO
 if 70 - 70: iI1 / II111iiii - iIii1I11I1II1 - I1iiiiI1iII
 if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - OoOooOOOO
 if 30 - 30: OoOoOO00
def Ii111 ( ) :
 OO00Oo = 'http://www.hdmovieswatch.org/'
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<li class="cat-item(.+?)</span>' , re . DOTALL ) . findall ( o0O0O00 )
 if 67 - 67: O0
 for oO0Oo in I11i1I1I :
  OO00Oo = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  oO0o0OOOO = re . compile ( 'title.+?">(.+?)</a>' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  IiII = 'https://www.dropbox.com/s/2b0j135ip39g89p/Movies.png?dl=1'
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 50 , IiII , iI111iI , '' )
  if 52 - 52: II111iiii . O0OOooO / OoOoOO00 / OoooooooOO . i11iIiiIii
def I1i1i ( url ) :
 if 86 - 86: Oo0Ooo / o00oo + O0 * I1iiiiI1iII
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<div class="item">(.+?)<span class="player">' , re . DOTALL ) . findall ( o0O0O00 )
 if 19 - 19: II111iiii * iIii1 + OoOO
 for oO0Oo in I11i1I1I :
  try :
   url = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = iii11 ( oO0o0OOOO )
   IiII = re . compile ( '<img src="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = oO0o0OOOO . split ( "Full" ) [ 0 ]
   oO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 51 , IiII , iI111iI , '' )
  except : pass
  if 65 - 65: iI1 . oO . OoO0O00 . I1iiiiI1iII - iI1
 try :
  i1II1I1Iii1 = re . compile ( '<div class="nav-previous alignleft"><a href="(.+?)" ></a>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , i1II1I1Iii1 , 50 , IiII , iI111iI , '' )
 except : pass
 if 19 - 19: i11iIiiIii + I1iiiiI1iII % O0OOooO
def IIi ( url ) :
 if 27 - 27: iI1 % OoOO
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 try :
  import urlresolver
  if urlresolver . HostedMediaFile ( I11i1I1I ) . valid_url ( ) :
   I11i1I1I = urlresolver . HostedMediaFile ( I11i1I1I ) . resolve ( )
   I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = IiII , thumbnailImage = IiII )
   I1III1111iIi . setPath ( I11i1I1I )
   xbmc . Player ( ) . play ( I11i1I1I , I1III1111iIi , False )
  else :
   I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
 except :
  I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
  if 58 - 58: iI1 * o0oOOo0O0Ooo + O0 % iI1
def iI1I1iIi11 ( ) :
 iiiI1I11i1 ( "[COLOR red] Search [/COLOR]" , 'null' , 90 , IiII , iI111iI , '' )
 OO00Oo = "http://www.afdah.bz/"
 o0O0O00 = o000o ( OO00Oo )
 OoO0O00O0oo0O = re . compile ( '<li class="cat-item.+?<a href="(.+?)" >(.+?)</a>' , re . DOTALL ) . findall ( o0O0O00 )
 for OO00Oo , oO0o0OOOO in sorted ( OoO0O00O0oo0O ) :
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 53 , IiII , iI111iI , '' )
  if 87 - 87: OoOoOO00
def Ii ( url ) :
 if 65 - 65: OoOoOO00 / OoO0O00 % iIii1
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<div class="movie-preview-content">(.+?)Views</small>' , re . DOTALL ) . findall ( o0O0O00 )
 if 45 - 45: OoOoOO00
 for oO0Oo in sorted ( I11i1I1I , reverse = True ) :
  if not "<i class" in oO0Oo :
   oO0OOoo0OO = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = oO0o0OOOO . replace ( "Afdah" , "" )
   oO0o0OOOO = iii11 ( oO0o0OOOO )
   Ii1Ii1iIiII1Ii = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  try :
   OOOooo = re . compile ( 'title=.+?Quality">(.+?)<' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  except : OOOooo = "Unknown"
  oO0 ( "[COLOR lime]" + oO0o0OOOO + 'Quality = ' "[/COLOR]" "[COLOR yellow]" + OOOooo + "[/COLOR]" , oO0OOoo0OO , 54 , Ii1Ii1iIiII1Ii , iI111iI , '' )
  if 66 - 66: OoO0O00
 try :
  i1II1I1Iii1 = re . compile ( '<link rel="next" href="(.+?)" />' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , i1II1I1Iii1 , 53 , IiII , iI111iI , '' )
 except : pass
 if 56 - 56: O0
def OOo00 ( url ) :
 if 37 - 37: i1IIi
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 try :
  import urlresolver
  if urlresolver . HostedMediaFile ( I11i1I1I ) . valid_url ( ) :
   I11i1I1I = urlresolver . HostedMediaFile ( I11i1I1I ) . resolve ( )
   I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = IiII , thumbnailImage = IiII )
   I1III1111iIi . setPath ( I11i1I1I )
   xbmc . Player ( ) . play ( I11i1I1I , I1III1111iIi , False )
  else :
   I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
 except :
  I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
  if 46 - 46: OoOoOO00 - OoOooOOOO - OoOO . i1IIi
def IiI1iii11iIi1 ( ) :
 if 40 - 40: OoOooOOOO % OoO0O00 . oO
 OOo0ii11I1 = ''
 OOO0oOOo00O = xbmc . Keyboard ( OOo0ii11I1 , 'Enter Search Term' )
 OOO0oOOo00O . doModal ( )
 if OOO0oOOo00O . isConfirmed ( ) :
  OOo0ii11I1 = OOO0oOOo00O . getText ( )
  if len ( OOo0ii11I1 ) > 1 :
   OO0o = OOo0ii11I1 . lower ( )
   OO0o = OO0o . replace ( " " , "+" )
  else : quit ( )
  if 39 - 39: o0oOOo0O0Ooo * O0OOooO + OoOO * II111iiii
 OO00Oo = "http://www.afdah.bz/?s=" + OO0o
 if 97 - 97: iIii1I11I1II1 + OoOooOOOO + II111iiii % iIii1 % oO % o00oo
 Ii ( OO00Oo )
 if 21 - 21: I1IiiI / O0OOooO % O0OOooO - o0oOOo0O0Ooo
 if 70 - 70: Oo0Ooo . OoOoOO00
 if 58 - 58: OoOooOOOO + II111iiii * I1iiiiI1iII * i11iIiiIii - iIii1I11I1II1
def oooo00o0o0o ( ) :
 if 87 - 87: OoOooOOOO * i1IIi - OoOO % iI1 / oO
 OOo0ii11I1 = ''
 OOO0oOOo00O = xbmc . Keyboard ( OOo0ii11I1 , 'Search For A Movie' )
 OOO0oOOo00O . doModal ( )
 if OOO0oOOo00O . isConfirmed ( ) :
  IiIiiI11111I1 = OOO0oOOo00O . getText ( )
  OO0o = IiIiiI11111I1
  OOo0ii11I1 = IiIiiI11111I1 . replace ( ' ' , '+' )
  if not len ( OOo0ii11I1 ) > 1 :
   I11 . ok ( "STREAM ARMY" , "No search term was entered." )
   quit ( )
   if 55 - 55: O0OOooO % OoooooooOO / OoooooooOO % OoooooooOO
  OOo0ii11I1 = OOo0ii11I1 . replace ( ' ' , '+' )
  OO00Oo = "http://housemovie.to/search?q=" + OOo0ii11I1
  o0O0O00 = o000o ( OO00Oo )
  I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
  if 52 - 52: I1ii11iIi11i + I1ii11iIi11i . II111iiii
  for i1iI1 in I11i1I1I :
   try :
    oO0o0OOOO = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( i1iI1 ) [ 0 ]
    OO00Oo = re . compile ( '<a href="(.+?)" class="fig_holder">' ) . findall ( i1iI1 ) [ 0 ]
    O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
    try :
     Iii = re . compile ( '<span class="imdb">(.+?)</span>' ) . findall ( i1iI1 ) [ 0 ]
    except : Iii = "IMDB Rating Unknown"
    if not "http" in OO00Oo :
     OO00Oo = "http://housemovie.to" + OO00Oo
     oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR] - [COLOR yellow][I]" + Iii + "[/I][/COLOR]" , OO00Oo , 21 , O0O0OoOO0 , iI111iI , '' )
   except : pass
   if 6 - 6: iI1 - I1ii11iIi11i + OoOO + i1IIi / O0 / o0oOOo0O0Ooo
def Iiii1I1 ( url ) :
 if 83 - 83: iI1 . oO + o00oo - iI1 * oO / oO
 o0O0O00 = o000o ( url )
 if 39 - 39: oO / Oo0Ooo % OoO0O00 % i11iIiiIii
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
 if 90 - 90: oO - OoooooooOO
 for O0oOO0 in I11i1I1I :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( O0oOO0 ) [ 0 ]
   oO0OOoo0OO = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( O0oOO0 ) [ 0 ]
   if "genres" in oO0OOoo0OO :
    oO0OOoo0OO = "http://housemovie.to" + oO0OOoo0OO
    iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , oO0OOoo0OO , 19 , IiII , iI111iI , '' )
  except : pass
  if 96 - 96: O0 . OoOO % OoO0O00 * iIii1I11I1II1
def O0O00oOooo0OO ( url ) :
 if 23 - 23: o00oo + OoO0O00
 o0O0O00 = o000o ( url )
 if 2 - 2: o00oo - OoOO - OoOooOOOO - oO . iIii1I11I1II1
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
 if 79 - 79: OoOO . OoO0O00
 for O0oOO0 in I11i1I1I :
  try :
   oO0o0OOOO = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
   Iii = re . compile ( 'imdb">(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
   if "(SOON)" in oO0o0OOOO :
    IIiI1I1 = oO0o0OOOO . split ( "(SOON)" ) [ 0 ]
    oO0o0OOOO = IIiI1I1 . title ( ) + '[COLOR red](Coming Soon)[/COLOR]'
   else : oO0o0OOOO = oO0o0OOOO . title ( )
   if 'search?' in url :
    oO0OOoo0OO = re . compile ( '<a href="(.+?)" class="fig_holder">' ) . findall ( O0oOO0 ) [ 0 ]
   else :
    oO0OOoo0OO = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( O0oOO0 ) [ 0 ]
   O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   if "watch" in oO0OOoo0OO :
    oO0OOoo0OO = "http://housemovie.to" + oO0OOoo0OO
    oO0 ( "[COLOR lime]" + oO0o0OOOO + " [/COLOR]-[COLOR yellow][I] " + Iii + "[/I][/COLOR]" , oO0OOoo0OO , 21 , O0O0OoOO0 , iI111iI , '' )
    if 15 - 15: OoOO * Oo0Ooo % I1ii11iIi11i * iIii1I11I1II1 - i11iIiiIii
  except : pass
  if 60 - 60: I1IiiI * oO % OoO0O00 + o00oo
def o0oo ( name , url , iconimage ) :
 if 80 - 80: oO * OoOoOO00 * II111iiii - O0 . OoOoOO00 % I1IiiI
 II1 = [ ]
 iiIIIiIii = [ ]
 I1i11II = [ ]
 II11 = [ ]
 I1iii = [ ]
 if 51 - 51: I1ii11iIi11i
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 41 - 41: I1ii11iIi11i * O0OOooO - OoOO + Oo0Ooo
 I11i1I1I = re . compile ( '<div class="fig_holder">(.+?)</div>' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  name = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
  oO0OOoo0OO = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  iconimage = re . compile ( 'src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  try :
   Iii = re . compile ( 'imdb">(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
  except : Iii = "0.0"
  if "imdb" in Iii . lower ( ) :
   Iii = Iii . replace ( "IMDB: " , "" ) . replace ( " " , "" )
  if not "." in Iii :
   Iii = Iii + ".0"
   if 23 - 23: II111iiii % o0oOOo0O0Ooo + o0oOOo0O0Ooo + I1iiiiI1iII - I1iiiiI1iII
  if "(SOON)" in name :
   IIiI1I1 = name . split ( "(SOON)" ) [ 0 ]
   name = IIiI1I1 . title ( ) + '[COLOR red](Coming Soon)[/COLOR]'
  else : name = name . title ( )
  oO0OOoo0OO = "http://housemovie.to" + oO0OOoo0OO
  if 62 - 62: o0oOOo0O0Ooo
  II1 . append ( name )
  iiIIIiIii . append ( oO0OOoo0OO )
  I1i11II . append ( iconimage )
  II11 . append ( Iii )
  I1iii = list ( zip ( II11 , II1 , iiIIIiIii , I1i11II ) )
  if 45 - 45: iI1 * O0OOooO
 ooOoOo = sorted ( I1iii , reverse = True )
 if 21 - 21: OoOoOO00 + i11iIiiIii + I1IiiI * o0oOOo0O0Ooo % I1iiiiI1iII % II111iiii
 for Iii , name , oO0OOoo0OO , iconimage in ooOoOo :
  if Iii == "0.0" :
   Iii = "IMDB Rating Unknown"
  else : Iii = "IMDB: " + Iii
  oO0 ( "[COLOR lime]" + name + " [/COLOR]-[COLOR yellow][I] " + Iii + "[/I][/COLOR]" , oO0OOoo0OO , 21 , iconimage , iI111iI , '' )
  if 55 - 55: Oo0Ooo - iI1
 try :
  O0OO0O = re . compile ( '<a href="([^"]*)" class="page_next">Next</a>' ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , O0OO0O , 19 , IiII , iI111iI , '' )
 except : pass
 if 49 - 49: iIii1I11I1II1 - O0 . i1IIi - OoooooooOO
def Ii1ooo0ooO ( name , url , iconimage ) :
 if 17 - 17: I1ii11iIi11i . II111iiii . O0OOooO / I1ii11iIi11i
 iiI1IIIi = [ ]
 iiIiIIIiiI = [ ]
 II11IiIi11 = [ ]
 if 57 - 57: OoOooOOOO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 67 - 67: OoO0O00 . O0OOooO
 O0oOO0 = re . compile ( '<div class="md_full_cell">(.+?)</div>' ) . findall ( o0O0O00 )
 if 87 - 87: o00oo % OoOO
 for II in O0oOO0 :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( II ) [ 0 ]
   i1iiIiI1Ii1i = re . compile ( 'rel="nofollow">(.+?)</a>' ) . findall ( II ) [ 0 ]
   url = "http://housemovie.to" + url
   for oo0OOOoOo in oo0o0O00 :
    if oo0OOOoOo . lower ( ) in i1iiIiI1Ii1i . lower ( ) :
     if 21 - 21: OoO0O00 - O0 . o00oo + OoOO . iIii1I11I1II1 - OoOoOO00
     iiI1IIIi . append ( i1iiIiI1Ii1i )
     iiIiIIIiiI . append ( url )
     II11IiIi11 . append ( iconimage )
  except : pass
  if 14 - 14: iIii1 % o00oo % Oo0Ooo - i11iIiiIii
  if 53 - 53: OoOO % Oo0Ooo
 name = '[COLOR lime]' + name + '[/COLOR]'
 oO00ooooO0o = I11 . select ( name , iiI1IIIi )
 if oO00ooooO0o < 0 :
  quit ( )
 else :
  url = iiIiIIIiiI [ oO00ooooO0o ]
  url = str ( url )
  IiII = II11IiIi11 [ oO00ooooO0o ]
  IiII = str ( IiII )
  if 59 - 59: iI1 % iIii1I11I1II1 . i1IIi + II111iiii * iIii1
  o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 41 - 41: OoOO % I1ii11iIi11i
  url = re . compile ( '<a href="([^"]*)" target="_blank" class="button_type_1">' ) . findall ( o0O0O00 ) [ 0 ]
  if 12 - 12: iI1
  try :
   import urlresolver
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
    I1III1111iIi = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
    I1III1111iIi . setPath ( IiI1iiiIii )
    xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
   else : I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
  except :
   I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
   if 69 - 69: OoooooooOO + iI1
   if 26 - 26: Oo0Ooo + iI1 / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
def i11I1I1iiI ( url ) :
 if 34 - 34: OoOooOOOO % O0OOooO . O0 . iIii1I11I1II1
 url = 'http://cmovieshd.com/library/'
 o0O0O00 = o000o ( url )
 if 93 - 93: i1IIi . i11iIiiIii . Oo0Ooo
 I11i1I1I = re . compile ( '<div class="movies-letter">(.+?)<div class="clearfix">' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 O0O00OOo = re . compile ( '<a(.+?)</a>' , re . DOTALL ) . findall ( I11i1I1I )
 for O0oOO0 in O0O00OOo :
  oO0OOoo0OO = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  OoOOo = re . compile ( 'href=".+?">(.+?)' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ] . replace ( '0' , '0-9' )
  iiiI1I11i1 ( "[COLOR lime]" + OoOOo + "[/COLOR]" , oO0OOoo0OO , 63 , IiII , iI111iI , '' )
  if 17 - 17: i1IIi
def i1IIII1iii11I ( url ) :
 if 97 - 97: OoooooooOO - oO
 if 58 - 58: iIii1I11I1II1 + O0
 if 30 - 30: O0OOooO % I1iiiiI1iII * iI1 - I1ii11iIi11i * OoOO % O0OOooO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="movies-list">(.+?)<div class="clearfix">' ) . findall ( o0O0O00 ) [ 0 ]
 oO0oo = re . compile ( '<a href="(.+?)" rel=".+?" class=".+?" title="(.+?)">.+?<img data-original="(.+?)"' ) . findall ( I11i1I1I )
 for O0oOO0 , i1iiIiI1Ii1i , IiII in oO0oo :
  I111iIi1 = O0oOO0 + 'watch/openload-0.html'
  oO0 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , I111iIi1 , 74 , IiII , iI111iI , '' )
  if 46 - 46: i11iIiiIii - O0 . o00oo
def Oo0O ( url ) :
 if 1 - 1: O0 / I1iiiiI1iII % oO . Oo0Ooo + iIii1
 if 27 - 27: oO % OoooooooOO + iIii1 % i1IIi / o00oo / OoooooooOO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( 'var movie =(.+?)data-toggle="tooltip"]' ) . findall ( o0O0O00 ) [ 0 ]
 III1IiIII1 = re . compile ( 'embed_src.+?"(.+?)"' ) . findall ( I11i1I1I ) [ 0 ]
 if 90 - 90: O0OOooO + II111iiii * I1ii11iIi11i / OoOO . o0oOOo0O0Ooo + o0oOOo0O0Ooo
 import urlresolver
 if urlresolver . HostedMediaFile ( III1IiIII1 ) . valid_url ( ) :
  III1IiIII1 = urlresolver . HostedMediaFile ( III1IiIII1 ) . resolve ( )
  I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = IiII , thumbnailImage = IiII )
  I1III1111iIi . setPath ( III1IiIII1 )
  xbmc . Player ( ) . play ( III1IiIII1 , I1III1111iIi , False )
 else : I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
 if 40 - 40: O0OOooO / OoOoOO00 % i11iIiiIii % I1ii11iIi11i / I1IiiI
 if 62 - 62: i1IIi - OoOoOO00
 if 62 - 62: i1IIi + Oo0Ooo % iIii1
 if 28 - 28: I1ii11iIi11i . i1IIi
 if 10 - 10: OoO0O00 / Oo0Ooo
 if 15 - 15: I1iiiiI1iII . OoOoOO00 / I1iiiiI1iII * OoOooOOOO - I1IiiI % I1ii11iIi11i
def oo0OOOOOO0 ( url ) :
 if 26 - 26: iIii1I11I1II1
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '\r' , '' )
 if 87 - 87: I1ii11iIi11i / OoooooooOO - Oo0Ooo % OoOoOO00 % iIii1 % Oo0Ooo
 I11i1I1I = re . compile ( '<td class="mlnh-thumb">(.+?)</a>' , re . DOTALL ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  Ii1I1iiiiii = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  i1iiIiI1Ii1i = re . compile ( 'title="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  IiII = re . compile ( '<img src="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , Ii1I1iiiiii , 53 , IiII , iI111iI , '' )
 try :
  O0OO0O = re . compile ( 'class="next"><a href="([^"]*)"' ) . findall ( o0O0O00 ) [ 0 ]
  I11 . ok ( "22" , str ( O0OO0O ) )
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , O0OO0O , 63 , IiII , iI111iI , '' )
 except : pass
 if 65 - 65: iIii1 + Oo0Ooo
def Ooo0O0 ( ) :
 if 71 - 71: OoooooooOO
 OO00Oo = 'http://movieflixter.to/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<ul class="menu vertical">(.+?)</ul>' ) . findall ( o0O0O00 ) [ 0 ]
 oO0oo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I11i1I1I )
 for OO00Oo , i1iiIiI1Ii1i in oO0oo :
  if not 'http' in OO00Oo :
   oO0OOoo0OO = 'http://movieflixter.to' + OO00Oo
   IiII = 'http://static.movieflixter.to/img/logo.png'
   iiiI1I11i1 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , oO0OOoo0OO , 76 , IiII , Iii1ii1II11i , '' )
   if 11 - 11: iIii1
def o0oooO ( url ) :
 if 89 - 89: II111iiii / o00oo
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="year">(.+?)</a>' ) . findall ( o0O0O00 )
 if 14 - 14: iI1 . I1IiiI * O0OOooO + II111iiii - O0OOooO + iI1
 for O0oOO0 in I11i1I1I :
  Ii1I1iiiiii = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  if not 'http' in Ii1I1iiiiii :
   I111iIi1 = 'http://movieflixter.to' + Ii1I1iiiiii
   i1iiIiI1Ii1i = re . compile ( 'title="(.+?)">' ) . findall ( O0oOO0 ) [ 0 ]
   i1iiIiI1Ii1i = iii11 ( i1iiIiI1Ii1i )
   try :
    IiII = re . compile ( '<img src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
    if not 'http' in IiII :
     IIIIIiII1 = 'http:' + IiII
     iiiI1I11i1 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , I111iIi1 , 77 , IIIIIiII1 , Iii1ii1II11i , '' )
   except : pass
 try :
  O0OO0O = re . compile ( "<li class='pagination-next'><a href='(.+?)'></a>" ) . findall ( o0O0O00 ) [ 0 ]
  if not 'http' in O0OO0O :
   iii11i1 = 'http://movieflixter.to' + O0OO0O
   if not 'search?' in url :
    iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , iii11i1 , 76 , IiII , iI111iI , '' )
 except : pass
 if 95 - 95: OoO0O00 . i1IIi / i11iIiiIii
def iIi1IIiI ( url ) :
 if 24 - 24: I1iiiiI1iII * II111iiii % I1iiiiI1iII % iIii1 + OoooooooOO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 if 29 - 29: II111iiii - OoooooooOO - i11iIiiIii . o0oOOo0O0Ooo
 if 19 - 19: II111iiii
 I11i1I1I = re . compile ( '<td nowrap>(.+?)&nbsp;' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  try :
   OoOOII1i11i1iIi11 = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   if not 'http' in OoOOII1i11i1iIi11 :
    oo0O0oO0O0O = 'http://movieflixter.to' + OoOOII1i11i1iIi11
    i1iiIiI1Ii1i = re . compile ( '<b>(.+?)</b>' ) . findall ( O0oOO0 ) [ 0 ]
    oOoO0o00OO0 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , oo0O0oO0O0O , 666 , IiII , iI111iI , '' )
  except : pass
  if 69 - 69: o00oo / i11iIiiIii
def OOo00iiiii1ii1 ( ) :
 if 48 - 48: O0 + O0 . oO - O0OOooO
 OO00Oo = 'http://movieflixter.to/movies/best-rated-popular'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="year">(.+?)</a>' ) . findall ( o0O0O00 )
 if 63 - 63: o00oo
 for O0oOO0 in I11i1I1I :
  Ii1I1iiiiii = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  if not 'http' in Ii1I1iiiiii :
   I111iIi1 = 'http://movieflixter.to' + Ii1I1iiiiii
   i1iiIiI1Ii1i = re . compile ( 'title="(.+?)">' ) . findall ( O0oOO0 ) [ 0 ]
   i1iiIiI1Ii1i = iii11 ( i1iiIiI1Ii1i )
   try :
    IiII = re . compile ( '<img src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
    if not 'http' in IiII :
     IIIIIiII1 = 'http:' + IiII
     iiiI1I11i1 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , I111iIi1 , 77 , IIIIIiII1 , Iii1ii1II11i , '' )
   except : pass
   if 71 - 71: i1IIi . OoOO * I1iiiiI1iII % OoooooooOO + iI1
   if 36 - 36: iIii1
   if 49 - 49: iI1 / OoooooooOO / I1IiiI
   if 74 - 74: oO % I1ii11iIi11i
   if 7 - 7: II111iiii
   if 27 - 27: o00oo . OoooooooOO + i11iIiiIii
   if 86 - 86: OoOooOOOO / o0oOOo0O0Ooo - o0oOOo0O0Ooo + I1ii11iIi11i + o00oo
   if 33 - 33: o0oOOo0O0Ooo . I1iiiiI1iII . iIii1 . i1IIi
   if 49 - 49: I1ii11iIi11i
   if 84 - 84: OoOooOOOO - Oo0Ooo / O0 - oO
   if 21 - 21: O0 * O0 % I1ii11iIi11i
def o00ooo ( url ) :
 if 31 - 31: O0 * o0oOOo0O0Ooo % o0oOOo0O0Ooo / o00oo / OoOooOOOO / OoO0O00
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<a class="site_tag(.+?)/a>' ) . findall ( o0O0O00 )
 if 11 - 11: OoOoOO00 + iIii1 - OoooooooOO / OoO0O00
 for o0O0O00 in I11i1I1I :
  url = re . compile ( 'href="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
  oO0o0OOOO = re . compile ( '/i>(.+?)<' ) . findall ( o0O0O00 ) [ 0 ]
  oO0OOoo0OO = "http://xoxfuck.com" + url
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , oO0OOoo0OO , 17 , IiII , iI111iI , '' )
  if 34 - 34: O0OOooO
def i1iI1IIi11i1II ( ) :
 if 73 - 73: o0oOOo0O0Ooo - I1IiiI * i1IIi / i11iIiiIii * iI1 % II111iiii
 OO00Oo = 'http://www.pornhd.com/category'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '&amp;' , 'and' )
 I11i1I1I = re . compile ( '<ul class="tag-150-list">(.+?)<div class="footer-zone">' , re . DOTALL ) . findall ( o0O0O00 )
 OoO0O00O0oo0O = re . compile ( '<li class="category">(.+?)</span>' , re . DOTALL ) . findall ( o0O0O00 )
 if 56 - 56: OoooooooOO * Oo0Ooo . Oo0Ooo . I1ii11iIi11i
 for O0oOO0 in OoO0O00O0oo0O :
  Ii1Ii1iIiII1Ii = re . compile ( 'data-original="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  oO0o0OOOO = re . compile ( 'alt="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  OoOOo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  if not 'http' in OoOOo :
   I111iIi1 = 'http://www.pornhd.com' + OoOOo
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , I111iIi1 , 42 , Ii1Ii1iIiII1Ii , iI111iI , '' )
   if 24 - 24: Oo0Ooo . OoOooOOOO * OoOO % I1iiiiI1iII / iI1
def Oo0Ooo0O0 ( url ) :
 if 42 - 42: i1IIi * o00oo - OoOO . I1IiiI + o0oOOo0O0Ooo . iIii1I11I1II1
 o0iIiiIiiIi = url
 i1i1II = 0
 try :
  o0O , url = url . split ( '|' )
  if 40 - 40: o0oOOo0O0Ooo
 except : i1i1II = 1
 iI1i11Iiii = o000o ( url )
 if 78 - 78: iIii1I11I1II1
 I11i1I1I = re . compile ( '<section id="pageContent"(.+?)<div class="pager paging">' , re . DOTALL ) . findall ( iI1i11Iiii )
 OoO0O00O0oo0O = re . compile ( '<a class="thumb"(.+?)<span class="add-to">' , re . DOTALL ) . findall ( iI1i11Iiii )
 if 56 - 56: OoooooooOO - OoOooOOOO - i1IIi
 if 8 - 8: oO / iI1 . I1IiiI + I1ii11iIi11i / i11iIiiIii
 if 31 - 31: O0OOooO - iIii1I11I1II1 + I1iiiiI1iII . Oo0Ooo / iIii1 % iIii1I11I1II1
 if 6 - 6: iIii1 * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + o0oOOo0O0Ooo / i1IIi
 for O0oOO0 in OoO0O00O0oo0O :
  try :
   i1iiIiI1Ii1i = re . compile ( '<img alt="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   if 53 - 53: OoOooOOOO + iIii1I11I1II1
   if 70 - 70: I1ii11iIi11i
   oo0O = re . compile ( '<time>(.+?)</time>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   if 6 - 6: Oo0Ooo . iIii1 / iIii1 - i11iIiiIii
   O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   if 87 - 87: Oo0Ooo / O0 * iIii1 / o0oOOo0O0Ooo
   if not "http" in O0O0OoOO0 :
    O0O0OoOO0 = re . compile ( 'data-original="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
    if 19 - 19: oO + i1IIi . I1IiiI - Oo0Ooo
    if 16 - 16: o00oo + O0OOooO / o0oOOo0O0Ooo
   o0O0O00 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   if not 'http' in o0O0O00 :
    I111iIi1 = 'http://www.pornhd.com' + o0O0O00
    iiiI1I11i1 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" "[COLOR red]" " :: Video Length :: " + oo0O + "[/COLOR]" , I111iIi1 , 43 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 82 - 82: iIii1 * i11iIiiIii % II111iiii - OoooooooOO
  if 90 - 90: Oo0Ooo . o00oo * i1IIi - i1IIi
 if i1i1II == 1 :
  try :
   IiIiiI11i1Ii = ""
   if not "=" in o0iIiiIiiIi :
    o0iIiiIiiIi = o0iIiiIiiIi + "?page=1"
    o0O , O00oO = o0iIiiIiiIi . split ( "=" )
    I1iiIIIi11 = int ( O00oO ) + 1
    IiIiiI11i1Ii = o0O + "=" + str ( I1iiIIIi11 )
    if 100 - 100: oO . I1IiiI * oO - I1IiiI . OoOooOOOO * OoOO
    iiiI1I11i1 ( '[COLOR red]Next Page >>[/COLOR]' , IiIiiI11i1Ii , 42 , IiII , Iii1ii1II11i )
    if 89 - 89: OoO0O00 + iIii1 * oO
  except : pass
  if 28 - 28: OoooooooOO . o00oo % I1ii11iIi11i / i1IIi / iI1
def III1I1I ( url , icon , fanart ) :
 if 14 - 14: OoOO . i11iIiiIii
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( 'sources.+?{(.+?)}' , re . DOTALL ) . findall ( o0O0O00 )
 o0O = str ( I11i1I1I )
 I11i1I1I = o0O . replace ( '\\' , '' )
 i11i111IiI = re . compile ( "720.+?'.+?'(.+?)'," ) . findall ( I11i1I1I ) [ 0 ]
 I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
 if 25 - 25: OoOooOOOO . I1IiiI + o00oo
 xbmc . Player ( ) . play ( i11i111IiI , I1III1111iIi , False )
 if 75 - 75: iIii1 - o0oOOo0O0Ooo % I1iiiiI1iII + i11iIiiIii
 quit ( 0 )
 if 100 - 100: OoOooOOOO + o0oOOo0O0Ooo - i11iIiiIii - II111iiii
def iIIIiIi1I1i ( name , url , iconimage ) :
 if 78 - 78: iIii1I11I1II1 % OoOoOO00 + I1ii11iIi11i / i1IIi % II111iiii + iI1
 OooOOOO0O0 = name . split ( '(' ) [ 1 ]
 OooOOOO0O0 = OooOOOO0O0 . replace ( ')' , '' ) . replace ( "[/COLOR]" , '' )
 OooOOOO0O0 = int ( OooOOOO0O0 )
 i1IIi1i1Ii1 = url
 if 45 - 45: iIii1I11I1II1 . o00oo / OoOoOO00 / iIii1
 ooOOOoOoOOO0 = 0
 ii111i1iI = 1
 IIi11i1i1iI1 = 0
 I1I1iII1i = 6
 if 30 - 30: O0 + I1ii11iIi11i + II111iiii
 Oo0o0000o0o0 . create ( "STREAM ARMY" , "[COLOR lime]Getting video 1 of " + str ( OooOOOO0O0 ) + "![/COLOR]" )
 Oo0o0000o0o0 . update ( 0 )
 while ii111i1iI < 2000 :
  if 14 - 14: o0oOOo0O0Ooo / iI1 - iIii1I11I1II1 - o00oo % O0OOooO
  if IIi11i1i1iI1 == 0 :
   o0O0O00 = o000o ( i1IIi1i1Ii1 )
   if 49 - 49: O0OOooO * o00oo / o0oOOo0O0Ooo / Oo0Ooo * iIii1I11I1II1
   I11i1I1I = re . compile ( '<div class="inner_block video_box">(.+?)</a>' ) . findall ( o0O0O00 )
   for i1iI1 in I11i1I1I :
    oO0OOoo0OO = re . compile ( 'href="(.+?)">' ) . findall ( i1iI1 ) [ 0 ]
    name = re . compile ( '<h2.+?>(.+?)<' ) . findall ( i1iI1 ) [ 0 ]
    iconimage = re . compile ( 'src="(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
    ooOOOoOoOOO0 = ooOOOoOoOOO0 + 1
    OOoO00ooO = 100 * int ( ooOOOoOoOOO0 ) / int ( OooOOOO0O0 )
    Oo0o0000o0o0 . update ( OOoO00ooO , "[COLOR lime]Getting video " + str ( ooOOOoOoOOO0 ) + " of " + str ( OooOOOO0O0 ) + "![/COLOR]" )
    oO0 ( "[COLOR lime]" + name . title ( ) + "[/COLOR]" , oO0OOoo0OO , 18 , iconimage , iI111iI , '' )
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
  else :
   url = i1IIi1i1Ii1 + '?load_more=10&loaded=' + str ( I1I1iII1i )
   o0O0O00 = o000o ( url )
   o0O0O00 = o0O0O00 . replace ( '\\' , '' )
   if 12 - 12: O0OOooO % I1IiiI + o00oo - i1IIi . OoOO / I1IiiI
   if "no_more_videos" in o0O0O00 :
    ii111i1iI = 2001
    if 51 - 51: iI1 . I1IiiI
   I11i1I1I = re . compile ( '<div class="(.+?)</a>' ) . findall ( o0O0O00 )
   for i1iI1 in I11i1I1I :
    if ii111i1iI < 2000 :
     oO0OOoo0OO = re . compile ( 'href="(.+?)">' ) . findall ( i1iI1 ) [ 0 ]
     name = re . compile ( '<h2.+?>(.+?)<' ) . findall ( i1iI1 ) [ 0 ]
     iconimage = re . compile ( 'src="(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
     ooOOOoOoOOO0 = ooOOOoOoOOO0 + 1
     OOoO00ooO = 100 * int ( ooOOOoOoOOO0 ) / int ( OooOOOO0O0 )
     Oo0o0000o0o0 . update ( OOoO00ooO , "[COLOR lime]Getting video " + str ( ooOOOoOoOOO0 ) + " of " + str ( OooOOOO0O0 ) + "![/COLOR]" )
     oO0 ( "[COLOR lime]" + name . title ( ) + "[/COLOR]" , oO0OOoo0OO , 18 , iconimage , iI111iI , '' )
   I1I1iII1i = I1I1iII1i + 10
  ii111i1iI = ii111i1iI + 1
 Oo0o0000o0o0 . close
 if 73 - 73: OoooooooOO . I1IiiI / oO % OoOO
def o0OO0O00o ( ) :
 if 73 - 73: i1IIi - iI1
 OO00Oo = 'https://www.porn.com/categories'
 if 80 - 80: O0OOooO + i11iIiiIii / o00oo * I1ii11iIi11i * I1ii11iIi11i + iIii1
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="wrap grid categories">(.+?)<div class="listFilters listFiltersWide"' ) . findall ( o0O0O00 ) [ 0 ]
 oO0oo = re . compile ( '<a class="thumbs" href="(.+?)" title="(.+?)"><img src="(.+?)"' ) . findall ( I11i1I1I )
 for Ii1I1iiiiii , i1iiIiI1Ii1i , OoOOoIii1 in oO0oo :
  if not 'http' in Ii1I1iiiiii :
   I111iIi1 = 'https://www.porn.com' + Ii1I1iiiiii
   iiiI1I11i1 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , I111iIi1 , 66 , OoOOoIii1 , iI111iI , '' )
   if 78 - 78: i11iIiiIii + o0oOOo0O0Ooo + oO / o0oOOo0O0Ooo % iIii1I11I1II1 % iIii1
def Oo0O0Oo00O ( url ) :
 if 9 - 9: o0oOOo0O0Ooo . I1IiiI - I1ii11iIi11i
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<ul class="listThumbs">(.+?)<div class="pager">' ) . findall ( o0O0O00 ) [ 0 ]
 OoO0O00O0oo0O = re . compile ( '<img(.+?)<span class="added"' ) . findall ( I11i1I1I )
 for O0oOO0 in OoO0O00O0oo0O :
  try :
   IiiiI = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   OoOOoIii1 = re . compile ( 'src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   i1iiIiI1Ii1i = re . compile ( 'class="title">(.+?)<' ) . findall ( O0oOO0 ) [ 0 ]
   if not 'http' in IiiiI :
    iiIIi = 'https://www.porn.com' + IiiiI
    iiiI1I11i1 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , iiIIi , 67 , OoOOoIii1 , iI111iI , '' )
  except : pass
  if 36 - 36: OoOooOOOO . II111iiii
 try :
  O0OO0O = re . compile ( '<link rel="next" href="([^"]*)"' ) . findall ( o0O0O00 ) [ 0 ]
  if not 'http' in O0OO0O :
   iIIiI1iiI = 'https://www.porn.com' + O0OO0O
   iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , iIIiI1iiI , 66 , IiII , iI111iI , '' )
 except : pass
 if 18 - 18: I1iiiiI1iII - o00oo % I1iiiiI1iII / OoOooOOOO
def O0Oo00OO00Ooo ( url ) :
 if 87 - 87: Oo0Ooo * iI1 % iIii1 % OoOoOO00
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="dlRow">(.+?)<div class="bn">' ) . findall ( o0O0O00 ) [ 0 ]
 iIi1Ii = re . compile ( '<a href="(.+?)".+?</i>(.+?)<' ) . findall ( I11i1I1I )
 for IiI1IIIII1I , OOOooo in iIi1Ii :
  if not 'http' in IiI1IIIII1I :
   oO0OOoo0OO = 'https://www.porn.com' + IiI1IIIII1I
   if 'mp4' in oO0OOoo0OO :
    oO0 ( OOOooo , oO0OOoo0OO , 4 , O0O0OoOO0 , iI111iI , '' )
    if 35 - 35: OoOO - OoOO + i1IIi - O0 - oO
def oOO0o0oo0 ( name , url , iconimage ) :
 if 78 - 78: iI1 + I1iiiiI1iII . iIii1
 I111iIi1 = o000o ( url )
 O0oOO0 = re . compile ( '<video class="video_tag_item" poster=".+?" preload="auto" controls="" src="(.+?)">' ) . findall ( I111iIi1 ) [ 0 ]
 i1iiIiI1Ii1i = re . compile ( '<title>(.+?)</title>' ) . findall ( I111iIi1 ) [ 0 ]
 i1iiIiI1Ii1i = i1iiIiI1Ii1i . split ( ' | ' ) [ 0 ]
 i1iiIiI1Ii1i = i1iiIiI1Ii1i . strip ( ' ' )
 I1III1111iIi = xbmcgui . ListItem ( i1iiIiI1Ii1i , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( O0oOO0 , I1III1111iIi , False )
 if 91 - 91: iIii1I11I1II1 . o0oOOo0O0Ooo . I1ii11iIi11i + OoooooooOO
 if 69 - 69: oO - I1IiiI
 if 95 - 95: I1IiiI * i11iIiiIii . O0OOooO
 if 41 - 41: II111iiii
 if 37 - 37: OoOooOOOO . Oo0Ooo % iIii1 * i1IIi
 if 71 - 71: Oo0Ooo / o0oOOo0O0Ooo + iI1
 if 48 - 48: oO + I1iiiiI1iII
def Iiii1II1iI ( ) :
 OO00Oo = 'http://watchseries.cr/letters/A'
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<a href="(.+?)".+?wpb_btn-small">(.+?)</a>' , re . DOTALL ) . findall ( o0O0O00 )
 O0O0OoOO0 = 'http://watchseries.cr/assets/wp-content/themes/Snaptube/images/new-logo.png'
 for o0O0O00 , i1iiIiI1Ii1i in I11i1I1I :
  if 'http' in o0O0O00 :
   iiiI1I11i1 ( i1iiIiI1Ii1i , o0O0O00 , 31 , O0O0OoOO0 , iI111iI , '' )
   if 42 - 42: o00oo % OoooooooOO + o0oOOo0O0Ooo
def ooOO0o ( url ) :
 if 51 - 51: Oo0Ooo - I1ii11iIi11i * OoOooOOOO
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<td><a style="font-size: 15px;" href="(.+?)">(.+?)</a></td>' , re . DOTALL ) . findall ( o0O0O00 )
 for o0O0O00 , oO0o0OOOO in I11i1I1I :
  iiiI1I11i1 ( oO0o0OOOO , o0O0O00 , 57 , O0O0OoOO0 , iI111iI , '' )
  if 12 - 12: iIii1I11I1II1 % O0OOooO % O0OOooO
def o0i1iI1iiI1I ( url ) :
 if 52 - 52: OoO0O00 % OoOO * II111iiii
 o0O0O00 = o000o ( url )
 Ii1Ii1iIiII1Ii = re . compile ( '<img src="(.+?)">' , re . DOTALL ) . findall ( o0O0O00 ) [ 5 ]
 I11i1I1I = re . compile ( '<h2 class="video-module-title">(.+?)<a href="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
 for I1IiIii11I , o0O0O00 in I11i1I1I :
  iiiI1I11i1 ( I1IiIii11I , o0O0O00 , 58 , Ii1Ii1iIiII1Ii , iI111iI , '' )
  if 29 - 29: o0oOOo0O0Ooo
def oo0 ( url ) :
 if 2 - 2: OoooooooOO
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<div class="vid_info">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  url = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  i1iiIiI1Ii1i = re . compile ( '</b>(.+?)</a>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  iiiI1I11i1 ( i1iiIiI1Ii1i , url , 59 , O0O0OoOO0 , iI111iI , '' )
  if 60 - 60: OoO0O00
def oO00Ooo0oO ( url ) :
 if 100 - 100: OoO0O00 / i1IIi - I1IiiI % OoOO - iIii1I11I1II1
 o0O0O00 = o000o ( url )
 if 17 - 17: OoOooOOOO / o0oOOo0O0Ooo % Oo0Ooo
 I11i1I1I = re . compile ( '<td class="view_link">(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  III1IiIII1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  if 'watchseries' in III1IiIII1 :
   I111iIi1 = o000o ( III1IiIII1 )
   OoO0O00O0oo0O = re . compile ( '<h1>(.+?)</a>' , re . DOTALL ) . findall ( I111iIi1 )
   if 71 - 71: iIii1 . oO . OoO0O00
   for O0oOO0 in OoO0O00O0oo0O :
    OoOOII1i11i1iIi11 = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
    if 'daclips.in' in OoOOII1i11i1iIi11 :
     oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OoOOII1i11i1iIi11 , 2 , O0O0OoOO0 , iI111iI , '' )
    elif 'vidzi.tv' in OoOOII1i11i1iIi11 :
     oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OoOOII1i11i1iIi11 , 2 , O0O0OoOO0 , iI111iI , '' )
     if 68 - 68: i11iIiiIii % o00oo * OoO0O00 * iIii1 * II111iiii + O0
def o00OoO0oO00 ( ) :
 if 2 - 2: iIii1I11I1II1
 OO00Oo = 'http://sockshare.net/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div id="mainmenu2">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OoOOo = re . compile ( '<a href="(.+?)"><img src="(.+?)">' , re . DOTALL ) . findall ( I11i1I1I )
 for Ii1I1iiiiii , OoOOoIii1 in OoOOo :
  iiii1 = 0
  if not 'http' in OoOOo :
   oo0oOo = [ 'genres' , 'countries' , 'years' , 'tv-series' , 'new-movies' , 'anime-series' ]
   for OO0o0oO0O000o in oo0oOo :
    if OO0o0oO0O000o in Ii1I1iiiiii :
     iiii1 = 1
   if iiii1 == 0 :
    I111iIi1 = 'http://sockshare.net' + Ii1I1iiiiii
    I1iI11iii = 'http://sockshare.net' + OoOOoIii1
    if not I111iIi1 . endswith ( '/' ) :
     i1iiIiI1Ii1i = I111iIi1 . replace ( 'http://sockshare.net/' , '' ) . replace ( 'search-movies/2016' , 'New Releases' ) . replace ( 'new-movies' , 'Recently Added' ) . replace ( '.html' , '' ) . replace ( '-' , ' ' )
     i1iiIiI1Ii1i = i1iiIiI1Ii1i . title ( )
     iiii1 = 1
     iiiI1I11i1 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , I111iIi1 , 61 , I1iI11iii , iI111iI , '' )
     if 78 - 78: O0 / II111iiii * OoO0O00
def IiIi1iI11 ( url ) :
 if 11 - 11: I1ii11iIi11i
 iiI1Ii11II1I = url
 if 44 - 44: OoOO % i11iIiiIii - I1iiiiI1iII * I1ii11iIi11i + Oo0Ooo * iI1
 oo0oOo = any ( i . isdigit ( ) for i in iiI1Ii11II1I )
 if 41 - 41: O0 * O0OOooO - OoOoOO00 . OoOO
 if 'http://sockshare.net/search-movies/2016.html' in url :
  oOIIIiI1ii1IIi = url . replace ( '.html' , '' )
  IiIiiI11i1Ii = oOIIIiI1ii1IIi + '/page-2.html'
  if 55 - 55: I1iiiiI1iII - OoO0O00
 elif oo0oOo == False :
  url = url . replace ( ".html" , "" )
  url = url + "/page-1.html"
  iiI1Ii11II1I = url
  o0i1I11iI1iiI = int ( filter ( str . isdigit , iiI1Ii11II1I ) )
  O0OO0O = int ( o0i1I11iI1iiI ) + 1
  if len ( str ( o0i1I11iI1iiI ) ) == 1 :
   iiI1Ii11II1I = iiI1Ii11II1I [ : - 6 ]
  elif len ( str ( o0i1I11iI1iiI ) ) == 2 :
   iiI1Ii11II1I = iiI1Ii11II1I [ : - 7 ]
  elif len ( str ( o0i1I11iI1iiI ) ) == 3 :
   iiI1Ii11II1I = iiI1Ii11II1I [ : - 8 ]
  IiIiiI11i1Ii = iiI1Ii11II1I + str ( O0OO0O ) + ".html"
 else :
  o0i1I11iI1iiI = int ( filter ( str . isdigit , iiI1Ii11II1I ) )
  O0OO0O = int ( o0i1I11iI1iiI ) + 1
  if len ( str ( o0i1I11iI1iiI ) ) == 1 :
   iiI1Ii11II1I = iiI1Ii11II1I [ : - 6 ]
  elif len ( str ( o0i1I11iI1iiI ) ) == 2 :
   iiI1Ii11II1I = iiI1Ii11II1I [ : - 7 ]
  elif len ( str ( o0i1I11iI1iiI ) ) == 3 :
   iiI1Ii11II1I = iiI1Ii11II1I [ : - 8 ]
  IiIiiI11i1Ii = iiI1Ii11II1I + str ( O0OO0O ) + ".html"
  if 48 - 48: OoOooOOOO . OoooooooOO . I1IiiI . OoOoOO00 % I1ii11iIi11i / I1iiiiI1iII
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<li class="item">(.+?)/div>' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  i1iiIiI1Ii1i = re . compile ( '<b>(.+?)</b>' ) . findall ( O0oOO0 ) [ 0 ]
  I111iIi1 = re . compile ( 'href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  IiII = re . compile ( '<img src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , I111iIi1 , 64 , IiII , iI111iI , '' )
  if 11 - 11: i1IIi % OoO0O00 % I1iiiiI1iII
  if 99 - 99: O0OOooO / iIii1I11I1II1 - OoOO * I1ii11iIi11i % I1IiiI
  if 13 - 13: OoO0O00
 try :
  if not 'search-movies' in url :
   iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , IiIiiI11i1Ii , 61 , IiII , iI111iI , '' )
 except : pass
 if 70 - 70: oO + O0 . o00oo * OoOO
def iiII111iIII1Ii ( url ) :
 if 19 - 19: o00oo * I1IiiI % i11iIiiIii
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<p class="server_play">(.+?)</p>' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  III1IiIII1 = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  if 'openload' in III1IiIII1 :
   oO0OOoo0OO = o000o ( III1IiIII1 )
  elif 'vidto' in III1IiIII1 :
   oO0OOoo0OO = o000o ( III1IiIII1 )
  try :
   iiI1Ii1I = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( oO0OOoo0OO ) [ 0 ]
   i11Ii1iIiII = base64 . decodestring ( iiI1Ii1I )
   OoOOII1i11i1iIi11 = re . compile ( 'src="(.+?)"' ) . findall ( i11Ii1iIiII ) [ 0 ]
   i1iiIiI1Ii1i = OoOOII1i11i1iIi11 . replace ( 'https://' , '' ) . replace ( 'http://' , '' ) . replace ( '/' , '' ) . split ( '.' ) [ 0 ]
   i1iiIiI1Ii1i = i1iiIiI1Ii1i . title ( )
   if 'http' in OoOOII1i11i1iIi11 :
    oOoO0o00OO0 ( "[COLOR lime]" + i1iiIiI1Ii1i + "[/COLOR]" , OoOOII1i11i1iIi11 , 2 , O0O0OoOO0 , iI111iI , '' )
    if 81 - 81: OoOooOOOO . OoooooooOO * OoOoOO00 % iIii1 . OoOooOOOO
  except : pass
  if 60 - 60: iI1 / I1IiiI
  if 78 - 78: OoOooOOOO . iIii1
def iI1i1II ( url ) :
 if 14 - 14: O0OOooO - iIii1I11I1II1 / O0 % iIii1 . OoOoOO00
 try :
  if not "http" in url :
   if "https://" in url :
    url = url . replace ( "https://" , "http://" )
   o0O0O00 = o000o ( url )
   oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0O0O00 ) [ 0 ] . split ( ' (' ) [ 0 ]
   iI1IIi11i1I1 = re . compile ( '<td width="100%" class="entry"><a href="(.+?)" title="(.+?)">' ) . findall ( o0O0O00 )
   O0O0OoOO0 = re . compile ( '<meta property="og:image" content="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   if 60 - 60: OoOooOOOO / i1IIi % I1ii11iIi11i / I1ii11iIi11i * I1ii11iIi11i . i11iIiiIii
   for url , i1iiIiI1Ii1i in iI1IIi11i1I1 :
    oO0 ( i1iiIiI1Ii1i , url , 14 , O0O0OoOO0 , iI111iI , '' )
  else :
   o0O0O00 = o000o ( url )
   if 99 - 99: OoOoOO00
   I11i1I1I = re . compile ( '<a class="addthis_counter addthis_pill_style"></a>(.+?)<strong>Sponsored Content</strong>' ) . findall ( o0O0O00 ) [ 0 ]
   OOo0ii11I1 = str ( I11i1I1I )
   OoO0O00O0oo0O = re . compile ( '<td width="100%" class="entry">(.+?)</td>' ) . findall ( OOo0ii11I1 )
   oO00OoOo = re . compile ( '<meta property="og:image" content="(.+?)"/>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
   for i1iI1 in OoO0O00O0oo0O :
    oO0o0OOOO = re . compile ( 'title="(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
    url = re . compile ( '<a href="(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
    i1iiIiI1Ii1i = oO0o0OOOO . split ( ' - ' ) [ 1 ]
    if not 'http' in url : url = 'http:' + url
    oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , url , 14 , oO00OoOo , iI111iI , '' )
 except :
  I11 . ok ( "Stream Army" , "Man Down, Man Down we couldn't get a stream!" )
  quit ( )
  if 74 - 74: II111iiii . O0 - I1IiiI + iIii1 % i11iIiiIii % OoOoOO00
  if 78 - 78: OoOO + OoOoOO00 + iIii1 - iIii1 . i11iIiiIii / OoO0O00
  if 27 - 27: OoOO - O0 % OoOooOOOO * oO . iIii1 % iIii1I11I1II1
  if 37 - 37: OoooooooOO + O0 - i1IIi % O0OOooO
  if 24 - 24: OoOoOO00
  if 94 - 94: i1IIi * i1IIi % II111iiii + iI1
  if 28 - 28: I1IiiI
def I11o0000o0Oo ( ) :
 if 90 - 90: iIii1I11I1II1 * II111iiii
 OO00Oo = 'https://soccerstreams.net/getAllEvents/24?draw=1&columns[0][data]=start_date&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=competition_name&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=home_team&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=event_status&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=away_team&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=event_id&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&start=0&length=-1&search[value]=&search[regex]=false'
 if 70 - 70: o0oOOo0O0Ooo * II111iiii - O0OOooO
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '{"start(.+?)}' ) . findall ( o0O0O00 )
 for i1iI1 in I11i1I1I :
  if not 'event_status":""' in str ( i1iI1 ) :
   oOOoo0 = 1
  else : oOOoo0 = 0
  IIIIiI11I = re . compile ( 'date":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  iiiI11iIIi1 = re . compile ( 'competition_name":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  o00OoooooooOo = re . compile ( 'competition_logo":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  iIii1I = re . compile ( 'home_team":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  iii11i1i1IiI1I111iIi = re . compile ( 'home_team_logo":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  IiiIIi1 = re . compile ( 'home_team_slug":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  try :
   iI1iIiiI = re . compile ( 'event_status":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  except : iI1iIiiI = "null"
  Oo0OOo = re . compile ( 'away_team":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  Ii1I11i11I1i = re . compile ( 'away_team_logo":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  oO00 = re . compile ( 'away_team_slug":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  IiI1II11iiI = re . compile ( 'event_id":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  try :
   o0oOOooo00O = re . compile ( 'game_minute":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  except : o0oOOooo00O = "null"
  OO0ooo0 = iii11i1i1IiI1I111iIi . split ( "-" )
  II1II1iI = Ii1I11i11I1i . split ( "-" )
  iIii1I = ""
  IIi11i1i1iI1 = 0
  for o0O in OO0ooo0 :
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
   oo0O = len ( OO0ooo0 )
   if IIi11i1i1iI1 < oo0O :
    iIii1I = iIii1I + " " + o0O
  Oo0OOo = ""
  IIi11i1i1iI1 = 0
  for o0O in II1II1iI :
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
   oo0O = len ( II1II1iI )
   if IIi11i1i1iI1 < oo0O :
    Oo0OOo = Oo0OOo + " " + o0O
    if 58 - 58: O0 . iIii1 / OoooooooOO . OoO0O00 / Oo0Ooo * II111iiii
  IIIIiI11I = IIIIiI11I + "!"
  IIIIiI11I , O0oo0O00 = IIIIiI11I . split ( ' ' )
  O0oo0O00 = O0oo0O00 . replace ( ":00!" , "" )
  o0O , O00oO , I1iiIIIi11 = IIIIiI11I . split ( "-" )
  IIIIiI11I = I1iiIIIi11 + "-" + O00oO + "-" + o0O
  O0oo0O00 = "[COLOR red][B]" + O0oo0O00 + "[/B][/COLOR]"
  IIIIiI11I = "[COLOR red][B]" + IIIIiI11I + "[/B][/COLOR]"
  OO00Oo = 'https://soccerstreams.net/streams/' + IiI1II11iiI + '/' + IiiIIi1 + '_vs_' + oO00
  oO0o0OOOO = '[COLOR lime][B]' + iIii1I . title ( ) + ' vs ' + Oo0OOo . title ( ) + '[/B][/COLOR]'
  OO00Oo = OO00Oo + "|SPLIT|" + oO0o0OOOO
  O0O0OoOO0 = 'https://soccerstreams.net/images/teams/' + iii11i1i1IiI1I111iIi
  if oOOoo0 == 0 :
   oO0 ( O0oo0O00 + ' | ' + oO0o0OOOO + ' - ' + IIIIiI11I + ' | [COLOR yellow]' + iiiI11iIIi1 + '[/COLOR]' , OO00Oo , 56 , O0O0OoOO0 , iI111iI , '' )
  else :
   o0oOOooo00O = o0oOOooo00O . replace ( '&#039;' , "'" )
   oO0 ( "[COLOR red][B]" + o0oOOooo00O + " " + iI1iIiiI + '[/B][/COLOR] | ' + oO0o0OOOO + ' - ' + IIIIiI11I + ' | [COLOR yellow]' + iiiI11iIIi1 + '[/COLOR]' , OO00Oo , 56 , O0O0OoOO0 , iI111iI , '' )
   if 69 - 69: iI1 % O0
   if 59 - 59: o0oOOo0O0Ooo . OoOoOO00 + oO + OoooooooOO . i1IIi
def I1III1iIi ( name , url , iconimage ) :
 if 82 - 82: I1IiiI + I1iiiiI1iII + I1ii11iIi11i * I1IiiI % i11iIiiIii % I1iiiiI1iII
 I11 = xbmcgui . Dialog ( )
 if 23 - 23: i1IIi . iIii1I11I1II1 . iI1 . O0 % OoOO % i11iIiiIii
 url , name = url . split ( "|SPLIT|" )
 Iiiii111 = name
 iiIiIIIiiI = [ ]
 iiI1IIIi = [ ]
 II11IiIi11 = [ ]
 if 93 - 93: OoooooooOO * Oo0Ooo
 IIi11i1i1iI1 = 1
 I1I1iII1i = 0
 I111iIi1 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0oOO0 = re . compile ( '<tr class="(.+?)</tr>' , re . DOTALL ) . findall ( I111iIi1 )
 for I1IiI1iIiIiii in O0oOO0 :
  url = re . compile ( 'data.+?="(.+?)"' ) . findall ( I1IiI1iIiIiii ) [ 0 ]
  iiIiIIIiiI . append ( url )
  iiI1IIIi . append ( "Link " + str ( IIi11i1i1iI1 ) )
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
  if 29 - 29: O0OOooO - i1IIi . OoOooOOOO - I1ii11iIi11i + O0OOooO + OoooooooOO
 if IIi11i1i1iI1 == 1 :
  I11 . ok ( oO0o0o0ooO0oO , "Sorry no links found!" )
  quit ( )
  if 36 - 36: i1IIi / O0OOooO . iIii1I11I1II1
 Iiiii111 = '[COLOR mediumpurple]' + Iiiii111 + '[/COLOR]'
 if 12 - 12: OoOO
 oO00ooooO0o = I11 . select ( Iiiii111 , iiI1IIIi )
 if oO00ooooO0o < 0 :
  quit ( )
 else :
  url = iiIiIIIiiI [ oO00ooooO0o ]
  oo0oOo = iiI1IIIi [ oO00ooooO0o ]
  name = urllib . quote_plus ( iiI1IIIi [ oO00ooooO0o ] )
  import liveresolver
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
   I1III1111iIi = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
   I1III1111iIi . setPath ( IiI1iiiIii )
   xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
  elif liveresolver . isValid ( url ) == True :
   url = liveresolver . resolve ( url )
   I1III1111iIi = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
   I1III1111iIi . setPath ( IiI1iiiIii )
   xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
  else :
   if '.m3u8' in url :
    url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
   elif '.ts' in url :
    url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
   else :
    OOOOoOOo0O0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=' + name + '%26url='
    o000O0o = "/"
    if not oo0oOo . endswith ( o000O0o ) :
     iI1iII1 = oo0oOo + "/"
    else :
     iI1iII1 = oo0oOo
    url = OOOOoOOo0O0 + iiIiIIIiiI [ oO00ooooO0o ] + "%26referer=" + iI1iII1
   I1III1111iIi = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
   I1III1111iIi . setPath ( url )
   xbmc . Player ( ) . play ( url , I1III1111iIi , False )
   if 71 - 71: I1IiiI . II111iiii . I1IiiI - O0OOooO
def I1ii1 ( ) :
 OO00Oo = 'http://mamahd.com/index.html'
 if 48 - 48: O0OOooO / iIii1I11I1II1 + iI1 + iIii1I11I1II1 . OoO0O00
 if 60 - 60: oO
 if 98 - 98: O0OOooO
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<div class="standard row channels">(.+?)<div class="standard row">' ) . findall ( o0O0O00 ) [ 0 ]
 Ii11i1Ii1IIII = re . compile ( '<a href="(.+?)".+?<img src="(.+?)">.+?<span>(.+?)</span>' ) . findall ( I11i1I1I )
 for o0O0O00 , OoOOoIii1 , oO0o0OOOO in Ii11i1Ii1IIII :
  OO00Oo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + o0O0O00 + '%26referer=no'
  oO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 2 , OoOOoIii1 , iI111iI , '' )
  if 41 - 41: OoOO / II111iiii . OoOoOO00
  if 63 - 63: O0
def i1I1iIii11 ( url ) :
 if 80 - 80: OoOoOO00 - II111iiii
 url = 'http://mamahd.com/index.html'
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<div class="schedule">(.+?)<div id="pagination">' ) . findall ( o0O0O00 ) [ 0 ]
 I1iI1IiI = re . compile ( '<a(.+?)</a>' ) . findall ( I11i1I1I )
 for O0oOO0 in I1iI1IiI :
  time = re . compile ( '<span class="day">(.+?)</span.+?span class="hours">(.+?)</span.+?span class="minutes">(.+?)</span.+?span class="seconds">(.+?)</span>' ) . findall ( O0oOO0 )
  for i1i1Ii1I , I1II1III1 , oooo0O0o0OoOO , III1 in time :
   iiiI1I = re . compile ( '<img src="(.+?)">' ) . findall ( O0oOO0 ) [ 0 ]
   oO0OOO0o0O = re . compile ( '<img src=".+?"><span>(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
   OOOOO0 = re . compile ( '<div class="away cell">.+?<span>(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
   Ooo0Oo0o = re . compile ( 'href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + Ooo0Oo0o + '%26referer=no'
   oO0 ( "[COLOR lime]" + i1i1Ii1I + "[/COLOR]" + "[COLOR lightseagreen]" + "-Days" + "[/COLOR]" + "  " + "[COLOR lime]" + I1II1III1 + "[/COLOR]" + "[COLOR lightseagreen]" + "-Hours" + "[/COLOR]" + "  " + "[COLOR lime]" + oooo0O0o0OoOO + "[/COLOR]" + "[COLOR lightseagreen]" + "-Minutes" + "[/COLOR]" + "   " + ":::" + "    " + "[COLOR yellow]" + oO0OOO0o0O + "  " + "Vs" + "  " + OOOOO0 + "[/COLOR]" , url , 2 , iiiI1I , iI111iI , '' )
   if 85 - 85: I1IiiI
def Ii1Ii1I ( ) :
 if 54 - 54: o00oo + OoOoOO00
 OO00Oo = 'http://www.goalsarena.org/en/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( o0O0O00 ) [ 0 ]
 oO0oo = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( I11i1I1I )
 if 77 - 77: OoOooOOOO . iIii1
 for Ii1I1iiiiii , o0O0OO0OOOOOo in oO0oo :
  iiiI1I11i1 ( "[COLOR lime]" + o0O0OO0OOOOOo + "[/COLOR]" , Ii1I1iiiiii , 69 , IiII , iI111iI , '' )
  if 16 - 16: OoO0O00 / I1iiiiI1iII / i1IIi . I1iiiiI1iII + o00oo
def Iiii1I ( url ) :
 if 56 - 56: i11iIiiIii - iIii1I11I1II1 . II111iiii
 if 81 - 81: iIii1 / OoOoOO00 * iIii1 . O0
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 if 61 - 61: OoO0O00 * iI1 + oO . iIii1I11I1II1 % OoOooOOOO . oO
 try :
  I11i1I1I = re . compile ( '<div id="videodetailsarea"(.+?)</div>' ) . findall ( o0O0O00 ) [ 0 ]
  OoO0O00O0oo0O = re . compile ( '<script data-config="(.+?)"' ) . findall ( I11i1I1I ) [ 0 ]
  if not 'http' in OoO0O00O0oo0O :
   O0o0oo0oOO0oO = 'http:' + ( OoO0O00O0oo0O )
   iIiIII1iI1111 = o000o ( O0o0oo0oOO0oO )
   Ii1I1I111iI = re . compile ( '"f4m":"(.+?)"' ) . findall ( iIiIII1iI1111 ) [ 0 ]
   I1i11I = o000o ( Ii1I1I111iI )
   OoOOII1i11i1iIi11 = re . compile ( '<media url="(.+?)"' ) . findall ( I1i11I ) [ 2 ]
   I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
   xbmc . Player ( ) . play ( OoOOII1i11i1iIi11 , I1III1111iIi , False )
   if 91 - 91: II111iiii * I1iiiiI1iII . i1IIi
   if 22 - 22: o00oo * OoOO * i11iIiiIii + I1iiiiI1iII * OoOoOO00 * OoO0O00
 except : pass
 quit ( 0 )
 if 85 - 85: I1iiiiI1iII * iI1 % Oo0Ooo - I1iiiiI1iII - OoOooOOOO
 if 46 - 46: O0
 if 65 - 65: iIii1I11I1II1 % o00oo + O0 / OoooooooOO
 if 52 - 52: OoOO % iI1 * I1IiiI % OoOooOOOO + iI1 / I1iiiiI1iII
 if 80 - 80: OoooooooOO + iIii1
 if 95 - 95: oO / o00oo * oO - OoooooooOO * OoooooooOO % OoO0O00
 if 43 - 43: Oo0Ooo . oO
def I1I1i1i ( ) :
 if 87 - 87: OoOoOO00 / iIii1 . O0OOooO - iI1 / OoO0O00
 OO00Oo = 'http://www.opentopia.com/hiddencam.php'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<select name="country"(.+?)</select>' ) . findall ( o0O0O00 ) [ 0 ] . replace ( '&nbsp;-&nbsp;' , '' ) . replace ( '* ' , '' ) . replace ( 'Anywhere' , 'Random' )
 OoO0O00O0oo0O = re . compile ( '<option value=".+?">(.+?)</option>' ) . findall ( I11i1I1I )
 for O0oOO0 in OoO0O00O0oo0O :
  if not 'http' in O0oOO0 :
   oo0oOo = "<" + O0oOO0 + ">"
   try :
    iiI1I = re . compile ( "<(.+?) \(.+?\)>" ) . findall ( oo0oOo ) [ 0 ]
   except : iiI1I = O0oOO0
   OOo0ii11I1 = iiI1I . replace ( " " , "+" )
   OO00Oo = "http://www.opentopia.com/hiddencam.php?country=" + OOo0ii11I1
   IiII = 'http://www.greenplanetfireandsecurity.co.uk/images/page-tops/cctv.jpg'
   iiiI1I11i1 ( "[COLOR lime]" + O0oOO0 + "[/COLOR]" , OO00Oo , 71 , IiII , iI111iI , '' )
   if 69 - 69: iIii1I11I1II1 . iI1 / iI1
def Oooooo0000 ( url ) :
 if 60 - 60: II111iiii . I1IiiI - Oo0Ooo + I1ii11iIi11i * I1ii11iIi11i
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<h3 class="navigation">(.+?)<div class="page">' ) . findall ( o0O0O00 ) [ 0 ]
 oO0oo = re . compile ( '<li>(.+?)</li>' ) . findall ( I11i1I1I )
 for O0oOO0 in oO0oo :
  Ii1I1iiiiii = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  if 27 - 27: iIii1 * I1IiiI . iIii1I11I1II1 - iIii1I11I1II1
  if not 'http' in Ii1I1iiiiii :
   I111iIi1 = 'http://www.opentopia.com' + Ii1I1iiiiii + '?viewmode=livevideo'
   OoOOoIii1 = re . compile ( '<img src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   oO0o0OOOO = re . compile ( '<div class="viewcamsname">(.+?)</div>' ) . findall ( O0oOO0 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , I111iIi1 , 72 , OoOOoIii1 , iI111iI , '' )
   if 5 - 5: iIii1
 try :
  i1II1I1Iii1 = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , i1II1I1Iii1 , 71 , IiII , iI111iI , '' )
 except : pass
 if 84 - 84: II111iiii * o00oo * II111iiii % iIii1 / I1IiiI
def O0O ( url ) :
 if 80 - 80: iIii1I11I1II1
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I11i1I1I = re . compile ( '<div class="big">(.+?)<div id="camdetailbottom">' ) . findall ( o0O0O00 ) [ 0 ]
  i1I11 = re . compile ( '<img src="(.+?)"' ) . findall ( I11i1I1I ) [ 0 ]
  I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
  xbmc . Player ( ) . play ( i1I11 , I1III1111iIi , False )
  if 5 - 5: OoOoOO00 % I1iiiiI1iII + iIii1
 except : pass
 quit ( 0 )
 if 13 - 13: iIii1
 if 19 - 19: II111iiii - iIii1
 if 59 - 59: o0oOOo0O0Ooo * OoO0O00 - OoOO . iI1
 if 89 - 89: iI1
 if 69 - 69: O0OOooO - OoooooooOO * O0
 if 84 - 84: O0OOooO + i11iIiiIii - iI1 * O0OOooO
 if 33 - 33: O0OOooO % i1IIi - o00oo . O0 / O0
 if 96 - 96: OoooooooOO + iIii1 * O0
 if 86 - 86: OoOO
 if 29 - 29: iIii1I11I1II1 - OoO0O00 + I1IiiI % iIii1I11I1II1 % iI1
 if 84 - 84: iIii1 + I1ii11iIi11i + OoOO + I1iiiiI1iII
 if 62 - 62: i11iIiiIii + OoOoOO00 + i1IIi
 if 69 - 69: OoOoOO00
 if 63 - 63: OoO0O00 / OoOoOO00 * iIii1I11I1II1 . oO
 if 85 - 85: i11iIiiIii / i11iIiiIii . OoO0O00 . O0
 if 67 - 67: II111iiii / o0oOOo0O0Ooo . iI1 . OoooooooOO
def i1I1Ii11i ( ) :
 if 19 - 19: iIii1 - o0oOOo0O0Ooo . iIii1I11I1II1 . OoOoOO00 / iI1
 OOo0ii11I1 = ''
 OOO0oOOo00O = xbmc . Keyboard ( OOo0ii11I1 , 'Enter Search Term' )
 OOO0oOOo00O . doModal ( )
 if OOO0oOOo00O . isConfirmed ( ) :
  OOo0ii11I1 = OOO0oOOo00O . getText ( )
  if len ( OOo0ii11I1 ) > 1 :
   OO0o = OOo0ii11I1 . lower ( )
   if 87 - 87: OoOoOO00 - O0OOooO - iI1 + Oo0Ooo % iIii1I11I1II1 / i11iIiiIii
  else : quit ( )
 i1iIIII1iiIIi = OO0o . replace ( ' ' , '+' )
 OO00Oo = "http://housemovie.to/search?q=" + i1iIIII1iiIIi
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From House Movies[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 O0O00oOooo0OO ( OO00Oo )
 if 17 - 17: OoOooOOOO
 oOoO0ooO0000 = OO0o . replace ( ' ' , '+' )
 OO00Oo = "http://www.afdah.bz/?s=" + oOoO0ooO0000
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From Afdah Movies[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 Ii ( OO00Oo )
 if 60 - 60: OoOoOO00 / I1ii11iIi11i + iI1 - I1iiiiI1iII
 IIii1III = OO0o . replace ( ' ' , '+' )
 OO00Oo = "http://cmovieshd.com/search/?q=" + IIii1III
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From CMovies[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 i1IIII1iii11I ( OO00Oo )
 if 94 - 94: i11iIiiIii % OoooooooOO / I1IiiI
 iII1Iii11111 = OO0o . replace ( ' ' , '+' )
 OO00Oo = "http://sockshare.net/search-movies/" + iII1Iii11111 + '.html'
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From Sockshare[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 IiIi1iI11 ( OO00Oo )
 if 80 - 80: o00oo * OoOooOOOO / iIii1I11I1II1 % o00oo / iIii1I11I1II1
 Iiii1 = OO0o . replace ( ' ' , '+' )
 OO00Oo = "http://movieflixter.to/search?q=" + Iiii1
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From MovieFlix[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 o0oooO ( OO00Oo )
 if 36 - 36: I1iiiiI1iII
 if 90 - 90: O0
 if 44 - 44: i1IIi . I1IiiI / i11iIiiIii + iIii1
 if 27 - 27: iI1
 if 52 - 52: oO % OoOoOO00 + iIii1I11I1II1 * o00oo . OoOO
 if 95 - 95: iIii1I11I1II1 . iIii1 - OoooooooOO * OoO0O00 / o0oOOo0O0Ooo
 if 74 - 74: o00oo
def iII1i1IIiI1I ( name , url , iconimage ) :
 if 67 - 67: OoOO
 iconimage = "null"
 if 43 - 43: OoO0O00 % OoO0O00
 IIi11i1i1iI1 = 0
 iiIiIIIiiI = [ ]
 iiI1IIIi = [ ]
 II11IiIi11 = [ ]
 if 46 - 46: Oo0Ooo % iIii1I11I1II1 . I1iiiiI1iII . O0 * O0OOooO / OoooooooOO
 II1iI1IIi = 1
 Ii11iiI1 = 0
 if "http" in url :
  if 71 - 71: o0oOOo0O0Ooo / iI1 % iI1
  Oo0o0000o0o0 . create ( "Stream Army" , "[COLOR white][B]Status: [/B][/COLOR][COLOR red]NOT CONNECTED[/COLOR]" )
  Oo0o0000o0o0 . update ( 0 )
  if 89 - 89: OoooooooOO + i11iIiiIii / OoOooOOOO + iIii1I11I1II1 % O0OOooO
  while II1iI1IIi < 11 :
   OOoO00ooO = 100 * int ( II1iI1IIi ) / int ( 10 )
   Oo0o0000o0o0 . update ( OOoO00ooO , "" , "[COLOR lime]Connection attempt " + str ( II1iI1IIi ) + " of 10[/COLOR]" )
   o0O0O00 = o000o ( url )
   if 29 - 29: I1ii11iIi11i
   if Ii11iiI1 == 0 :
    II1iI1IIi = II1iI1IIi + 1
    i1iiIiI1Ii1i = re . compile ( 'title="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
    i1iiIiI1Ii1i = i1iiIiI1Ii1i . split ( " - " ) [ 0 ]
    if 53 - 53: i11iIiiIii . I1ii11iIi11i % OoOO / O0OOooO % iIii1I11I1II1
    iIiIii1I1 = re . compile ( '<td class="entry">(.+?)target' ) . findall ( o0O0O00 )
    for II in iIiIii1I1 :
     O0OOOOo0 = 1
     OOooO0Oo00 = len ( II )
     iIIIIIIIiIII = 100 * int ( O0OOOOo0 ) / int ( OOooO0Oo00 )
     Oo0o0000o0o0 . update ( iIIIIIIIiIII , "[COLOR white][B]Status: [/B][/COLOR][COLOR lime]CONNECTED[/COLOR]" , "[COLOR lime]Filtering links " + str ( O0OOOOo0 ) + " of " + str ( OOooO0Oo00 ) + " possible matches[/COLOR]" )
     if 94 - 94: I1iiiiI1iII * iIii1I11I1II1 . OoOooOOOO
     if not "putlocker.bypassed.info" in II :
      IiiI11I1IIiI = re . compile ( '<a rel=".+?" href="(.+?)"' ) . findall ( II ) [ 0 ]
      IIi11i1i1iI1 = IIi11i1i1iI1 + 1
      iiI1IIIi . append ( "Link " + str ( IIi11i1i1iI1 ) )
      iiIiIIIiiI . append ( IiiI11I1IIiI )
      II11IiIi11 . append ( iconimage )
     Ii11iiI1 = 1
     II1iI1IIi = 12
     O0OOOOo0 = O0OOOOo0 + 1
     if 5 - 5: Oo0Ooo
   if Oo0o0000o0o0 . iscanceled ( ) :
    sys . exit ( )
   import time
   time . sleep ( 1 )
   II1iI1IIi = II1iI1IIi + 1
   if 100 - 100: OoOO + iIii1I11I1II1
 else :
  if 59 - 59: iIii1
  I111iIi1 = o000o ( url )
  O0oOO0 = re . compile ( '<td class="entry">(.+?)</tr>' ) . findall ( I111iIi1 )
  if 89 - 89: OoOoOO00 % iIii1I11I1II1
  for II in O0oOO0 :
   url = re . compile ( 'href="(.+?)"' ) . findall ( II ) [ 0 ]
   if not "putlocker.unblocked.ink" in url :
    IIi11i1i1iI1 = IIi11i1i1iI1 + 1
    iiI1IIIi . append ( "Link " + str ( IIi11i1i1iI1 ) )
    iiIiIIIiiI . append ( url )
    II11IiIi11 . append ( iconimage )
    if 35 - 35: I1ii11iIi11i + oO - OoOoOO00 % o00oo % o0oOOo0O0Ooo % OoOoOO00
    if 45 - 45: I1IiiI * iI1 % OoO0O00
    if 24 - 24: O0OOooO - OoOooOOOO * o00oo
 if IIi11i1i1iI1 == 0 :
  I11 . ok ( "Stream Army" , "Man Down, Man Down we couldn't get a stream!" )
  quit ( )
 name = '[COLOR lime]' + name + '[/COLOR]'
 oO00ooooO0o = I11 . select ( name , iiI1IIIi )
 if oO00ooooO0o < 0 :
  quit ( )
 else :
  url = iiIiIIIiiI [ oO00ooooO0o ]
  url = str ( url )
  IiII = II11IiIi11 [ oO00ooooO0o ]
  IiII = str ( IiII )
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
   I1III1111iIi = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
   I1III1111iIi . setPath ( IiI1iiiIii )
   xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
   if 87 - 87: OoOO - I1ii11iIi11i % I1ii11iIi11i . o00oo / I1ii11iIi11i
def II1i ( name , url , iconimage ) :
 o0II1IIi1iII1i = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; I1III1111iIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 o0II1IIi1iII1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = I1III1111iIi )
 xbmc . Player ( ) . play ( url , I1III1111iIi , False )
 if 26 - 26: O0
def iI1111iiii ( name , url , iconimage ) :
 if 17 - 17: II111iiii
 name = name . replace ( '  ' , '' )
 if not 'f4m' in url :
  if '.m3u8' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + IiII
  elif '.ts' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + IiII
 else : url = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
 if 9 - 9: OoooooooOO + o00oo
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
  I1III1111iIi = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
  I1III1111iIi . setPath ( IiI1iiiIii )
  xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
  quit ( )
 else :
  IiI1iiiIii = url
  I1III1111iIi = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
  I1III1111iIi . setPath ( IiI1iiiIii )
  xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
  quit ( )
  if 33 - 33: O0
def oOoO00o ( name , url , iconimage ) :
 if 39 - 39: I1IiiI + Oo0Ooo
 if not 'http' in url : url = 'http://' + url
 if 'youtube.com/playlist' in url :
  o0OO = url . split ( 'list=' ) [ 1 ]
  ooO = iiIIIII1i1iI + o0OO + o0oO0
  iI1111ii1I = urllib2 . Request ( ooO )
  iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  I11i1I1I = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
  try :
   i1II1I1Iii1 = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   ooO = oo00 + i1II1I1Iii1 + o00 + o0OO + Oo0oO0ooo
   iiiI1I11i1 ( 'Next Page >>' , ooO , 2 , i1i1II , Iii1ii1II11i )
  except : pass
  if 41 - 41: i1IIi + II111iiii * O0OOooO
  if 68 - 68: OoOO - I1IiiI
  if 41 - 41: o00oo
  if 21 - 21: O0OOooO + o0oOOo0O0Ooo % oO + i11iIiiIii + I1iiiiI1iII + II111iiii
  for name , oOO0OOOOOo0Oo in I11i1I1I :
   url = 'https://www.youtube.com/watch?v=' + oOO0OOOOOo0Oo
   iconimage = 'https://i.ytimg.com/vi/' + oOO0OOOOOo0Oo + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     oOoO0o00OO0 ( name , url , 2 , iconimage , Iii1ii1II11i )
     if 40 - 40: iIii1I11I1II1
 if 'https://www.googleapis.com/youtube/v3' in url :
  o0OO = re . compile ( 'playlistId=(.+?)&maxResults' ) . findall ( url ) [ 0 ]
  iI1111ii1I = urllib2 . Request ( url )
  iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  I11i1I1I = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
  try :
   i1II1I1Iii1 = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   ooO = oo00 + i1II1I1Iii1 + o00 + o0OO + Oo0oO0ooo
   iiiI1I11i1 ( 'Next Page >>' , ooO , 2 , i1i1II , Iii1ii1II11i )
  except : pass
  if 56 - 56: o00oo + O0OOooO
  if 32 - 32: II111iiii + OoOoOO00 % O0OOooO / OoOoOO00 + I1ii11iIi11i
  if 2 - 2: i11iIiiIii - oO + OoO0O00 % OoOooOOOO * OoOO
  for name , oOO0OOOOOo0Oo in I11i1I1I :
   url = 'https://www.youtube.com/watch?v=' + oOO0OOOOOo0Oo
   iconimage = 'https://i.ytimg.com/vi/' + oOO0OOOOOo0Oo + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     oOoO0o00OO0 ( name , url , 2 , iconimage , Iii1ii1II11i )
     if 54 - 54: O0 - I1iiiiI1iII . iI1 % I1iiiiI1iII + I1iiiiI1iII
     if 36 - 36: iI1 % i11iIiiIii
     if 47 - 47: i1IIi + II111iiii . Oo0Ooo * o00oo . OoOooOOOO / i1IIi
 if "plugin://" in url :
  url = "PlayMedia(" + url + ")"
  xbmc . executebuiltin ( url )
  quit ( )
  if 50 - 50: oO / i1IIi % OoooooooOO
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
 elif liveresolver . isValid ( url ) == True :
  IiI1iiiIii = liveresolver . resolve ( url )
 else : IiI1iiiIii = url
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
 I1III1111iIi . setPath ( IiI1iiiIii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1III1111iIi )
 if 83 - 83: I1ii11iIi11i * I1ii11iIi11i + iI1
def OooooOoO ( url ) :
 if 79 - 79: O0OOooO % iI1
 try :
  oO0o0OOOO , url , O0O0OoOO0 = url . split ( "!SASPLIT!" )
  I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
  xbmc . Player ( ) . play ( url , I1III1111iIi , False )
 except :
  xbmc . Player ( ) . play ( url )
  if 54 - 54: OoOoOO00 - oO
def o000o ( url ) :
 try :
  iI1111ii1I = urllib2 . Request ( url )
  iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 65 - 65: oO . O0OOooO + iI1 / Oo0Ooo + iIii1 % i1IIi
  return o0O0O00
 except : quit ( )
 if 28 - 28: i11iIiiIii + O0 / I1ii11iIi11i
def Oo0oOOo ( url ) :
 if 3 - 3: OoO0O00 * i1IIi . I1IiiI . O0 - OoOoOO00
 if 81 - 81: I1IiiI - iIii1I11I1II1 / I1IiiI / O0
 try :
  iI1111ii1I = urllib2 . Request ( url )
  iI1111ii1I . add_header ( 'User-Agent' , 'obsession' )
  OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
  o0O0O00 = OO00OooO0OO . read ( )
  if 34 - 34: OoOO * OoOO - I1ii11iIi11i - O0 . i11iIiiIii
  IioOo0O = o00O ( o0O0O00 )
  print "--------- decoded --------" , IioOo0O
  OO00OooO0OO . close ( )
  IioOo0O = IioOo0O . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 30 - 30: OoOO . I1ii11iIi11i / iI1
  return IioOo0O
 except : quit ( )
 if 2 - 2: iIii1 % I1IiiI - oO
def OOOo00oo0oO ( url ) :
 iI1111ii1I = urllib2 . Request ( url )
 iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
 o0O0O00 = OO00OooO0OO . read ( )
 OO00OooO0OO . close ( )
 if 79 - 79: OoooooooOO / I1ii11iIi11i . O0
 return o0O0O00
 if 79 - 79: o00oo - II111iiii
def Ii1iiI1 ( ) :
 o0ooOOoO0oO0 = [ ]
 oo00I1IiI1IIiI = sys . argv [ 2 ]
 if len ( oo00I1IiI1IIiI ) >= 2 :
  o0Oo0oO0oOO00 = sys . argv [ 2 ]
  oooo = o0Oo0oO0oOO00 . replace ( '?' , '' )
  if ( o0Oo0oO0oOO00 [ len ( o0Oo0oO0oOO00 ) - 1 ] == '/' ) :
   o0Oo0oO0oOO00 = o0Oo0oO0oOO00 [ 0 : len ( o0Oo0oO0oOO00 ) - 2 ]
  o0o0oo0Ooo = oooo . split ( '&' )
  o0ooOOoO0oO0 = { }
  for IIi11i1i1iI1 in range ( len ( o0o0oo0Ooo ) ) :
   iI1i = { }
   iI1i = o0o0oo0Ooo [ IIi11i1i1iI1 ] . split ( '=' )
   if ( len ( iI1i ) ) == 2 :
    o0ooOOoO0oO0 [ iI1i [ 0 ] ] = iI1i [ 1 ]
 return o0ooOOoO0oO0
 if 3 - 3: iIii1 / OoOooOOOO
def Ii11 ( name , url , mode , iconimage , itemcount , isFolder = False ) :
 I1i1ii = name . partition ( '(' )
 O0000oo00oOOO = ""
 oOIii11111iiI = ""
 if len ( I1i1ii ) > 0 :
  O0000oo00oOOO = I1i1ii [ 0 ]
  oOIii11111iiI = I1i1ii [ 2 ] . partition ( ')' )
 if len ( oOIii11111iiI ) > 0 :
  oOIii11111iiI = oOIii11111iiI [ 0 ]
 o0OOOOoO = metahandlers . MetaData ( )
 OoO0o = o0OOOOoO . get_meta ( 'movie' , name = O0000oo00oOOO , year = oOIii11111iiI )
 OoO0Ooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 o0II1IIi1iII1i = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = OoO0o [ 'cover_url' ] , thumbnailImage = OoO0o [ 'cover_url' ] )
 I1III1111iIi . setInfo ( type = "Video" , infoLabels = OoO0o )
 Ii1I1I = [ ]
 Ii1I1I . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 I1III1111iIi . addContextMenuItems ( Ii1I1I , replaceItems = False )
 if not OoO0o [ 'backdrop_url' ] == '' : I1III1111iIi . setProperty ( 'fanart_image' , OoO0o [ 'backdrop_url' ] )
 else : I1III1111iIi . setProperty ( 'fanart_image' , Iii1ii1II11i )
 o0II1IIi1iII1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO0Ooo , listitem = I1III1111iIi , isFolder = isFolder , totalItems = itemcount )
 return o0II1IIi1iII1i
 if 56 - 56: O0
def iiiI1I11i1 ( name , url , mode , iconimage , fanart , description = '' ) :
 OoO0Ooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0II1IIi1iII1i = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1III1111iIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , 'plot' : description } )
 I1III1111iIi . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' in url : OoO0Ooo = url
 o0II1IIi1iII1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO0Ooo , listitem = I1III1111iIi , isFolder = True )
 return o0II1IIi1iII1i
 if 45 - 45: OoOoOO00 - OoO0O00 - OoOoOO00
def oO0 ( name , url , mode , iconimage , fanart , description = '' ) :
 OoO0Ooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0II1IIi1iII1i = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1III1111iIi . setProperty ( 'fanart_image' , fanart )
 o0II1IIi1iII1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO0Ooo , listitem = I1III1111iIi , isFolder = False )
 return o0II1IIi1iII1i
 if 41 - 41: Oo0Ooo / i1IIi / Oo0Ooo - I1iiiiI1iII . o0oOOo0O0Ooo
def oOoO0o00OO0 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 65 - 65: O0 * i11iIiiIii . OoooooooOO / I1IiiI / I1iiiiI1iII
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 OoO0Ooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0II1IIi1iII1i = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1III1111iIi . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' not in url :
  I1III1111iIi . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : OoO0Ooo = url
 o0II1IIi1iII1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO0Ooo , listitem = I1III1111iIi , isFolder = False )
 return o0II1IIi1iII1i
 if 69 - 69: O0OOooO % O0OOooO
def Ii1iIiII1ii1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 76 - 76: i11iIiiIii * I1iiiiI1iII / OoO0O00 % I1ii11iIi11i + iI1
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 OoO0Ooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0II1IIi1iII1i = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1III1111iIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I1III1111iIi . setProperty ( "Fanart_Image" , fanart )
 if 'plugin://' not in url :
  I1III1111iIi . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : OoO0Ooo = url
 o0II1IIi1iII1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO0Ooo , listitem = I1III1111iIi , isFolder = False )
 return o0II1IIi1iII1i
 if 48 - 48: iIii1I11I1II1 % i1IIi + OoOoOO00 % o0oOOo0O0Ooo
def OO0oo00oOO ( url ) :
 import urlresolver
 if 38 - 38: oO . I1iiiiI1iII . I1IiiI * OoO0O00
 if 'movieflixter.to' in url :
  iI1111ii1I = urllib2 . Request ( url )
  iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36' )
  OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
  url = OO00OooO0OO . geturl ( )
  if 69 - 69: o0oOOo0O0Ooo % i11iIiiIii / OoOO
  if 93 - 93: O0OOooO
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
 elif liveresolver . isValid ( url ) == True :
  IiI1iiiIii = liveresolver . resolve ( url )
 else : IiI1iiiIii = url
 I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O0OoOO0 )
 I1III1111iIi . setPath ( IiI1iiiIii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1III1111iIi )
 if 34 - 34: o00oo - O0OOooO * Oo0Ooo / o0oOOo0O0Ooo
 if 19 - 19: I1ii11iIi11i
def IiI ( url ) :
 if 4 - 4: OoooooooOO + O0OOooO . i1IIi / O0 - O0
 oOooOOo00ooO = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( oOooOOo00ooO )
 sys . exit ( 1 )
 if 71 - 71: oO - o0oOOo0O0Ooo - iI1
def iiI ( text , pattern ) :
 if 81 - 81: iIii1 * I1ii11iIi11i + II111iiii % iIii1
 iI1i11Iiii = ""
 try :
  IiI1ii11I1 = re . findall ( pattern , text , flags = re . DOTALL )
  iI1i11Iiii = IiI1ii11I1 [ 0 ]
 except :
  iI1i11Iiii = ""
  if 19 - 19: oO + iIii1 / o00oo / II111iiii
 return iI1i11Iiii
 if 92 - 92: i1IIi % O0OOooO + O0OOooO - iIii1I11I1II1 . OoOO
def i1i1iI1iiiI ( str ) :
 if 33 - 33: o0oOOo0O0Ooo / O0 + iI1
 try :
  import chardet
  str = str . decode ( chardet . detect ( str ) [ "encoding" ] ) . encode ( "utf-8" )
 except :
  try :
   str = str . encode ( "utf-8" )
  except :
   pass
 return str
 if 75 - 75: iIii1 % i11iIiiIii + iIii1I11I1II1
def IIiIi1iI ( heading , text ) :
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 oOoOo0o00o = xbmcgui . Window ( id )
 iIIi1 = 50
 while ( iIIi1 > 0 ) :
  try :
   xbmc . sleep ( 10 )
   iIIi1 -= 1
   oOoOo0o00o . getControl ( 1 ) . setLabel ( heading )
   oOoOo0o00o . getControl ( 5 ) . setText ( text )
   return
  except :
   pass
   if 68 - 68: Oo0Ooo
def ii111I11Ii ( link ) :
 try :
  I11i1I1I = re . compile ( '<layouttype>(.+?)</layouttype>' ) . findall ( link ) [ 0 ]
  if layout == 'thumbnail' : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
  else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 except : pass
 if 6 - 6: OoOO
def iIIiII ( ) :
 if 77 - 77: i1IIi + OoO0O00 . I1IiiI * iI1 / iIii1 / OoOO
 OooO0 = xbmc . getInfoLabel ( "System.BuildVersion" )
 II11iiii1Ii = float ( OooO0 [ : 4 ] )
 if 84 - 84: OoO0O00 / iIii1I11I1II1
 if II11iiii1Ii >= 1.0 and II11iiii1Ii <= 16.9 :
  IiI1 = 'Jarvis'
 elif II11iiii1Ii >= 17.0 and II11iiii1Ii <= 17.9 :
  IiI1 = 'Krypton'
  if 13 - 13: OoooooooOO + OoO0O00
 if IiI1 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif IiI1 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 32 - 32: O0 + o00oo % Oo0Ooo
o0Oo0oO0oOO00 = Ii1iiI1 ( ) ; OO00Oo = None ; oO0o0OOOO = None ; iI1iI = None ; O0O0 = None ; O0O0OoOO0 = None
try : O0O0 = urllib . unquote_plus ( o0Oo0oO0oOO00 [ "site" ] )
except : pass
try : OO00Oo = urllib . unquote_plus ( o0Oo0oO0oOO00 [ "url" ] )
except : pass
try : oO0o0OOOO = urllib . unquote_plus ( o0Oo0oO0oOO00 [ "name" ] )
except : pass
try : iI1iI = int ( o0Oo0oO0oOO00 [ "mode" ] )
except : pass
try : O0O0OoOO0 = urllib . unquote_plus ( o0Oo0oO0oOO00 [ "iconimage" ] )
except : pass
try : Iii1ii1II11i = urllib . unquote_plus ( o0Oo0oO0oOO00 [ "fanart" ] )
except : pass
if 70 - 70: iI1 * o00oo / I1IiiI * OoOoOO00 * I1IiiI
if iI1iI == None or OO00Oo == None or len ( OO00Oo ) < 1 : II1III ( )
elif iI1iI == 1 : o00oooO0Oo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i )
elif iI1iI == 2 : oOoO00o ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 3 : IIIii11 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 4 : II1i ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 5 : SEARCH ( )
elif iI1iI == 6 : YOUTUBE_CHANNEL ( OO00Oo )
elif iI1iI == 7 : OooooOoO ( OO00Oo )
elif iI1iI == 8 : iI11 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 9 : IiI ( OO00Oo )
elif iI1iI == 10 : I11iI1i1I11I11 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 11 : OooOo0ooo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 12 : I1ii1 ( )
elif iI1iI == 13 : iI1i1II ( OO00Oo )
elif iI1iI == 14 : iII1i1IIiI1I ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 15 : Iiii1I1 ( OO00Oo )
elif iI1iI == 16 : o00ooo ( OO00Oo )
elif iI1iI == 17 : iIIIiIi1I1i ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 18 : oOO0o0oo0 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 19 : o0oo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 20 : o0 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i )
elif iI1iI == 21 : Ii1ooo0ooO ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 22 : O0O00oOooo0OO ( OO00Oo )
elif iI1iI == 23 : oooo00o0o0o ( )
elif iI1iI == 24 : ii1 ( OO00Oo )
elif iI1iI == 25 : O0000OOO0 ( OO00Oo )
elif iI1iI == 26 : oooO0 ( )
elif iI1iI == 27 : IiII1II11I ( OO00Oo )
elif iI1iI == 28 : i11i1iiI1i ( OO00Oo )
elif iI1iI == 29 : o000O000 ( OO00Oo )
elif iI1iI == 30 : Iiii1II1iI ( )
elif iI1iI == 31 : ooOO0o ( OO00Oo )
elif iI1iI == 32 : i1Iii11Ii1i1 ( )
elif iI1iI == 33 : ii111I ( OO00Oo )
elif iI1iI == 34 : o00o0 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 35 : o0o0O ( )
elif iI1iI == 36 : OOooo ( OO00Oo )
elif iI1iI == 37 : Ooo00O0o ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 38 : ooo0OOO ( )
elif iI1iI == 39 : IiIii1i111 ( OO00Oo )
elif iI1iI == 40 : o0oOO ( OO00Oo )
elif iI1iI == 41 : i1iI1IIi11i1II ( )
elif iI1iI == 42 : Oo0Ooo0O0 ( OO00Oo )
elif iI1iI == 43 : III1I1I ( OO00Oo , IiII , Iii1ii1II11i )
elif iI1iI == 44 : i1I1iIii11 ( OO00Oo )
elif iI1iI == 45 : Ii1 ( OO00Oo )
elif iI1iI == 46 : oOO0 ( )
elif iI1iI == 47 : Ii1II ( OO00Oo )
elif iI1iI == 48 : SCRAPE_SPORTSMAMA_PLAY ( OO00Oo )
elif iI1iI == 49 : Ii111 ( )
elif iI1iI == 50 : I1i1i ( OO00Oo )
elif iI1iI == 51 : IIi ( OO00Oo )
elif iI1iI == 52 : iI1I1iIi11 ( )
elif iI1iI == 53 : Ii ( OO00Oo )
elif iI1iI == 54 : OOo00 ( OO00Oo )
elif iI1iI == 55 : I11o0000o0Oo ( )
elif iI1iI == 56 : I1III1iIi ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iI1iI == 57 : o0i1iI1iiI1I ( OO00Oo )
elif iI1iI == 58 : oo0 ( OO00Oo )
elif iI1iI == 59 : oO00Ooo0oO ( OO00Oo )
elif iI1iI == 60 : o00OoO0oO00 ( )
elif iI1iI == 61 : IiIi1iI11 ( OO00Oo )
elif iI1iI == 62 : i11I1I1iiI ( OO00Oo )
elif iI1iI == 63 : oo0OOOOOO0 ( OO00Oo )
elif iI1iI == 64 : iiII111iIII1Ii ( OO00Oo )
elif iI1iI == 65 : o0OO0O00o ( )
elif iI1iI == 66 : Oo0O0Oo00O ( OO00Oo )
elif iI1iI == 67 : O0Oo00OO00Ooo ( OO00Oo )
elif iI1iI == 68 : Ii1Ii1I ( )
elif iI1iI == 69 : Iiii1I ( OO00Oo )
elif iI1iI == 70 : I1I1i1i ( )
elif iI1iI == 71 : Oooooo0000 ( OO00Oo )
elif iI1iI == 72 : O0O ( OO00Oo )
elif iI1iI == 73 : i1IIII1iii11I ( OO00Oo )
elif iI1iI == 74 : Oo0O ( OO00Oo )
elif iI1iI == 75 : Ooo0O0 ( )
elif iI1iI == 76 : o0oooO ( OO00Oo )
elif iI1iI == 77 : iIi1IIiI ( OO00Oo )
elif iI1iI == 78 : OOo00iiiii1ii1 ( )
if 61 - 61: o00oo + I1ii11iIi11i / i1IIi * o00oo
if 90 - 90: OoOO % o00oo
if 6 - 6: OoooooooOO / i11iIiiIii / oO
if 60 - 60: I1IiiI % o00oo / o0oOOo0O0Ooo % o00oo * i11iIiiIii / I1iiiiI1iII
if 34 - 34: oO - iI1
if 25 - 25: o00oo % I1IiiI + i11iIiiIii + O0 * OoooooooOO
if 64 - 64: i1IIi
if 10 - 10: oO % O0 / I1IiiI % OoOooOOOO
if 25 - 25: II111iiii / OoO0O00
if 64 - 64: O0 % O0OOooO
elif iI1iI == 90 : IiI1iii11iIi1 ( )
elif iI1iI == 91 : i1I1Ii11i ( )
if 40 - 40: o0oOOo0O0Ooo + OoOooOOOO
elif iI1iI == 666 : OO0oo00oOO ( OO00Oo )
if 77 - 77: i11iIiiIii % iIii1 + oO % OoooooooOO - OoOooOOOO
if 26 - 26: Oo0Ooo + O0 - iIii1I11I1II1
if 47 - 47: OoooooooOO
if 2 - 2: OoOoOO00 % oO * Oo0Ooo * OoOoOO00
if 65 - 65: i11iIiiIii + Oo0Ooo * OoooooooOO - OoO0O00
if 26 - 26: o0oOOo0O0Ooo % iI1 + iI1 % OoOooOOOO * i11iIiiIii / I1iiiiI1iII
if 64 - 64: o00oo % OoOoOO00 / II111iiii % O0OOooO - I1iiiiI1iII
if 2 - 2: oO - I1ii11iIi11i + o0oOOo0O0Ooo * OoO0O00 / I1iiiiI1iII
if 26 - 26: iI1 * Oo0Ooo
if 31 - 31: OoOooOOOO * o00oo . OoOO
if 35 - 35: OoOooOOOO
if 94 - 94: O0OOooO / i11iIiiIii % O0
if 70 - 70: OoOooOOOO - Oo0Ooo / OoooooooOO % OoooooooOO
if iI1iI == None or OO00Oo == None or len ( OO00Oo ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
