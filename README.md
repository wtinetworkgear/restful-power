Power RESTful call to Western Telematic Inc. (WTI) devices.

This is a Simple Python3 script on how to talk to WTI PDU devices with a RESTful call to read power information.

This works on any modern WTI PDU/CPM device with power capabilities, the power RESTful call is universal on all WTI Power type devices.

To Configure:

To change the default values modify SITE_NAME to the address of your WTI device. Change the USERNAME and PASSWORD to the correct values for your WTI device.

To Run:
python3 power.py

The current power information and timestamp should display on the screen, otherwise if the WTI device you are talking to does not have power capabilities, there will be a message and the program will exit.

Documentation:

The HTML, RAML and OpenAPI file relating to the RESTful API calls can be found here:

https://www.wti.com/t-wti-restful-api-download.aspx

Contact US
If you have any questions, comments or suggestions you can email us at kenp@wti.com

About Us
WTI - Western Telematic, Inc.
5 Sterling, Irvine, California 92618

Western Telematic Inc. was founded in 1964 and is an industry leader in designing and manufacturing power management and remote console management solutions for data centers and global network locations.
Our extensive product line includes Intelligent PDUs for remote power distribution, metering, reporting and control, Serial Console Servers, RJ45 A/B Fallback Switches and Automatic Power Transfer Switches.
