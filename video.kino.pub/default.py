#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, xbmc, xbmcaddon
__id__ = 'video.kino.pub'
__addon__ = xbmcaddon.Addon(id=__id__)
__settings__ = xbmcaddon.Addon(id=__id__)
__skinsdir__ = "DefaultSkin"

_ADDON_PATH =   xbmc.translatePath(__addon__.getAddonInfo('path'))
if (sys.platform == 'win32') or (sys.platform == 'win64'):
    _ADDON_PATH = _ADDON_PATH.decode('utf-8')
sys.path.append( os.path.join( _ADDON_PATH, 'resources', 'lib') )
sys.path.append( os.path.join( _ADDON_PATH, 'resources', 'skins') )
sys.path.append( os.path.join( _ADDON_PATH, 'resources', 'skins', 'DefaultSkin') )

try:
    reset_auth = int(__settings__.getSetting('reset_auth'))
except:
    reset_auth = 0

if reset_auth == 1:
	__settings__.setSetting('access_token', '')
	__settings__.setSetting('refresh_token', '')
	__settings__.setSetting('access_token_expire', '')
	__settings__.setSetting('reset_auth', '0')
	__settings__.setSetting('device_info_update', '0')

if (__name__ == '__main__' ):
    import addonworker
    addonworker.init()






