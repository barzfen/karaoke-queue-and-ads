from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from PySide6.QtCore import QSettings

settings = QSettings('FensomSoftware', 'KaraokeQueue')

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL and query parameters
        url = urlparse(self.path)
        query_params = parse_qs(url.query)

        # Check if the 'key' parameter is in the query string
        if 'key' in query_params:
            # Set the value of 'Access/key' in QSettings to the value of the 'key' parameter
            settings.setValue('Access/key', query_params['key'][0])
            settings.sync()

        # Check if the 'queue_time' parameter is in the query string
        if 'queue_time' in query_params:
            # Set the value of 'Timing/queue' in QSettings to the value of the 'queue_time' parameter
            settings.setValue('Timing/queue', int(query_params['queue_time'][0]))
            settings.sync()


        # Check if the 'promo_time' parameter is in the query string
        if 'promo_time' in query_params:
            # Set the value of 'Timing/promo' in QSettings to the value of the 'promo_time' parameter
            settings.setValue('Timing/promo', int(query_params['promo_time'][0]))
            settings.sync()

        # Get the values of the settings
        access_key = settings.value('Access/key')
        queue_time = int(settings.value('Timing/queue'))
        promo_time = int(settings.value('Timing/promo'))

        # Send a response to the client with the values of the settings and a success message
        response = f"Access/key: {access_key}\nTiming/queue: {queue_time}\nTiming/promo: {promo_time}\nSuccess"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

# Create an HTTP server on port 8000
server_address = ('', 8000)
httpd = HTTPServer(server_address, RequestHandler)
print('Server running at http://localhost:8000')

# Start the server and keep it running
httpd.serve_forever()
