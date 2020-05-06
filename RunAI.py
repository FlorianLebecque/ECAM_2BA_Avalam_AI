import cherrypy
import sys
import AI
import ConnectAI as CA

class Server:

    oldBoard = []

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''

        body = cherrypy.request.json
        

        #create a player
        p = AI.player(body)
        #play
        mov = p.play()

        return mov

    @cherrypy.expose
    def ping(self):
        return "pong"

if __name__ == "__main__":

    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8080

        #inscription au serveur
    msg = '{"matricules": ["'+str(port)+'"],"port":'+str(port)+',"name": "Lbcqu Florian : '+str(port)+'"}'
    addr = "192.168.1.205"
    CA.EchoClient(msg).run(addr, 5001)
    print(msg)
    print("connected")

        #demarre le serveur
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})
    cherrypy.quickstart(Server())