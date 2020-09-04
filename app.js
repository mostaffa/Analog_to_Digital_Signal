const debug = require('debug')('analog-to-digital-signal');
const express = require('express')
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const Mcp3008 = require('mcp3008.js')
adc = new Mcp3008();
const index = require('./routes/index')

let run = false;




var app = express()
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.set('port', process.env.PORT || 3005);

app.use('/', index);

var server = app.listen(app.get('port'), function () {
    debug('Express server listening on port ' + server.address().port);
});
var io = require('socket.io').listen(server);
io.on('connection', function (socket) {
   const channel= function readChannels() {
        let obj = {
            channel0: 0,
            channel1: 0,
            channel2: 0,
            channel3: 0,
            channel4: 0,
            channel5: 0,
            channel6: 0,
            channel7: 0,
        }
        adc.read(0, v0 => {
            obj.channel0 = v0;
            adc.read(1, v1 => {
                obj.channel1 = v1;
                adc.read(2, v2 => {
                    obj.channel2 = v2;
                    adc.read(3, v3 => {
                        obj.channel3 = v3;
                        adc.read(4, v4 => {
                            obj.channel4 = v4;
                            adc.read(5, v5 => {
                                obj.channel5 = v5;
                                adc.read(6, v6 => {
                                    obj.channel6 = v6;
                                    adc.read(7, v7 => {
                                        obj.channel7 = v7;
                                        socket.emit("channels", obj)
                                    })
                                })
                            })
                        })
                    })
                })
            })
        }); 
    }
    run = true
    let interval = null;
    if(run)
    interval = setInterval(channel, 100);
    socket.on('con', function (data) {
        interval = setInterval(channel, 300);
        run = true
    });

    socket.on("dis", data => {
        run = false
        clearInterval(interval)
    });
});
