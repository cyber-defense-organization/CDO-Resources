#!/usr/bin/python3
from lxml import etree
from http import server

routes = {
    "/inband" : {
        "output" : True,
        "error" : True
    },
    "/error" : {
        "output" : False,
        "error" : True
    },
    "/outband" : {
        "output" : False,
        "error" : False
    }
}

def parse_xml(xml, is_output, is_error):
    try:
        parser = etree.XMLParser(no_network=False)
        doc = etree.fromstring(xml, parser)
        parsed_xml = etree.tostring(doc)
        if is_output:
            return parsed_xml
    except Exception as e:
        if is_error:
            return str(e).encode("utf-8")
    return b""

class handle(server.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_header("Content-type", "text/xml")
        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len).strip()
        if post_body:
            if self.path in routes.keys():
                self.send_response(200)
                self.end_headers()
                self.wfile.write(parse_xml(post_body, routes[self.path]["output"], routes[self.path]["error"]))
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"""<?xml version="1.0"?>
<result>
   <status>error</status>
   <response>Nothing Sent in Post Body</response>
</result>""")

port = 8081
print("Routes; POST {}".format(" ".join(routes.keys())))
print("Listening on: {}".format(port))
server.HTTPServer(("", port), handle).serve_forever()
