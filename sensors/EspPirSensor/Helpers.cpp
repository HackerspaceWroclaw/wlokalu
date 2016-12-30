#include "Helpers.h"
#include <cstdio>

using namespace ::hswro::esppirsensor;

std::string helpers::toString(uint32_t value)
{
    char buffer[32];
    snprintf(buffer, sizeof(buffer), "%u", value);
    return std::string(buffer);
}

std::string helpers::toString(int32_t value)
{
    char buffer[32];
    snprintf(buffer, sizeof(buffer), "%d", value);
    return std::string(buffer);
}

std::string helpers::toString(double value)
{
    char buffer[64];
    snprintf(buffer, sizeof(buffer), "%lf", value);
    return std::string(buffer);
}
