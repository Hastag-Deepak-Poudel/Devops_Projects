import http.server
import socketserver
import ssl
PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler
keyfile="openssl/your_keyfile"  # Generate ssl certificate and copy the keyfile and certfile to the openssl directory.
certfile="openssl/your_certfile"

with socketserver.TCPServer(("", PORT), HANDLER) as httpd:

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile, keyfile)

    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print(f"Serving securely on https://localhost:{PORT}/templatemo_564_plot_listing/index.html")
    print('localhost',' ', PORT)
    # Start the server
    httpd.serve_forever()
