//
// Created by Huynh Tan Ngan on 4/12/20.
//

#include <iostream>
#include "time_repository.h"

int main() {
    TimeRepository time_repository;
    auto current_time = time_repository.GetCurrentTime();
    std::cout << "Current time: " << current_time << std::endl;
    return 0;
}
