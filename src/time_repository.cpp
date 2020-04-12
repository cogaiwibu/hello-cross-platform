//
// Created by Huynh Tan Ngan on 4/12/20.
//

#include "time_repository.h"
#include <ctime>
#include <iomanip>
#include <sstream>

std::string TimeRepository::GetCurrentTime() {
    auto t = std::time(nullptr);
    auto tm = *std::localtime(&t);

    std::ostringstream oss;
    oss << std::put_time(&tm, "%d-%m-%Y %H:%M:%S");
    return oss.str();
}
