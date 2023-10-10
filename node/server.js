var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${formatUptime(os.uptime)}</p>
            <p>Total Memory: ${os.totalmem/1000000} MB</p>
            <p>Free Memory: ${os.freemem/1000000} MB</p>
            <p>Number of CPUs: ${os.cpus().length}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

function formatUptime(uptime) {
    const days = Math.floor(uptime / (3600 * 24));
    uptime %= (3600 * 24);
    const hours = Math.floor(uptime / 3600);
    uptime %= 3600;
    const minutes = Math.floor(uptime / 60);
    const seconds = uptime % 60;
    return `${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
}


console.log("Server listening on port 3000");