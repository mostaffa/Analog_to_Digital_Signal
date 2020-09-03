var Mcp3008 = require('mcp3008.js'),
    adc = new Mcp3008(),
    channel = 0;

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
setInterval(function(){
    adc.read(0, v0=> {
        obj.channel0 = v0;
        adc.read(1,v1=>{
            obj.channel1 = v1;
            adc.read(2, v2=>{
                obj.channel2 = v2;
                adc.read(3, v3=>{
                    obj.channel3 = v3;
                    adc.read(4, v4=>{
                        obj.channel4 = v4;
                        adc.read(5, v5=>{
                            obj.channel5 = v5;
                            adc.read(6, v6=>{
                                obj.channel6 = v6;
                                adc.read(7, v7=>{
                                    obj.channel7 = v7;
                                    console.log(obj)
                                })
                            })
                        })
                    })
                })
            })
        })
    });
}, 100)