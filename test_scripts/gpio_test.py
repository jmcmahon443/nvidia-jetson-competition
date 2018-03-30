   # Import Twisted mainloop
    
    from twisted.internet import reactor
    
    # Import this package objects
    
    from sysfs.gpio import Controller, OUTPUT, INPUT, RISING
    
    # Refer to your chip GPIO numbers and set them this way
    
    Controller.available_pins = [1, 2, 3, 4]
    
    # Allocate a pin as Output signal
    
    pin = Controller.alloc_pin(1, OUTPUT)
    pin.set()   # Sets pin to high logic level
    pin.reset() # Sets pin to low logic level
    pin.read()  # Reads pin logic level
    
    # Allocate a pin as simple Input signal
    
    pin = Controller.alloc_pin(1, INPUT)
    pin.read()  # Reads pin logic level
    
    # Allocate a pin as level triggered Input signal
    
    def pin_changed(number, state):
        print("Pin '%d' changed to %d state" % (number, state))
    
    pin = Controller.alloc_pin(1, INPUT, pin_changed, RISING)
    pin.read()  # Reads pin logic level
