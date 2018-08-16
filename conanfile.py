from conans import ConanFile


class ErrConan(ConanFile):
    name = "Err"
    version = "1.0.0"
    requires = 'ConfigEx/1.0.0@microblink/stable'
    license = "Boost Software License"
    url = "https://github.com/microblink/err"
    description = 'err - yet another take on C++ error handling'
    generators = "cmake"
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }
    no_copy_source = True


    def package(self):
        self.copy("include/*.hpp")


    def package_id(self):
        self.info.header_only()

