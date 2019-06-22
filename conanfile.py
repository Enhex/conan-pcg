import os

from conans import ConanFile, tools


class PcgConan(ConanFile):
    name = "pcg"
    version = "master"
    license = "MIT"
    url = "https://github.com/Enhex/conan-pcg"
    description = "PCG random number generator."
    topics = ("RNG")
    no_copy_source = True
    # No settings/options are necessary, this is header only

    def source(self):
        self.run("git clone --depth=1 https://github.com/imneme/pcg-cpp.git .")

    def package(self):
        self.copy("*.hpp", dst="include", src="include")
