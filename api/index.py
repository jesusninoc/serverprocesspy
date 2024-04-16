import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Comando que quieres ejecutar
        comando = 'ps'
        
        # Ejecutar el comando y obtener la salida
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)
        salida = proceso.communicate()[0].decode('utf-8')
        
        # Enviar la salida como respuesta
        self.wfile.write(salida.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor corriendo en el puerto {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()


