##create new playlist by HTTP Control
#http://127.0.0.1:8888/ajquery/?cmd=CreatePlaylist&param1=New+Playlist&param3=NoResponse


import sys, os
import codecs
#import http
from http import client
#import urllib
import urllib.parse
import urllib.request

def main( argv=None ):
	sysCode = sys.getdefaultencoding()
	print( "defaultencoding=", sysCode )
	if( 1 ):
		##vs2015 debug will raise exception in sys.stdout.detach(), but just run it not
		try:
			sys.stdout = codecs.getwriter("utf_8")(sys.stdout.detach()) ##important
		except:
			print("except error stdout")
		try:
			sys.stdin = codecs.getwriter("utf_8")(sys.stdin.detach()) ##important
		except:
			print("except error stdin")

	out = sys.stdout
	out.flush()

	if argv is None:
		argv = sys.argv
        # etc., replacing sys.argv with argv in the getopt() call.
    #_ if

	noArgv = len(argv)
	if noArgv <= 1:
		print( "No path string input ..!" )
		exit(0)
	#_ if
	print( "noArgv=", noArgv )
	dirIN = argv[1]
	print( "dirIN=", dirIN )
	sys.stdout.flush()

#_ def main

if __name__ == "__main__":
	main()

	##sys.exit(main())
#_ if
