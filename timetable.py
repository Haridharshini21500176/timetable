from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
<title>MY TIMETABLE</title>
</head>
<body style="background~colour:mediumblue">
<img src="https://www.saveetha.ac.in/images/WEB_LOGO-01.png"width="100%"height="200">
<h1 style ="text-align:center;"FIRST SEMESTER TIMETABLE</h1>
<table border="1" cellspacing="1" bordercolor="brown" bgcolor="navyblue" width="100%">
    
    <tr>
        <th colspan="8" height="40px" style="background-color:pink">TIME TABLE</th>
    </tr>
    <tr bgcolor="cyan">
        <th colspan="4" height="40px">NAME:S.HARIDHARSHINI</th>
        <th colspan="8" height="40px">REFERENCE NO:21500176</th>
    </tr>
    <tr height="40px">
        
        <th style="background-color:white">DAY</th>
        <th style="background-color:white">1</th>
        <th style="background-color:white">2</th>
        <th style="background-color:white">3</th>
        <th style="background-color:white">4</th>
        <th rowspan="6" bgcolor="magenta">LUNCH BREAK</th>
        <th style="background-color:white">5</th>
        <th style="background-color:white">6</th>
    </tr>
    <tr height="40px" style="text-align:center;">
        <td style="background-color:green">MONDAY</td>
        <td colspan="2">Fundamentals of Web Technology</td>
        <td colspan="2">Linear Algebra Laboratory</td>
        <td colspan="2">Mathematics for Artificial Intelligence</td>
    </tr>
    <tr height="40px" style="text-align:center;">
        <td style="background-color:red">TUESDAY</td>
        <td colspan="2">soft skills</td>
        <td colspan="2">Engineering Design and Modeling</td>
        <td colspan="2">Engineering Mechanics and Product Development</td>
    </tr>
    <tr height="40px" style="text-align:center;">
        <td style="background-color:green">WEDNESDAY</td>
        <td colspan="2">Free time</td>
        <td colspan="2">Python Programming</td>
        <td colspan="2">Fundamentals of Web Technology</td>
    </tr>
    <tr height="40px" style="text-align:center;">
        <td style="background-color:red">THURSDAY</td>
        <td colspan="2">Engineering Mechanics and Product Development</td>
        <td colspan="2">Python Programming</td>
        <td colspan="2">Engineering Design and Modeling</td>
    </tr>
    <tr height="40px" style="text-align:center;">
        <td style="background-color:green">FRIDAY</td>
        <td colspan="2">Environmental science</td>
        <td colspan="2">Mathematics for Artificial Intelligence</td>
        <td colspan="2">Web Technology Laboratory</td>
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
server_address = ('',8080)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()