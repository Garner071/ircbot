import http.server


class RequestHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()

		self.server.bot._send_msg('Received HTTP request!', '*')
		self.wfile.write(b'OK\n')


class HTTPServer(http.server.HTTPServer):
	def set_bot(self, bot):
		self.bot = bot
		bot.http_server = self


def run_http_server(bot, port=8000):
	httpd = HTTPServer(('', port), RequestHandler)
	httpd.set_bot(bot)
	httpd.serve_forever()

if __name__ == '__main__':
	run_http_server('hello world', 8000)
