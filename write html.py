import http.server


class RequestHandlerImpl(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        if "?" in self.path:
            ans = []
            t = self.path
            t = t[8:]
            t = t.split("+")
            t = [eval(i) for i in t]
            avg = sum(t) / len(t)
            for i in t:
                an = abs(i - avg)
                ans.append(an)
            answer = sum(ans) / len(ans) / avg * 100

            html = None
            with open("if true.html", 'r', encoding="utf-8") as file:
                html = file.read().format(answer=answer)

        else:
            html = None
            with open("if not true.html", 'r', encoding="utf-8") as file:
                html = file.read()

        self.wfile.write(html.encode("utf-8"))
        print(self.path)

server_address = ("", 11451)
httpd = http.server.HTTPServer(server_address, RequestHandlerImpl)
httpd.serve_forever()
