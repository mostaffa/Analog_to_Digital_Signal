# Analog_to_Digital_Signal
Receive an analog signal, convert it to digital, to be handled with micro controllers ARM processors using [MCP3008](https://cdn-shop.adafruit.com/datasheets/MCP3008.pdf)  IC.
<p>Using Raspberry Pi4 and nodejs and python</p>
<p>Connect the MCP3008 pins to Raspberry pi in this order:</p>

<pre>
         ____
  CH0 __|    |__VDD
  CH1 __|    |__VREF
  CH2 __|    |__AGND
  CH3 __|    |__CLK
  CH4 __|    |__Dout
  CH5 __|    |__Din
  CH6 __|    |__CS/SHDN
  CH7 __|____|__DGND</pre>
        
<ol>
    <li><pre>MCP3008 (VDD)  =======> Raspberry (3.3v)</pre></li>
    <li><pre>MCP3008 (Vref) =======> Raspberry (3.3v)</pre></li>
    <li><pre>MCP3008 (AGND) =======> Raspberry (GND)</pre></li>
    <li><pre>MCP3008 (CLK)  =======> Raspberry PIN23(SCLK)</pre></li>
    <li><pre>MCP3008 (Dout) =======> Raspberry PIN21(MISO)</pre></li>
    <li><pre>MCP3008 (Din)  =======> Raspberry PIN19(MOSI)</pre></li>
    <li><pre>MCP3008 (CS/SHDN) ====> Raspberry PIN22(CE0)</pre></li>
    <li><pre>MCP3008 (DGND) =======> Raspberry (GND)</pre></li>
</ol>