import machine
import utime

led = machine.Pin("LED", machine.Pin.OUT)
led_pin = machine.Pin(25, machine.Pin.OUT)

while True:
    led_pin.value(1)
    led.on()
    print("ON")
    utime.sleep(2)
    led_pin.value(0)
    led.off()
    print("OFF")
    utime.sleep(2)