#ifndef PIRSENSOR_H
#define PIRSENSOR_H


class PirSensor
{
public:
    explicit PirSensor(unsigned int pinNumber);
    unsigned int getAndClearPulseCount();
    void poll();
private:
    const unsigned int pinNumber;
    unsigned int pulseCount;
    int previousPinState;
};

#endif // PIRSENSOR_H
