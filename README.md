Power RESTful call to Western Telematic Inc. (WTI) devices.

This is a Simple Python script on how to talk to WTI PDU devices with a RESTful call to read power information.

This works on any modern WTI PDU device with power capabilities, the power RESTful call is universal on all WTI PDU type devices.

To Configure:

Change your BASE_PATH to the address of your WTI PDU device
Change your USERNAME and PASSWORD to the correct values for your WTI PDU device.

To Run:
python power.py

The current power information and timestamp should repeat on the screen, otherwise if the WTI device you are talking to does not have power capabilities, there will be a message and the program will exit.

Documentation:

The HTML or RAML file relating to the RESTful API calls can be found here:

https://www.wti.com/t-wti-restful-api-download.aspx

Contact US
If you have any questions, comments or suggestions you can email us at kenp@wti.com

About Us
WTI - Western Telematic, Inc.
5 Sterling, Irvine, California 92618

Western Telematic Inc. was founded in 1964 and is an industry leader in designing and manufacturing power management and remote console management solutions for data centers and global network locations.
Our extensive product line includes Intelligent PDUs for remote power distribution, metering, reporting and control, Serial Console Servers, RJ45 A/B Fallback Switches and Automatic Power Transfer Switches.
