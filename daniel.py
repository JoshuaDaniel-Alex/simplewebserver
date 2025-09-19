from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>sample page</title>
    </head>
       <body>
        Name:Joshua Daniel
        Ref_no:25017654
        <table border="3" cellspacing="5" cellpadding="0">
        <tr>
            <th>S.No.</th>
            <th>device specification</th>
            <th>details</th>
        </tr>
        <tr>
            <td>1</td>
            <td>STORAGE</td>
            <td>1TB</td>
        </tr>
        <tr>
            <td>2</td>
            <td>RAM</td>
            <td>16GB</td>
        </tr>
        <tr>
            <td>3</td>
            <td>MODEL</td>
            <td>ACER </td>
        </tr>
        <tr>
            <td>4</td>
            <td>WINDOWS</td>
            <td>11</td>
        </tr>
        <tr>
            <td>5</td>
            <td>GRAPHICS CARD</td>
           <td>128GB</td>
        </tr>
        </table>
        </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()