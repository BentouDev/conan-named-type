from conans import ConanFile, CMake, tools
import os, platform

named_type_version = os.getenv('NAMED_TYPE_VERSION', '1.0')

class NamedTypeConan(ConanFile):
    name = "named-type"
    license = "MIT"
    url = "https://github.com/BentouDev/conan-named-type"
    version = named_type_version

    description = "NamedType can be used to declare a strong type with a typedef-like syntax"
    no_copy_source = True
    exports_sources = ["named-type-source/*"]

    def package_id(self):
        self.info.header_only()

    def package(self):
        self.copy(pattern="*.hpp", dst="include", src="named-type-source")