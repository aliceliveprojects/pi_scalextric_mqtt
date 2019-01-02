const express = require('express');
const http = require('http')
const path = require('path');
var fs = require('fs');


var getClientConfig = function () {
  var result = {};

  if(!process.env.BROKER_HOST) process.env.BROKER_HOST = '';
  if(!process.env.BROKER_PORT) process.env.BROKER_PORT = '';
  
  result.HOST = process.env.BROKER_HOST;
  result.PORT = process.env.BROKER_PORT;
  
  return result;
}

var writeClientConfig = function(config){
  var client_config = config;
  client_config = "angular.module('app').constant('brokerDetails'," + JSON.stringify(client_config) + ");";
  fs.writeFileSync('./app/components/brokerDetails/brokerDetailsConstant.js',client_config);
}

writeClientConfig(getClientConfig());


const app = express();

app.use(express.static(path.join(__dirname, '')));

app.get('/*', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
});

const port = process.env.PORT || 8080;
app.set('port', port);

const server = http.createServer(app);
server.listen(port, () => console.log('running'));