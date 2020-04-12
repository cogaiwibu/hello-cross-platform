from distutils.spawn import find_executable


def get_cmake_executable():
    cmake_executable = find_executable('cmake')
    if not cmake_executable:
        raise Exception('Could not find cmake executable')

    return cmake_executable
