#ifndef PIRIRQHANDLER_H
#define PIRIRQHANDLER_H
#include <map>

class IGpioIrqListener
{
};

typedef void(IGpioIrqListener::*GpioIrqCallback)();

class GpioIrqHandler
{
public:
    GpioIrqHandler();

    bool registerListener(unsigned int pin, IGpioIrqListener* listener, GpioIrqCallback callback);
    void unregisterListener(unsigned int pin);
private:
    std::map<unsigned int, std::pair<IGpioIrqListener, GpioIrqCallback> > irqMap;
};

#endif // PIRIRQHANDLER_H
