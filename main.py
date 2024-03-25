serial.set_baud_rate(BaudRate.BAUD_RATE115200)
microIoT.microIoT_WIFI("TheMosConnect", "BigSpiceLive")
serial.write_line("Wifi Complete")
