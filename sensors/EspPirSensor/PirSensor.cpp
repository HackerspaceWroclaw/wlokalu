#include "PirSensor.h"
#include <algorithm>
#include <Arduino.h>

PirSensor::PirSensor(unsigned int pinNumber):
    pinNumber(pinNumber),
    pulseCount(0),
    previousPinState(LOW)
{
    pinMode(pinNumber, INPUT);
}

unsigned int PirSensor::getAndClearPulseCount()
{
     auto currentPulseCount = pulseCount;
     pulseCount = 0U;
     return currentPulseCount;
}

void PirSensor::poll()
{
    auto pinState = digitalRead(pinNumber);

    if(pinState == HIGH && previousPinState == LOW)
        ++pulseCount;

    previousPinState = pinState;
}
