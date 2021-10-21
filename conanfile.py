from conans import ConanFile, CMake
from conans import tools
from conans.tools import os_info, SystemPackageTool
import os, sys
import sysconfig
from io import StringIO

class ExportMKVConan(ConanFile):
    name = "spline_opt"
    version = "0.1.0"

    description = "export_mkv_k4a"
    url = "https://github.com/lennart7/spline-opt"
    license = "GPL"

    short_paths = True
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "virtualrunenv", "cmake_find_package_multi"

    requires = (
        "ceres-solver/2.0.0",
    )

    default_options = {
    }

    # all sources are deployed with the package
    exports_sources = "cmake/*", "include/*", "src/*", "CMakeLists.txt"

    def configure(self):
        pass

    def imports(self):
        self.copy(src="bin", pattern="*.dll", dst="./bin") # Copies all dll files from packages bin folder to my "bin" folder
        self.copy(src="lib", pattern="*.dll", dst="./bin") # Copies all dll files from packages bin folder to my "bin" folder
        self.copy(src="lib", pattern="*.dylib*", dst="./lib") # Copies all dylib files from packages lib folder to my "lib" folder
        self.copy(src="lib", pattern="*.so*", dst="./lib") # Copies all so files from packages lib folder to my "lib" folder
        self.copy(src="lib", pattern="*.a", dst="./lib") # Copies all static libraries from packages lib folder to my "lib" folder
        self.copy(src="bin", pattern="*", dst="./bin") # Copies all applications

    def _cmake_configure(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        return cmake
       
    def build(self):
        cmake = self._cmake_configure()
        cmake.build()

    def package(self):
        cmake = self._cmake_configure()
        cmake.install()
