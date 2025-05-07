r"""Wrapper for rcim_client.h

Generated with:
/Users/haiyin/code/python/rc-im-mcp-demo/.venv/bin/ctypesgen -o lib/rcim_client.py -l librust_universal_imsdk lib/rcim_client.h

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):
    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["librust_universal_imsdk"] = load_library("librust_universal_imsdk")

# 1 libraries
# End libraries

# No modules

uint8_t = c_ubyte# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types/_uint8_t.h: 31

uint32_t = c_uint# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types/_uint32_t.h: 31

uint64_t = c_ulonglong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types/_uint64_t.h: 31

enum_RcimAppState = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 37

RcimAppState_Foreground = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 37

RcimAppState_Background = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 37

RcimAppState_Hangup = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 37

RcimAppState_Terminate = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 37

RcimAppState = enum_RcimAppState# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 37

enum_RcimAreaCode = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 63

RcimAreaCode_Bj = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 63

RcimAreaCode_Sg = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 63

RcimAreaCode_Na = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 63

RcimAreaCode_SgB = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 63

RcimAreaCode_Sa = 5# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 63

RcimAreaCode = enum_RcimAreaCode# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 63

enum_RcimChatroomMemberActionType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 77

RcimChatroomMemberActionType_Quit = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 77

RcimChatroomMemberActionType_Join = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 77

RcimChatroomMemberActionType = enum_RcimChatroomMemberActionType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 77

enum_RcimChatroomMemberBannedEventType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 115

RcimChatroomMemberBannedEventType_UnmuteUser = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 115

RcimChatroomMemberBannedEventType_MuteUsers = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 115

RcimChatroomMemberBannedEventType_UnmuteAll = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 115

RcimChatroomMemberBannedEventType_MuteAll = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 115

RcimChatroomMemberBannedEventType_RemoveWhitelist = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 115

RcimChatroomMemberBannedEventType_AddWhitelist = 5# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 115

RcimChatroomMemberBannedEventType_UnmuteGlobal = 6# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 115

RcimChatroomMemberBannedEventType_MuteGlobal = 7# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 115

RcimChatroomMemberBannedEventType = enum_RcimChatroomMemberBannedEventType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 115

enum_RcimChatroomMemberBlockedEventType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 129

RcimChatroomMemberBlockedEventType_Unblock = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 129

RcimChatroomMemberBlockedEventType_Block = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 129

RcimChatroomMemberBlockedEventType = enum_RcimChatroomMemberBlockedEventType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 129

enum_RcimChatroomMultiClientSyncEventType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 145

RcimChatroomMultiClientSyncEventType_Quit = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 145

RcimChatroomMultiClientSyncEventType_Join = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 145

RcimChatroomMultiClientSyncEventType = enum_RcimChatroomMultiClientSyncEventType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 145

enum_RcimChatroomMultiClientSyncQuitType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 159

RcimChatroomMultiClientSyncQuitType_Manual = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 159

RcimChatroomMultiClientSyncQuitType_Kick = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 159

RcimChatroomMultiClientSyncQuitType = enum_RcimChatroomMultiClientSyncQuitType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 159

enum_RcimChatroomStatus = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

RcimChatroomStatus_Idle = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

RcimChatroomStatus_Joining = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

RcimChatroomStatus_Joined = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

RcimChatroomStatus_JoinFailed = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

RcimChatroomStatus_Leaving = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

RcimChatroomStatus_Left = 5# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

RcimChatroomStatus_LeaveFailed = 6# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

RcimChatroomStatus_DestroyManually = 7# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

RcimChatroomStatus_DestroyAuto = 8# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

RcimChatroomStatus = enum_RcimChatroomStatus# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 201

enum_RcimCloudType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 219

RcimCloudType_PublicCloud = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 219

RcimCloudType_PrivateCloud = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 219

RcimCloudType_PrivateCloud104 = (RcimCloudType_PrivateCloud + 1)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 219

RcimCloudType = enum_RcimCloudType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 219

enum_RcimConnectionStatus = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_Idle = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_Connecting = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_Connected = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_Disconnecting = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectNetworkUnavailable = 10# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectUserLogout = 11# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectLicenseExpired = 12# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectLicenseMismatch = 13# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectIllegalProtocolVersion = 14# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectIdReject = 15# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectPlatformUnavailable = 16# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectTokenIncorrect = 17# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectNotAuthorized = 18# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectPackageNameInvalid = 19# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectAppBlockOrDelete = 20# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectUserBlocked = 21# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectUserKicked = 22# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectTokenExpired = 23# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectDeviceError = 24# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectHostnameError = 25# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectOtherDeviceLogin = 26# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectConcurrentLimitError = 27# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectClusterError = 28# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectAppAuthFailed = 29# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectOneTimePasswordUsed = 30# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectPlatformError = 31# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectUserDeleteAccount = 32# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectConnectionTimeout = 33# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus_DisconnectDatabaseOpenFailed = 34# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

RcimConnectionStatus = enum_RcimConnectionStatus# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 354

enum_RcimConversationType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_NotSupportedYet = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_Private = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_Discussion = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_Group = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_Chatroom = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_CustomerService = 5# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_System = 6# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_AppPublicService = 7# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_PublicService = 8# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_PushService = 9# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_UltraGroup = 10# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_Encrypted = 11# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType_RtcRoom = 12# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

RcimConversationType = enum_RcimConversationType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 412

enum_RcimDatabaseStatus = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 446

RcimDatabaseStatus_Idle = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 446

RcimDatabaseStatus_OpenSuccess = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 446

RcimDatabaseStatus_OpenFailed = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 446

RcimDatabaseStatus_Upgrading = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 446

RcimDatabaseStatus_UpgradeSuccess = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 446

RcimDatabaseStatus_UpgradeFailed = 5# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 446

RcimDatabaseStatus_Error = 127# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 446

RcimDatabaseStatus = enum_RcimDatabaseStatus# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 446

enum_RcimDevLogLevel = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 459

RcimDevLogLevel_Error = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 459

RcimDevLogLevel_Warn = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 459

RcimDevLogLevel_Info = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 459

RcimDevLogLevel_Debug = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 459

RcimDevLogLevel_Trace = 5# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 459

RcimDevLogLevel = enum_RcimDevLogLevel# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 459

enum_RcimDisconnectMode = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 473

RcimDisconnectMode_KeepPush = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 473

RcimDisconnectMode_NoPush = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 473

RcimDisconnectMode = enum_RcimDisconnectMode# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 473

enum_RcimEngineError = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_Success = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_RejectedByBlackList = 405# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_NotWhitelisted = 407# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ForbiddenInPrivateChat = 20106# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConversationNotSupportMessage = 20109# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageSendOverFrequency = 20604# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_RequestOverFrequency = 20607# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageIncludeSensitiveWord = 21501# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageReplacedSensitiveWord = 21502# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_NotInGroup = 22406# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ForbiddenInGroupChat = 22408# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ForbiddenInChatroom = 23408# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKicked = 23409# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomNotExist = 23410# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomIsFull = 23411# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_NotInChatroom = 23406# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_GetUserError = 23407# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomInvalidParameter = 23412# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_QueryChatroomHistoryError = 23413# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_RoamingServiceUnavailableChatroom = 23414# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvCountExceed = 23423# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvOverwriteInvalidKey = 23424# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvCallAPIExceed = 23425# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvStoreUnavailable = 23426# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvNotExist = 23427# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvNotAllSuccess = 23428# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvLimit = 23429# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvConcurrentError = 23431# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_RecallParameterInvalid = 25101# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageStorageServiceUnavailable = 25102# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_RecallMessageUserInvalid = 25107# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_PushSettingParameterInvalid = 26001# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_SettingSyncFailed = 26002# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMessageUid = 26009# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_RequestUploadTokenSizeError = 26107# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidPublicService = 29201# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectionClosed = 30001# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectionClosing = 30027# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_SocketRecvTimeout = 30003# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_NaviReqFailed = 30004# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_NaviReqTimeout = 30005# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MsgSizeOutOfLimit = 30016# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_SocketSendTimeout = 30022# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_NaviRespTokenIncorrect = 30024# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_NaviLicenseMismatch = 30026# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_HttpReqFailed = 34026# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_HttpReqTimeout = 34027# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectIllegalProtocolVersion = 31001# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectIdReject = 31002# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectPlatformUnavailable = 31003# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectTokenIncorrect = 31004# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectNotAuthorized = 31005# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectRedirect = 31006# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectPackageNameInvalid = 31007# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectAppBlockOrDelete = 31008# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectUserBlocked = 31009# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DisconnectUserKicked = 31010# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DisconnectUserBlocked = 31011# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DisconnectUserLogout = 31012# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_SocketConnectionFailed = 31014# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_SocketShutdownFailed = 31015# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectionCancel = 31016# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectTokenExpired = 31020# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectDeviceError = 31021# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectHostnameError = 31022# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectOtherDeviceLogin = 31023# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectConcurrentLimitError = 31024# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectClusterError = 31025# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectAppAuthFailed = 31026# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectOneTimePasswordUsed = 31027# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectPlatformError = 31028# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectUserDeleteAccount = 31029# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectLicenseExpired = 31030# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_KvStoreNotOpened = 31510# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_KvStoreOpenFailed = 31511# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_KvStoreIOError = 31512# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_KvStoreSerializationError = 31513# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_JsonParserFailed = 31610# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ImageFormatError = 31611# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_RequestUploadTokenError = 31612# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_GetUploadTokenError = 31613# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_SightMessageCompressError = 31614# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_RequestCanceled = 33200# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DownloadRequestExist = 33202# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_RequestPaused = 33204# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DownloadTaskNotExist = 33205# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_UploadTaskNotExist = 33206# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MediaMessageHandlerError = 33207# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectRefused = 32061# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageSavedError = 33000# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectionInProcess = 33006# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CloudStorageForHistoryMessageDisable = 33007# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectionExists = 34001# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_GifMessageSizeOutOfLimit = 34003# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ConnectionTimeout = 34006# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageCantExpand = 34008# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageExpansionSizeLimitExceed = 34010# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_UploadMediaFailed = 34011# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_GroupReadReceiptVersionNotSupport = 34014# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_UserSettingUnavailable = 34016# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageNotRegistered = 34021# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageExpandConversationTypeNotMatch = 34025# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentUltraGroupNotSupport = 34022# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentAppKey = 34105# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentTimestamp = 34202# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMessageContent = 34205# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMessageVec = 34206# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentConversationType = 34209# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentTargetId = 34210# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidParameterMessageExpansion = 34220# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentChannelId = 34211# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentContentNotMedia = 34223# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentFileNameEmpty = 33201# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentTimeString = 34224# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidEnumOutOfRange = 34225# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentPushNotificationMuteLevel = 34228# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMessageIdVec = 34229# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentCount = 34232# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMediaLocalPath = 34234# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMediaUrl = 34235# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMessage = 34243# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentSentStatus = 34244# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvInvalidKey = 34260# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvInvalidKeyVec = 34261# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvInvalidValue = 34262# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_ChatroomKvInvalidKeyValueVec = 34263# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMessageDirectionEmpty = 34267# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentObjectName = 34271# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentLimit = 34279# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMessageDirection = 34280# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentSpanMinutes = 34283# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentConversationTypeVec = 34284# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentNaviUrl = 34286# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentConversationIdentifierVec = 34287# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DirectionalMessageNotSupport = 34296# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageDestructing = 34297# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_MessageNotDestructing = 23298# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidParameterReceivedStatus = 34230# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidParameterUserId = 34214# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidParameterUserList = 34215# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DatabaseNotOpened = 34301# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DatabaseOpenFailed = 34302# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DatabaseIOError = 34303# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DatabaseTargetNotFound = 34304# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_NetDataParserFailed = 34305# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_DatabaseThreadError = 34316# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_EngineDropped = 34400# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_SightMsgDurationLimit = 34002# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentEngineSync = 34401# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentEngineBuilder = 34402# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentDeviceId = 34403# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentPackageName = 34404# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentSdkVersion = 34405# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentFileStoragePath = 34406# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentToken = 34407# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMessageId = 34408# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentMessageType = 34409# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentNotMediaMessage = 34410# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentUserIdEmpty = 34411# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentAudioDuration = 34413# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentLogInfo = 34414# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentEngineBuilderParam = 34415# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentDeviceModel = 34416# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentDeviceManufacturer = 34417# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentPushTokenVec = 34418# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentPushType = 34419# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentPushToken = 34420# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentSenderId = 34421# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentPushNotificationMuteLevelVec = 34422# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentConnectionStatus = 34423# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentVersion = 34424# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentOsVersion = 34425# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentAppVersion = 34426# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentStatisticUrl = 34427# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentDraft = 34428# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentKeyword = 34429# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentOffset = 34430# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentObjectNameVec = 34431# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentTimeInterval = 34432# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentTimeoutSeconds = 34433# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentDestructDuration = 34434# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentUniqueId = 34435# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentOutUniqueId = 34436# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentOutUserId = 34437# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentExtra = 34438# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentChatroomId = 36001# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentRtcMethodName = 36002# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentRtcKey = 36003# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_InvalidArgumentRtcValue = 36004# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallNotInRoom = 40001# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallInternalError = 40002# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallHasNoRoom = 40003# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallInvalidUserId = 40004# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallLimitError = 40005# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallParamError = 40006# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallTokenError = 40007# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallDbError = 40008# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallJsonError = 40009# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallNotOpen = 40010# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallRoomTypeError = 40011# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallNoAuthUser = 40012# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallHasNoConfigMcuAddress = 40015# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallNotAllowVideoBroadcast = 40016# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallNotAllowAudioBroadcast = 40017# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallGetTokenError = 40018# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallUserIsBlocked = 40021# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallInviteRoomNotExist = 40022# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallInviteUserNotInRoom = 40023# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallInviteInProgress = 40024# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallCancelInviteNotProgress = 40025# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallAnswerInviteNotProgress = 40026# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallAnswerInviteTimeout = 40027# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallPingNotProgress = 40028# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallRoomAlreadyExist = 40029# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallRoomTypeNotSupport = 40030# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallIdentityChangeTypeError = 40031# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallAlreadyJoinRoom = 40032# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallNotAllowCrossApp = 40033# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallUserNotAllowedForRtc = 40034# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallConcurrentLimitError = 40130# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallExpiredError = 40131# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusUnknownError = 41000# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusDbError = 41001# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusJsonError = 41002# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusInvalidJsonFormat = 41003# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusMissingParameters = 41004# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusOperationNotPermitted = 41005# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusCircuitBreakerOpen = 41006# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusMethodNotImplement = 41007# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusCallingUserNotRegistCallServer = 41008# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusNotSupportNewCall = 41009# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusCallNotExist = 41010# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusSingleCallOverload = 41011# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusGroupCallOverload = 41012# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusOperationHasExpired = 41013# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusDeviceHasCalling = 41014# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusCallUserNotInCall = 41015# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusDataHasExpired = 41016# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusStreamReadyTimeInvalid = 41018# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusCallNotSelf = 41019# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusStateNotExist = 41020# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusHangupNotAllowed = 41021# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusAcceptNotAllowed = 41022# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusOperationNotAllowed = 41025# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusTransactionNotExist = 41100# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusMediaTypeSwitching = 41101# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusAudioToVideoCancel = 41150# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusVideoToAudioNoRequired = 41151# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusAudioToVideoNoRequired = 41152# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_CallplusNoCompensationData = 41200# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError_NotSupportedYet = 99999# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

RcimEngineError = enum_RcimEngineError# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1576

enum_RcimLogLevel = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1602

RcimLogLevel_None = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1602

RcimLogLevel_Error = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1602

RcimLogLevel_Warn = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1602

RcimLogLevel_Info = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1602

RcimLogLevel_Debug = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1602

RcimLogLevel = enum_RcimLogLevel# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1602

enum_RcimLogSource = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1615

RcimLogSource_RUST = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1615

RcimLogSource_FFI = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1615

RcimLogSource_IMLib = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1615

RcimLogSource_IMKit = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1615

RcimLogSource_RTCLib = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1615

RcimLogSource_CallLib = 5# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1615

RcimLogSource_CallPlus = 6# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1615

RcimLogSource = enum_RcimLogSource# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1615

enum_RcimLogType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1623

RcimLogType_IM = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1623

RcimLogType_RTC = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1623

RcimLogType = enum_RcimLogType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1623

enum_RcimMediaHandlerError = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1633

RcimMediaHandlerError_Success = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1633

RcimMediaHandlerError_Canceled = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1633

RcimMediaHandlerError_Paused = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1633

RcimMediaHandlerError_Failed = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1633

RcimMediaHandlerError = enum_RcimMediaHandlerError# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1633

enum_RcimMessageBlockSourceType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1642

RcimMessageBlockSourceType_Default = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1642

RcimMessageBlockSourceType_Extension = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1642

RcimMessageBlockSourceType_Modification = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1642

RcimMessageBlockSourceType = enum_RcimMessageBlockSourceType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1642

enum_RcimMessageBlockType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1652

RcimMessageBlockType_None = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1652

RcimMessageBlockType_BlockGlobal = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1652

RcimMessageBlockType_BlockCustom = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1652

RcimMessageBlockType_BlockThirdParty = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1652

RcimMessageBlockType = enum_RcimMessageBlockType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1652

enum_RcimMessageDirection = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1670

RcimMessageDirection_Send = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1670

RcimMessageDirection_Receive = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1670

RcimMessageDirection = enum_RcimMessageDirection# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1670

enum_RcimMessageFlag = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1693

RcimMessageFlag_None = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1693

RcimMessageFlag_Save = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1693

RcimMessageFlag_Count = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1693

RcimMessageFlag_Status = 16# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1693

RcimMessageFlag = enum_RcimMessageFlag# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1693

enum_RcimNetworkType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1727

RcimNetworkType_None = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1727

RcimNetworkType_Wifi = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1727

RcimNetworkType_Wired = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1727

RcimNetworkType_Cellular2G = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1727

RcimNetworkType_Cellular3G = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1727

RcimNetworkType_Cellular4G = 5# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1727

RcimNetworkType_Cellular5G = 6# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1727

RcimNetworkType = enum_RcimNetworkType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1727

enum_RcimOrder = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1741

RcimOrder_Descending = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1741

RcimOrder_Ascending = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1741

RcimOrder = enum_RcimOrder# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1741

enum_RcimPlatform = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

RcimPlatform_Android = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

RcimPlatform_IOS = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

RcimPlatform_HarmonyOS = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

RcimPlatform_Windows = 3# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

RcimPlatform_MacOS = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

RcimPlatform_Linux = 5# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

RcimPlatform_Electron = 6# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

RcimPlatform_Web = 7# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

RcimPlatform_Unknown = 127# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

RcimPlatform = enum_RcimPlatform# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1759

enum_RcimPublicServiceMenuItemType = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1777

RcimPublicServiceMenuItemType_Group = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1777

RcimPublicServiceMenuItemType_View = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1777

RcimPublicServiceMenuItemType_Click = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1777

RcimPublicServiceMenuItemType = enum_RcimPublicServiceMenuItemType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1777

enum_RcimPushNotificationMuteLevel = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1810

RcimPushNotificationMuteLevel_All = (-1)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1810

RcimPushNotificationMuteLevel_Default = 0# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1810

RcimPushNotificationMuteLevel_Mention = 1# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1810

RcimPushNotificationMuteLevel_MentionUsers = 2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1810

RcimPushNotificationMuteLevel_MentionAll = 4# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1810

RcimPushNotificationMuteLevel_Blocked = 5# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1810

RcimPushNotificationMuteLevel = enum_RcimPushNotificationMuteLevel# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1810

enum_RcimSentStatus = c_int# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1841

RcimSentStatus_SENDING = 10# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1841

RcimSentStatus_FAILED = 20# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1841

RcimSentStatus_SENT = 30# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1841

RcimSentStatus_RECEIVED = 40# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1841

RcimSentStatus_READ = 50# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1841

RcimSentStatus_DESTROYED = 60# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1841

RcimSentStatus_CANCELED = 70# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1841

RcimSentStatus = enum_RcimSentStatus# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1841

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1846
class struct_RcimEngineBuilder(Structure):
    pass

RcimEngineBuilder = struct_RcimEngineBuilder# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1846

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1851
class struct_RcimEngineSync(Structure):
    pass

RcimEngineSync = struct_RcimEngineSync# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1851

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1865
class struct_RcimSDKVersion(Structure):
    pass

struct_RcimSDKVersion.__slots__ = [
    'name',
    'version',
]
struct_RcimSDKVersion._fields_ = [
    ('name', String),
    ('version', String),
]

RcimSDKVersion = struct_RcimSDKVersion# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1865

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1920
class struct_RcimEngineBuilderParam(Structure):
    pass

struct_RcimEngineBuilderParam.__slots__ = [
    'app_key',
    'platform',
    'device_id',
    'package_name',
    'imlib_version',
    'device_model',
    'device_manufacturer',
    'os_version',
    'sdk_version_vec',
    'sdk_version_vec_len',
    'app_version',
]
struct_RcimEngineBuilderParam._fields_ = [
    ('app_key', String),
    ('platform', enum_RcimPlatform),
    ('device_id', String),
    ('package_name', String),
    ('imlib_version', String),
    ('device_model', String),
    ('device_manufacturer', String),
    ('os_version', String),
    ('sdk_version_vec', POINTER(struct_RcimSDKVersion)),
    ('sdk_version_vec_len', c_int32),
    ('app_version', String),
]

RcimEngineBuilderParam = struct_RcimEngineBuilderParam# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1920

RcimDatabaseStatusLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimDatabaseStatus)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1928

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1942
class struct_RcimPushTokenInfo(Structure):
    pass

struct_RcimPushTokenInfo.__slots__ = [
    'push_type',
    'push_token',
]
struct_RcimPushTokenInfo._fields_ = [
    ('push_type', String),
    ('push_token', String),
]

RcimPushTokenInfo = struct_RcimPushTokenInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1942

RcimConnectionStatusLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimConnectionStatus)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1950

RcimConnectCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, String)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1959

RcimEngineErrorCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1967

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1978
class struct_RcimReceivedStatus(Structure):
    pass

struct_RcimReceivedStatus.__slots__ = [
    'is_read',
    'is_listened',
    'is_download',
    'is_retrieved',
    'is_multiple_received',
]
struct_RcimReceivedStatus._fields_ = [
    ('is_read', c_bool),
    ('is_listened', c_bool),
    ('is_download', c_bool),
    ('is_retrieved', c_bool),
    ('is_multiple_received', c_bool),
]

RcimReceivedStatus = struct_RcimReceivedStatus# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1978

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1992
class struct_RcimReadReceiptUserInfo(Structure):
    pass

struct_RcimReadReceiptUserInfo.__slots__ = [
    'sender_id',
    'timestamp',
]
struct_RcimReadReceiptUserInfo._fields_ = [
    ('sender_id', String),
    ('timestamp', uint64_t),
]

RcimReadReceiptUserInfo = struct_RcimReadReceiptUserInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1992

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2008
class struct_RcimReadReceiptInfo(Structure):
    pass

struct_RcimReadReceiptInfo.__slots__ = [
    'is_read_receipt_message',
    'has_respond',
    'respond_user_vec',
    'respond_user_vec_len',
]
struct_RcimReadReceiptInfo._fields_ = [
    ('is_read_receipt_message', c_bool),
    ('has_respond', c_bool),
    ('respond_user_vec', POINTER(struct_RcimReadReceiptUserInfo)),
    ('respond_user_vec_len', c_int32),
]

RcimReadReceiptInfo = struct_RcimReadReceiptInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2008

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2028
class struct_RcimReadReceiptInfoV2(Structure):
    pass

struct_RcimReadReceiptInfoV2.__slots__ = [
    'has_respond',
    'respond_user_vec',
    'respond_user_vec_len',
    'read_count',
    'total_count',
]
struct_RcimReadReceiptInfoV2._fields_ = [
    ('has_respond', c_bool),
    ('respond_user_vec', POINTER(struct_RcimReadReceiptUserInfo)),
    ('respond_user_vec_len', c_int32),
    ('read_count', uint32_t),
    ('total_count', uint32_t),
]

RcimReadReceiptInfoV2 = struct_RcimReadReceiptInfoV2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2028

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2060
class struct_RcimIosConfig(Structure):
    pass

struct_RcimIosConfig.__slots__ = [
    'thread_id',
    'category',
    'apns_collapse_id',
    'rich_media_uri',
    'interruption_level',
]
struct_RcimIosConfig._fields_ = [
    ('thread_id', String),
    ('category', String),
    ('apns_collapse_id', String),
    ('rich_media_uri', String),
    ('interruption_level', String),
]

RcimIosConfig = struct_RcimIosConfig# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2060

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2146
class struct_RcimAndroidConfig(Structure):
    pass

struct_RcimAndroidConfig.__slots__ = [
    'notification_id',
    'mi_channel_id',
    'hw_channel_id',
    'hw_importance',
    'hw_image_url',
    'hw_category',
    'honor_importance',
    'honor_image_url',
    'oppo_channel_id',
    'vivo_category',
    'vivo_type',
    'fcm_channel_id',
    'fcm_collapse_key',
    'fcm_image_url',
]
struct_RcimAndroidConfig._fields_ = [
    ('notification_id', String),
    ('mi_channel_id', String),
    ('hw_channel_id', String),
    ('hw_importance', String),
    ('hw_image_url', String),
    ('hw_category', String),
    ('honor_importance', String),
    ('honor_image_url', String),
    ('oppo_channel_id', String),
    ('vivo_category', String),
    ('vivo_type', String),
    ('fcm_channel_id', String),
    ('fcm_collapse_key', String),
    ('fcm_image_url', String),
]

RcimAndroidConfig = struct_RcimAndroidConfig# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2146

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2161
class struct_RcimHarmonyConfig(Structure):
    pass

struct_RcimHarmonyConfig.__slots__ = [
    'image_url',
    'category',
]
struct_RcimHarmonyConfig._fields_ = [
    ('image_url', String),
    ('category', String),
]

RcimHarmonyConfig = struct_RcimHarmonyConfig# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2161

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2213
class struct_RcimPushConfig(Structure):
    pass

struct_RcimPushConfig.__slots__ = [
    'disable_push_title',
    'push_title',
    'push_content',
    'push_data',
    'force_show_detail_content',
    'ios_config',
    'android_config',
    'harmony_config',
]
struct_RcimPushConfig._fields_ = [
    ('disable_push_title', c_bool),
    ('push_title', String),
    ('push_content', String),
    ('push_data', String),
    ('force_show_detail_content', c_bool),
    ('ios_config', POINTER(struct_RcimIosConfig)),
    ('android_config', POINTER(struct_RcimAndroidConfig)),
    ('harmony_config', POINTER(struct_RcimHarmonyConfig)),
]

RcimPushConfig = struct_RcimPushConfig# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2213

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2321
class struct_RcimMessageBox(Structure):
    pass

struct_RcimMessageBox.__slots__ = [
    'conv_type',
    'target_id',
    'channel_id',
    'message_id',
    'direction',
    'sender_id',
    'received_status',
    'sent_status',
    'received_time',
    'sent_time',
    'object_name',
    'content',
    'searchable_words',
    'uid',
    'extra',
    'read_receipt_info',
    'read_receipt_info_v2',
    'is_notification_disabled',
    'push_config',
    'is_offline',
    'is_ext_supported',
    'ext_content',
]
struct_RcimMessageBox._fields_ = [
    ('conv_type', enum_RcimConversationType),
    ('target_id', String),
    ('channel_id', String),
    ('message_id', c_int64),
    ('direction', enum_RcimMessageDirection),
    ('sender_id', String),
    ('received_status', POINTER(struct_RcimReceivedStatus)),
    ('sent_status', enum_RcimSentStatus),
    ('received_time', c_int64),
    ('sent_time', c_int64),
    ('object_name', String),
    ('content', String),
    ('searchable_words', String),
    ('uid', String),
    ('extra', String),
    ('read_receipt_info', POINTER(struct_RcimReadReceiptInfo)),
    ('read_receipt_info_v2', POINTER(struct_RcimReadReceiptInfoV2)),
    ('is_notification_disabled', c_bool),
    ('push_config', POINTER(struct_RcimPushConfig)),
    ('is_offline', c_bool),
    ('is_ext_supported', c_bool),
    ('ext_content', String),
]

RcimMessageBox = struct_RcimMessageBox# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2321

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2330
class struct_RcimReceivedInfo(Structure):
    pass

struct_RcimReceivedInfo.__slots__ = [
    'left',
    'has_package',
    'is_offline',
]
struct_RcimReceivedInfo._fields_ = [
    ('left', c_int32),
    ('has_package', c_bool),
    ('is_offline', c_bool),
]

RcimReceivedInfo = struct_RcimReceivedInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2330

RcimMessageReceivedLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimMessageBox), POINTER(struct_RcimReceivedInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2339

RcimOfflineMessageSyncCompletedLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2348

RcimMessageSearchableWordsCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), String)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2359

RcimMessageSearchableWordsCbLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, String, POINTER(None), RcimMessageSearchableWordsCb)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2374

RcimSightCompressCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), String)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2389

RcimSightCompressCbLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), uint32_t, uint32_t, String, POINTER(None), RcimSightCompressCb)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2404

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2445
class struct_RcimRecallNotificationMessage(Structure):
    pass

struct_RcimRecallNotificationMessage.__slots__ = [
    'base_info',
    'operator_id',
    'recall_time',
    'original_object_name',
    'original_content',
    'recall_content',
    'action_time',
    'is_admin',
    'is_deleted',
]
struct_RcimRecallNotificationMessage._fields_ = [
    ('base_info', String),
    ('operator_id', String),
    ('recall_time', c_int64),
    ('original_object_name', String),
    ('original_content', String),
    ('recall_content', String),
    ('action_time', c_int64),
    ('is_admin', c_bool),
    ('is_deleted', c_bool),
]

RcimRecallNotificationMessage = struct_RcimRecallNotificationMessage# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2445

RcimRecallMessageLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimMessageBox), POINTER(struct_RcimRecallNotificationMessage))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2454

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2499
class struct_RcimMessageBlockInfo(Structure):
    pass

struct_RcimMessageBlockInfo.__slots__ = [
    'conv_type',
    'target_id',
    'channel_id',
    'uid',
    'extra',
    'block_type',
    'source_type',
    'source_content',
]
struct_RcimMessageBlockInfo._fields_ = [
    ('conv_type', enum_RcimConversationType),
    ('target_id', String),
    ('channel_id', String),
    ('uid', String),
    ('extra', String),
    ('block_type', enum_RcimMessageBlockType),
    ('source_type', enum_RcimMessageBlockSourceType),
    ('source_content', String),
]

RcimMessageBlockInfo = struct_RcimMessageBlockInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2499

RcimMessageBlockedLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimMessageBlockInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2507

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2530
class struct_RcimSendMessageOption(Structure):
    pass

struct_RcimSendMessageOption.__slots__ = [
    'is_voip_push',
    'user_ids',
    'user_ids_len',
    'encrypted',
]
struct_RcimSendMessageOption._fields_ = [
    ('is_voip_push', c_bool),
    ('user_ids', POINTER(POINTER(c_char))),
    ('user_ids_len', c_int32),
    ('encrypted', c_bool),
]

RcimSendMessageOption = struct_RcimSendMessageOption# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2530

RcimCodeMessageCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimMessageBox))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2539

RcimMessageCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimMessageBox))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2549

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2563
class struct_RcimSendReadReceiptResponseMessageData(Structure):
    pass

struct_RcimSendReadReceiptResponseMessageData.__slots__ = [
    'sender_id',
    'message_uid',
]
struct_RcimSendReadReceiptResponseMessageData._fields_ = [
    ('sender_id', String),
    ('message_uid', String),
]

RcimSendReadReceiptResponseMessageData = struct_RcimSendReadReceiptResponseMessageData# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2563

RcimGetMessageListCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimMessageBox), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2573

RcimMessageNotifyLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimMessageBox))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2584

RcimReadReceiptRequestLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimConversationType, String, String, String)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2595

RcimReadReceiptResponseLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimConversationType, String, String, String, POINTER(struct_RcimReadReceiptUserInfo), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2612

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2632
class struct_RcimReadReceiptV2ReaderInfo(Structure):
    pass

struct_RcimReadReceiptV2ReaderInfo.__slots__ = [
    'user_id',
    'read_time',
]
struct_RcimReadReceiptV2ReaderInfo._fields_ = [
    ('user_id', String),
    ('read_time', c_int64),
]

RcimReadReceiptV2ReaderInfo = struct_RcimReadReceiptV2ReaderInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2632

RcimGetReadReceiptV2ReaderListCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, uint32_t, POINTER(struct_RcimReadReceiptV2ReaderInfo), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2643

RcimReadReceiptResponseV2Lsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimConversationType, String, String, String, uint32_t, uint32_t)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2660

RcimSendMessageOnProgressCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimMessageBox), uint8_t)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2675

RcimMediaHandlerProgressCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2687

RcimMediaHandlerResultCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimMediaHandlerError, String)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2698

RcimMediaMessageHandlerCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimMessageBox), POINTER(None), RcimMediaHandlerProgressCb, RcimMediaHandlerResultCb)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2713

RcimDownloadMediaCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, String)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2726

RcimDownloadMessageProgressCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int64, uint8_t)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2735

RcimDownloadFileProgressCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, uint8_t)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2746

RcimRecallMessageCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimRecallNotificationMessage))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2757

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2774
class struct_RcimMessageType(Structure):
    pass

struct_RcimMessageType.__slots__ = [
    'object_name',
    'flag',
    'is_media_message',
]
struct_RcimMessageType._fields_ = [
    ('object_name', String),
    ('flag', enum_RcimMessageFlag),
    ('is_media_message', c_bool),
]

RcimMessageType = struct_RcimMessageType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2774

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2788
class struct_RcimMessageExpansionKvInfo(Structure):
    pass

struct_RcimMessageExpansionKvInfo.__slots__ = [
    'key',
    'value',
]
struct_RcimMessageExpansionKvInfo._fields_ = [
    ('key', String),
    ('value', String),
]

RcimMessageExpansionKvInfo = struct_RcimMessageExpansionKvInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2788

RcimMessageExpansionKvUpdateLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimMessageExpansionKvInfo), c_int32, POINTER(struct_RcimMessageBox))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2798

RcimMessageExpansionKvRemoveLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(POINTER(c_char)), c_int32, POINTER(struct_RcimMessageBox))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2811

RcimGetBoolCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, c_bool)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2822

RcimMessageDestructingLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimMessageBox), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2835

RcimMessageDestructionStopLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimMessageBox))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2848

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2882
class struct_RcimConversationStatusChangeItem(Structure):
    pass

struct_RcimConversationStatusChangeItem.__slots__ = [
    'conv_type',
    'target_id',
    'channel_id',
    'update_time',
    'pin_time',
    'is_pinned',
    'mute_level',
]
struct_RcimConversationStatusChangeItem._fields_ = [
    ('conv_type', enum_RcimConversationType),
    ('target_id', String),
    ('channel_id', String),
    ('update_time', c_int64),
    ('pin_time', POINTER(c_int64)),
    ('is_pinned', POINTER(c_bool)),
    ('mute_level', POINTER(enum_RcimPushNotificationMuteLevel)),
]

RcimConversationStatusChangeItem = struct_RcimConversationStatusChangeItem# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2882

RcimConversationStatusLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimConversationStatusChangeItem), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2891

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2908
class struct_RcimTypingStatus(Structure):
    pass

struct_RcimTypingStatus.__slots__ = [
    'user_id',
    'object_name',
    'sent_time',
]
struct_RcimTypingStatus._fields_ = [
    ('user_id', String),
    ('object_name', String),
    ('sent_time', uint64_t),
]

RcimTypingStatus = struct_RcimTypingStatus# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2908

RcimTypingStatusLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimConversationType, String, String, POINTER(struct_RcimTypingStatus), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2919

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2964
class struct_RcimConversation(Structure):
    pass

struct_RcimConversation.__slots__ = [
    'conv_type',
    'target_id',
    'channel_id',
    'unread_message_count',
    'is_pinned',
    'last_received_time',
    'last_sent_time',
    'last_operate_time',
    'object_name',
    'sender_user_id',
    'last_message_id',
    'last_message_content',
    'draft',
    'mute_level',
    'mentioned_count',
    'match_count',
]
struct_RcimConversation._fields_ = [
    ('conv_type', enum_RcimConversationType),
    ('target_id', String),
    ('channel_id', String),
    ('unread_message_count', c_int32),
    ('is_pinned', c_bool),
    ('last_received_time', c_int64),
    ('last_sent_time', c_int64),
    ('last_operate_time', c_int64),
    ('object_name', String),
    ('sender_user_id', String),
    ('last_message_id', c_int64),
    ('last_message_content', String),
    ('draft', String),
    ('mute_level', enum_RcimPushNotificationMuteLevel),
    ('mentioned_count', c_int32),
    ('match_count', uint32_t),
]

RcimConversation = struct_RcimConversation# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2964

RcimGetConversationCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimConversation))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2973

RcimGetConversationListCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimConversation), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2985

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2994
class struct_RcimConversationIdentifier(Structure):
    pass

struct_RcimConversationIdentifier.__slots__ = [
    'conv_type',
    'target_id',
    'channel_id',
]
struct_RcimConversationIdentifier._fields_ = [
    ('conv_type', enum_RcimConversationType),
    ('target_id', String),
    ('channel_id', String),
]

RcimConversationIdentifier = struct_RcimConversationIdentifier# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2994

RcimGetLocalConversationMuteLevelCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, enum_RcimPushNotificationMuteLevel)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3002

RcimGetNoDisturbingCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, String, c_int32, enum_RcimPushNotificationMuteLevel)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3015

RcimGetTextMessageDraftCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, String)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3028

RcimGetCountCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, c_int64)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3039

RcimConversationReadStatusLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimConversationType, String, String, c_int64)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3052

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3083
class struct_RcimChatroomJoinedInfo(Structure):
    pass

struct_RcimChatroomJoinedInfo.__slots__ = [
    'create_time',
    'member_count',
    'is_all_chatroom_banned',
    'is_current_user_banned',
    'is_current_chatroom_banned',
    'is_current_chatroom_in_whitelist',
]
struct_RcimChatroomJoinedInfo._fields_ = [
    ('create_time', c_int64),
    ('member_count', c_int32),
    ('is_all_chatroom_banned', c_bool),
    ('is_current_user_banned', c_bool),
    ('is_current_chatroom_banned', c_bool),
    ('is_current_chatroom_in_whitelist', c_bool),
]

RcimChatroomJoinedInfo = struct_RcimChatroomJoinedInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3083

RcimChatroomStatusLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, String, enum_RcimChatroomStatus, POINTER(struct_RcimChatroomJoinedInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3094

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3112
class struct_RcimChatroomMemberActionInfo(Structure):
    pass

struct_RcimChatroomMemberActionInfo.__slots__ = [
    'user_id',
    'action_type',
]
struct_RcimChatroomMemberActionInfo._fields_ = [
    ('user_id', String),
    ('action_type', enum_RcimChatroomMemberActionType),
]

RcimChatroomMemberActionInfo = struct_RcimChatroomMemberActionInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3112

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3134
class struct_RcimChatroomMemberChangeInfo(Structure):
    pass

struct_RcimChatroomMemberChangeInfo.__slots__ = [
    'room_id',
    'member_count',
    'action_vec',
    'action_vec_len',
]
struct_RcimChatroomMemberChangeInfo._fields_ = [
    ('room_id', String),
    ('member_count', c_int32),
    ('action_vec', POINTER(struct_RcimChatroomMemberActionInfo)),
    ('action_vec_len', c_int32),
]

RcimChatroomMemberChangeInfo = struct_RcimChatroomMemberChangeInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3134

RcimChatroomMemberChangedLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimChatroomMemberChangeInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3142

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3177
class struct_RcimChatroomMemberBannedInfo(Structure):
    pass

struct_RcimChatroomMemberBannedInfo.__slots__ = [
    'room_id',
    'event_type',
    'duration_time',
    'operate_time',
    'user_id_vec',
    'user_id_vec_len',
    'extra',
]
struct_RcimChatroomMemberBannedInfo._fields_ = [
    ('room_id', String),
    ('event_type', enum_RcimChatroomMemberBannedEventType),
    ('duration_time', c_int64),
    ('operate_time', c_int64),
    ('user_id_vec', POINTER(POINTER(c_char))),
    ('user_id_vec_len', c_int32),
    ('extra', String),
]

RcimChatroomMemberBannedInfo = struct_RcimChatroomMemberBannedInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3177

RcimChatroomMemberBannedLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimChatroomMemberBannedInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3185

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3217
class struct_RcimChatroomMemberBlockedInfo(Structure):
    pass

struct_RcimChatroomMemberBlockedInfo.__slots__ = [
    'room_id',
    'event_type',
    'duration_time',
    'operate_time',
    'user_id_vec',
    'user_id_vec_len',
    'extra',
]
struct_RcimChatroomMemberBlockedInfo._fields_ = [
    ('room_id', String),
    ('event_type', enum_RcimChatroomMemberBlockedEventType),
    ('duration_time', c_int64),
    ('operate_time', c_int64),
    ('user_id_vec', POINTER(POINTER(c_char))),
    ('user_id_vec_len', c_int32),
    ('extra', String),
]

RcimChatroomMemberBlockedInfo = struct_RcimChatroomMemberBlockedInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3217

RcimChatroomMemberBlockedLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimChatroomMemberBlockedInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3225

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3252
class struct_RcimChatroomMultiClientSyncInfo(Structure):
    pass

struct_RcimChatroomMultiClientSyncInfo.__slots__ = [
    'room_id',
    'event_type',
    'quit_type',
    'time',
    'extra',
]
struct_RcimChatroomMultiClientSyncInfo._fields_ = [
    ('room_id', String),
    ('event_type', enum_RcimChatroomMultiClientSyncEventType),
    ('quit_type', enum_RcimChatroomMultiClientSyncQuitType),
    ('time', c_int64),
    ('extra', String),
]

RcimChatroomMultiClientSyncInfo = struct_RcimChatroomMultiClientSyncInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3252

RcimChatroomMultiClientSyncLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimChatroomMultiClientSyncInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3260

RcimJoinChatroomCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimChatroomJoinedInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3270

RcimJoinExistingChatroomCb = RcimJoinChatroomCb# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3277

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3288
class struct_RcimChatroomUserInfo(Structure):
    pass

struct_RcimChatroomUserInfo.__slots__ = [
    'user_id',
    'join_time',
]
struct_RcimChatroomUserInfo._fields_ = [
    ('user_id', String),
    ('join_time', c_int64),
]

RcimChatroomUserInfo = struct_RcimChatroomUserInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3288

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3314
class struct_RcimChatroomInfo(Structure):
    pass

struct_RcimChatroomInfo.__slots__ = [
    'room_id',
    'total_user_count',
    'join_order',
    'user_info_vec',
    'user_info_vec_len',
]
struct_RcimChatroomInfo._fields_ = [
    ('room_id', String),
    ('total_user_count', c_int32),
    ('join_order', enum_RcimOrder),
    ('user_info_vec', POINTER(struct_RcimChatroomUserInfo)),
    ('user_info_vec_len', c_int32),
]

RcimChatroomInfo = struct_RcimChatroomInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3314

RcimGetChatroomInfoCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimChatroomInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3316

RcimChatroomKvSyncLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), String)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3326

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3340
class struct_RcimChatroomKvInfo(Structure):
    pass

struct_RcimChatroomKvInfo.__slots__ = [
    'key',
    'value',
]
struct_RcimChatroomKvInfo._fields_ = [
    ('key', String),
    ('value', String),
]

RcimChatroomKvInfo = struct_RcimChatroomKvInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3340

RcimChatroomKvChangedLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, POINTER(struct_RcimChatroomKvInfo), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3350

RcimChatroomKvDeleteLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, POINTER(struct_RcimChatroomKvInfo), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3363

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3374
class struct_RcimChatroomKeyErrorInfo(Structure):
    pass

struct_RcimChatroomKeyErrorInfo.__slots__ = [
    'key',
    'error',
]
struct_RcimChatroomKeyErrorInfo._fields_ = [
    ('key', String),
    ('error', enum_RcimEngineError),
]

RcimChatroomKeyErrorInfo = struct_RcimChatroomKeyErrorInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3374

RcimChatroomKvCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimChatroomKeyErrorInfo), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3384

RcimChatroomGetKvCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimChatroomKvInfo), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3397

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3442
class struct_RcimLogInfo(Structure):
    pass

struct_RcimLogInfo.__slots__ = [
    'session_id',
    'log_type',
    'source',
    'level',
    'tag',
    'content',
    'trace_id',
    'create_time',
    'location',
]
struct_RcimLogInfo._fields_ = [
    ('session_id', String),
    ('log_type', enum_RcimLogType),
    ('source', enum_RcimLogSource),
    ('level', enum_RcimLogLevel),
    ('tag', String),
    ('content', String),
    ('trace_id', c_int64),
    ('create_time', c_int64),
    ('location', String),
]

RcimLogInfo = struct_RcimLogInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3442

RcimLogLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimLogInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3450

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3484
class struct_RcimInsertLogInfo(Structure):
    pass

struct_RcimInsertLogInfo.__slots__ = [
    'log_type',
    'source',
    'level',
    'tag',
    'content',
    'trace_id',
    'location',
]
struct_RcimInsertLogInfo._fields_ = [
    ('log_type', enum_RcimLogType),
    ('source', enum_RcimLogSource),
    ('level', enum_RcimLogLevel),
    ('tag', String),
    ('content', String),
    ('trace_id', c_int64),
    ('location', String),
]

RcimInsertLogInfo = struct_RcimInsertLogInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3484

RcimDevLogLsr = CFUNCTYPE(UNCHECKED(None), enum_RcimDevLogLevel, String)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3486

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3491
class struct_RcimPublicServiceMenuItem(Structure):
    pass

struct_RcimPublicServiceMenuItem.__slots__ = [
    'id',
    'name',
    'url',
    'menu_type',
    'sub_menu_vec',
    'sub_menu_vec_len',
]
struct_RcimPublicServiceMenuItem._fields_ = [
    ('id', String),
    ('name', String),
    ('url', String),
    ('menu_type', enum_RcimPublicServiceMenuItemType),
    ('sub_menu_vec', POINTER(struct_RcimPublicServiceMenuItem)),
    ('sub_menu_vec_len', c_int32),
]

RcimPublicServiceMenuItem = struct_RcimPublicServiceMenuItem# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3516

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3559
class struct_RcimPublicServiceInfo(Structure):
    pass

struct_RcimPublicServiceInfo.__slots__ = [
    'target_id',
    'conv_type',
    'name',
    'portrait',
    'introduction',
    'is_followed',
    'menu_vec',
    'menu_vec_len',
    'is_global',
]
struct_RcimPublicServiceInfo._fields_ = [
    ('target_id', String),
    ('conv_type', enum_RcimConversationType),
    ('name', String),
    ('portrait', String),
    ('introduction', String),
    ('is_followed', c_bool),
    ('menu_vec', POINTER(struct_RcimPublicServiceMenuItem)),
    ('menu_vec_len', c_int32),
    ('is_global', c_bool),
]

RcimPublicServiceInfo = struct_RcimPublicServiceInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3559

RcimGetPublicServiceCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimPublicServiceInfo))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3570

RcimGetLocalPublicServiceListCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(struct_RcimPublicServiceInfo), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3582

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3597
class struct_RcimRtcConfig(Structure):
    pass

struct_RcimRtcConfig.__slots__ = [
    'log_server',
    'data_center',
    'jwt_token',
    'open_gzip',
    'voip_call_info',
]
struct_RcimRtcConfig._fields_ = [
    ('log_server', String),
    ('data_center', String),
    ('jwt_token', String),
    ('open_gzip', c_bool),
    ('voip_call_info', String),
]

RcimRtcConfig = struct_RcimRtcConfig# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3597

RcimVoipCallInfoLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimRtcConfig))# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3605

RcimSendRtcSignalingCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, POINTER(uint8_t), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3617

RcimRtcHeartBeatSendLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, c_int64)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3625

RcimRtcHeartBeatResultLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, String, c_int64, c_int64)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3630

RcimRtcRoomEventLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(uint8_t), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3639

RcimRtcSetKVSignalingCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), enum_RcimEngineError, String, String)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3653

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3670
class struct_RcimRtcKvInfo(Structure):
    pass

struct_RcimRtcKvInfo.__slots__ = [
    'key',
    'value',
]
struct_RcimRtcKvInfo._fields_ = [
    ('key', String),
    ('value', String),
]

RcimRtcKvInfo = struct_RcimRtcKvInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3670

RcimRtcKvSignalingLsr = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(struct_RcimRtcKvInfo), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3675

RcimCmpSendCb = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int32)# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3689

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3701
if _libs["librust_universal_imsdk"].has("rcim_create_engine_builder", "cdecl"):
    rcim_create_engine_builder = _libs["librust_universal_imsdk"].get("rcim_create_engine_builder", "cdecl")
    rcim_create_engine_builder.argtypes = [POINTER(struct_RcimEngineBuilderParam), POINTER(POINTER(struct_RcimEngineBuilder))]
    rcim_create_engine_builder.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3713
if _libs["librust_universal_imsdk"].has("rcim_destroy_engine_builder", "cdecl"):
    rcim_destroy_engine_builder = _libs["librust_universal_imsdk"].get("rcim_destroy_engine_builder", "cdecl")
    rcim_destroy_engine_builder.argtypes = [POINTER(struct_RcimEngineBuilder)]
    rcim_destroy_engine_builder.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3732
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_set_cloud_type", "cdecl"):
    rcim_engine_builder_set_cloud_type = _libs["librust_universal_imsdk"].get("rcim_engine_builder_set_cloud_type", "cdecl")
    rcim_engine_builder_set_cloud_type.argtypes = [POINTER(struct_RcimEngineBuilder), enum_RcimCloudType]
    rcim_engine_builder_set_cloud_type.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3747
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_set_db_encrypted", "cdecl"):
    rcim_engine_builder_set_db_encrypted = _libs["librust_universal_imsdk"].get("rcim_engine_builder_set_db_encrypted", "cdecl")
    rcim_engine_builder_set_db_encrypted.argtypes = [POINTER(struct_RcimEngineBuilder), c_bool]
    rcim_engine_builder_set_db_encrypted.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3762
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_set_enable_group_call", "cdecl"):
    rcim_engine_builder_set_enable_group_call = _libs["librust_universal_imsdk"].get("rcim_engine_builder_set_enable_group_call", "cdecl")
    rcim_engine_builder_set_enable_group_call.argtypes = [POINTER(struct_RcimEngineBuilder), c_bool]
    rcim_engine_builder_set_enable_group_call.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3779
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_set_enable_reconnect_kick", "cdecl"):
    rcim_engine_builder_set_enable_reconnect_kick = _libs["librust_universal_imsdk"].get("rcim_engine_builder_set_enable_reconnect_kick", "cdecl")
    rcim_engine_builder_set_enable_reconnect_kick.argtypes = [POINTER(struct_RcimEngineBuilder), c_bool]
    rcim_engine_builder_set_enable_reconnect_kick.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3794
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_set_store_path", "cdecl"):
    rcim_engine_builder_set_store_path = _libs["librust_universal_imsdk"].get("rcim_engine_builder_set_store_path", "cdecl")
    rcim_engine_builder_set_store_path.argtypes = [POINTER(struct_RcimEngineBuilder), String]
    rcim_engine_builder_set_store_path.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3810
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_set_network_env", "cdecl"):
    rcim_engine_builder_set_network_env = _libs["librust_universal_imsdk"].get("rcim_engine_builder_set_network_env", "cdecl")
    rcim_engine_builder_set_network_env.argtypes = [POINTER(struct_RcimEngineBuilder), String]
    rcim_engine_builder_set_network_env.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3825
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_set_file_path", "cdecl"):
    rcim_engine_builder_set_file_path = _libs["librust_universal_imsdk"].get("rcim_engine_builder_set_file_path", "cdecl")
    rcim_engine_builder_set_file_path.argtypes = [POINTER(struct_RcimEngineBuilder), String]
    rcim_engine_builder_set_file_path.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3847
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_set_navi_server", "cdecl"):
    rcim_engine_builder_set_navi_server = _libs["librust_universal_imsdk"].get("rcim_engine_builder_set_navi_server", "cdecl")
    rcim_engine_builder_set_navi_server.argtypes = [POINTER(struct_RcimEngineBuilder), POINTER(POINTER(c_char)), c_int32]
    rcim_engine_builder_set_navi_server.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3863
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_set_statistic_server", "cdecl"):
    rcim_engine_builder_set_statistic_server = _libs["librust_universal_imsdk"].get("rcim_engine_builder_set_statistic_server", "cdecl")
    rcim_engine_builder_set_statistic_server.argtypes = [POINTER(struct_RcimEngineBuilder), String]
    rcim_engine_builder_set_statistic_server.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3878
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_set_area_code", "cdecl"):
    rcim_engine_builder_set_area_code = _libs["librust_universal_imsdk"].get("rcim_engine_builder_set_area_code", "cdecl")
    rcim_engine_builder_set_area_code.argtypes = [POINTER(struct_RcimEngineBuilder), enum_RcimAreaCode]
    rcim_engine_builder_set_area_code.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3891
if _libs["librust_universal_imsdk"].has("rcim_engine_builder_build", "cdecl"):
    rcim_engine_builder_build = _libs["librust_universal_imsdk"].get("rcim_engine_builder_build", "cdecl")
    rcim_engine_builder_build.argtypes = [POINTER(struct_RcimEngineBuilder), POINTER(POINTER(struct_RcimEngineSync))]
    rcim_engine_builder_build.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3902
if _libs["librust_universal_imsdk"].has("rcim_destroy_engine", "cdecl"):
    rcim_destroy_engine = _libs["librust_universal_imsdk"].get("rcim_destroy_engine", "cdecl")
    rcim_destroy_engine.argtypes = [POINTER(struct_RcimEngineSync)]
    rcim_destroy_engine.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3915
if _libs["librust_universal_imsdk"].has("rcim_engine_set_database_status_listener", "cdecl"):
    rcim_engine_set_database_status_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_database_status_listener", "cdecl")
    rcim_engine_set_database_status_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimDatabaseStatusLsr]
    rcim_engine_set_database_status_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3930
if _libs["librust_universal_imsdk"].has("rcim_engine_get_sdk_version", "cdecl"):
    rcim_engine_get_sdk_version = _libs["librust_universal_imsdk"].get("rcim_engine_get_sdk_version", "cdecl")
    rcim_engine_get_sdk_version.argtypes = [POINTER(struct_RcimEngineSync), POINTER(POINTER(c_char))]
    rcim_engine_get_sdk_version.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3943
if _libs["librust_universal_imsdk"].has("rcim_engine_set_device_id", "cdecl"):
    rcim_engine_set_device_id = _libs["librust_universal_imsdk"].get("rcim_engine_set_device_id", "cdecl")
    rcim_engine_set_device_id.argtypes = [POINTER(struct_RcimEngineSync), String]
    rcim_engine_set_device_id.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3960
if _libs["librust_universal_imsdk"].has("rcim_engine_set_push_token", "cdecl"):
    rcim_engine_set_push_token = _libs["librust_universal_imsdk"].get("rcim_engine_set_push_token", "cdecl")
    rcim_engine_set_push_token.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimPushTokenInfo), c_int32]
    rcim_engine_set_push_token.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3975
if _libs["librust_universal_imsdk"].has("rcim_engine_get_delta_time", "cdecl"):
    rcim_engine_get_delta_time = _libs["librust_universal_imsdk"].get("rcim_engine_get_delta_time", "cdecl")
    rcim_engine_get_delta_time.argtypes = [POINTER(struct_RcimEngineSync), POINTER(c_int64)]
    rcim_engine_get_delta_time.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3988
if _libs["librust_universal_imsdk"].has("rcim_engine_get_user_id", "cdecl"):
    rcim_engine_get_user_id = _libs["librust_universal_imsdk"].get("rcim_engine_get_user_id", "cdecl")
    rcim_engine_get_user_id.argtypes = [POINTER(struct_RcimEngineSync), POINTER(POINTER(c_char))]
    rcim_engine_get_user_id.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4002
if _libs["librust_universal_imsdk"].has("rcim_engine_set_connection_status_listener", "cdecl"):
    rcim_engine_set_connection_status_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_connection_status_listener", "cdecl")
    rcim_engine_set_connection_status_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimConnectionStatusLsr]
    rcim_engine_set_connection_status_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4016
if _libs["librust_universal_imsdk"].has("rcim_engine_get_connection_status", "cdecl"):
    rcim_engine_get_connection_status = _libs["librust_universal_imsdk"].get("rcim_engine_get_connection_status", "cdecl")
    rcim_engine_get_connection_status.argtypes = [POINTER(struct_RcimEngineSync), POINTER(enum_RcimConnectionStatus)]
    rcim_engine_get_connection_status.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4037
if _libs["librust_universal_imsdk"].has("rcim_engine_connect", "cdecl"):
    rcim_engine_connect = _libs["librust_universal_imsdk"].get("rcim_engine_connect", "cdecl")
    rcim_engine_connect.argtypes = [POINTER(struct_RcimEngineSync), String, c_int32, POINTER(None), RcimConnectCb]
    rcim_engine_connect.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4054
if _libs["librust_universal_imsdk"].has("rcim_engine_disconnect", "cdecl"):
    rcim_engine_disconnect = _libs["librust_universal_imsdk"].get("rcim_engine_disconnect", "cdecl")
    rcim_engine_disconnect.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimDisconnectMode, POINTER(None), RcimEngineErrorCb]
    rcim_engine_disconnect.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4069
if _libs["librust_universal_imsdk"].has("rcim_engine_notify_app_state_changed", "cdecl"):
    rcim_engine_notify_app_state_changed = _libs["librust_universal_imsdk"].get("rcim_engine_notify_app_state_changed", "cdecl")
    rcim_engine_notify_app_state_changed.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimAppState]
    rcim_engine_notify_app_state_changed.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4082
if _libs["librust_universal_imsdk"].has("rcim_engine_notify_network_changed", "cdecl"):
    rcim_engine_notify_network_changed = _libs["librust_universal_imsdk"].get("rcim_engine_notify_network_changed", "cdecl")
    rcim_engine_notify_network_changed.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimNetworkType]
    rcim_engine_notify_network_changed.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4098
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_received_listener", "cdecl"):
    rcim_engine_set_message_received_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_received_listener", "cdecl")
    rcim_engine_set_message_received_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimMessageReceivedLsr]
    rcim_engine_set_message_received_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4112
if _libs["librust_universal_imsdk"].has("rcim_engine_set_offline_message_sync_completed_listener", "cdecl"):
    rcim_engine_set_offline_message_sync_completed_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_offline_message_sync_completed_listener", "cdecl")
    rcim_engine_set_offline_message_sync_completed_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimOfflineMessageSyncCompletedLsr]
    rcim_engine_set_offline_message_sync_completed_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4128
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_searchable_words_callback_listener", "cdecl"):
    rcim_engine_set_message_searchable_words_callback_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_searchable_words_callback_listener", "cdecl")
    rcim_engine_set_message_searchable_words_callback_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimMessageSearchableWordsCbLsr]
    rcim_engine_set_message_searchable_words_callback_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4144
if _libs["librust_universal_imsdk"].has("rcim_engine_set_sight_compress_callback_listener", "cdecl"):
    rcim_engine_set_sight_compress_callback_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_sight_compress_callback_listener", "cdecl")
    rcim_engine_set_sight_compress_callback_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimSightCompressCbLsr]
    rcim_engine_set_sight_compress_callback_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4159
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_recalled_listener", "cdecl"):
    rcim_engine_set_message_recalled_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_recalled_listener", "cdecl")
    rcim_engine_set_message_recalled_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimRecallMessageLsr]
    rcim_engine_set_message_recalled_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4174
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_blocked_listener", "cdecl"):
    rcim_engine_set_message_blocked_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_blocked_listener", "cdecl")
    rcim_engine_set_message_blocked_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimMessageBlockedLsr]
    rcim_engine_set_message_blocked_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4197
if _libs["librust_universal_imsdk"].has("rcim_engine_send_message", "cdecl"):
    rcim_engine_send_message = _libs["librust_universal_imsdk"].get("rcim_engine_send_message", "cdecl")
    rcim_engine_send_message.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimMessageBox), POINTER(struct_RcimSendMessageOption), POINTER(None), RcimCodeMessageCb, RcimMessageCb]
    rcim_engine_send_message.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4218
if _libs["librust_universal_imsdk"].has("rcim_engine_send_read_receipt_message", "cdecl"):
    rcim_engine_send_read_receipt_message = _libs["librust_universal_imsdk"].get("rcim_engine_send_read_receipt_message", "cdecl")
    rcim_engine_send_read_receipt_message.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, c_int64, POINTER(None), RcimCodeMessageCb]
    rcim_engine_send_read_receipt_message.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4237
if _libs["librust_universal_imsdk"].has("rcim_engine_send_read_receipt_request", "cdecl"):
    rcim_engine_send_read_receipt_request = _libs["librust_universal_imsdk"].get("rcim_engine_send_read_receipt_request", "cdecl")
    rcim_engine_send_read_receipt_request.argtypes = [POINTER(struct_RcimEngineSync), String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_send_read_receipt_request.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4257
if _libs["librust_universal_imsdk"].has("rcim_engine_send_read_receipt_response", "cdecl"):
    rcim_engine_send_read_receipt_response = _libs["librust_universal_imsdk"].get("rcim_engine_send_read_receipt_response", "cdecl")
    rcim_engine_send_read_receipt_response.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(struct_RcimSendReadReceiptResponseMessageData), c_int32, POINTER(None), RcimGetMessageListCb]
    rcim_engine_send_read_receipt_response.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4277
if _libs["librust_universal_imsdk"].has("rcim_engine_set_read_receipt_received_listener", "cdecl"):
    rcim_engine_set_read_receipt_received_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_read_receipt_received_listener", "cdecl")
    rcim_engine_set_read_receipt_received_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimMessageNotifyLsr]
    rcim_engine_set_read_receipt_received_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4292
if _libs["librust_universal_imsdk"].has("rcim_engine_set_read_receipt_request_listener", "cdecl"):
    rcim_engine_set_read_receipt_request_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_read_receipt_request_listener", "cdecl")
    rcim_engine_set_read_receipt_request_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimReadReceiptRequestLsr]
    rcim_engine_set_read_receipt_request_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4307
if _libs["librust_universal_imsdk"].has("rcim_engine_set_read_receipt_response_listener", "cdecl"):
    rcim_engine_set_read_receipt_response_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_read_receipt_response_listener", "cdecl")
    rcim_engine_set_read_receipt_response_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimReadReceiptResponseLsr]
    rcim_engine_set_read_receipt_response_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4326
if _libs["librust_universal_imsdk"].has("rcim_engine_send_read_receipt_response_v2", "cdecl"):
    rcim_engine_send_read_receipt_response_v2 = _libs["librust_universal_imsdk"].get("rcim_engine_send_read_receipt_response_v2", "cdecl")
    rcim_engine_send_read_receipt_response_v2.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(POINTER(c_char)), c_int32, POINTER(None), RcimGetMessageListCb]
    rcim_engine_send_read_receipt_response_v2.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4349
if _libs["librust_universal_imsdk"].has("rcim_engine_get_read_receipt_v2_readers", "cdecl"):
    rcim_engine_get_read_receipt_v2_readers = _libs["librust_universal_imsdk"].get("rcim_engine_get_read_receipt_v2_readers", "cdecl")
    rcim_engine_get_read_receipt_v2_readers.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, String, POINTER(None), RcimGetReadReceiptV2ReaderListCb]
    rcim_engine_get_read_receipt_v2_readers.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4369
if _libs["librust_universal_imsdk"].has("rcim_engine_set_read_receipt_response_v2_listener", "cdecl"):
    rcim_engine_set_read_receipt_response_v2_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_read_receipt_response_v2_listener", "cdecl")
    rcim_engine_set_read_receipt_response_v2_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimReadReceiptResponseV2Lsr]
    rcim_engine_set_read_receipt_response_v2_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4385
if _libs["librust_universal_imsdk"].has("rcim_engine_cancel_send_media_message", "cdecl"):
    rcim_engine_cancel_send_media_message = _libs["librust_universal_imsdk"].get("rcim_engine_cancel_send_media_message", "cdecl")
    rcim_engine_cancel_send_media_message.argtypes = [POINTER(struct_RcimEngineSync), c_int64, POINTER(None), RcimEngineErrorCb]
    rcim_engine_cancel_send_media_message.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4412
if _libs["librust_universal_imsdk"].has("rcim_engine_send_media_message", "cdecl"):
    rcim_engine_send_media_message = _libs["librust_universal_imsdk"].get("rcim_engine_send_media_message", "cdecl")
    rcim_engine_send_media_message.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimMessageBox), POINTER(struct_RcimSendMessageOption), POINTER(None), RcimCodeMessageCb, RcimMessageCb, RcimSendMessageOnProgressCb, RcimMediaMessageHandlerCb]
    rcim_engine_send_media_message.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4435
if _libs["librust_universal_imsdk"].has("rcim_engine_download_media_message", "cdecl"):
    rcim_engine_download_media_message = _libs["librust_universal_imsdk"].get("rcim_engine_download_media_message", "cdecl")
    rcim_engine_download_media_message.argtypes = [POINTER(struct_RcimEngineSync), c_int64, POINTER(None), RcimDownloadMediaCb, RcimDownloadMessageProgressCb, RcimMediaMessageHandlerCb]
    rcim_engine_download_media_message.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4455
if _libs["librust_universal_imsdk"].has("rcim_engine_cancel_download_media_message", "cdecl"):
    rcim_engine_cancel_download_media_message = _libs["librust_universal_imsdk"].get("rcim_engine_cancel_download_media_message", "cdecl")
    rcim_engine_cancel_download_media_message.argtypes = [POINTER(struct_RcimEngineSync), c_int64, POINTER(None), RcimEngineErrorCb]
    rcim_engine_cancel_download_media_message.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4473
if _libs["librust_universal_imsdk"].has("rcim_engine_pause_download_media_message", "cdecl"):
    rcim_engine_pause_download_media_message = _libs["librust_universal_imsdk"].get("rcim_engine_pause_download_media_message", "cdecl")
    rcim_engine_pause_download_media_message.argtypes = [POINTER(struct_RcimEngineSync), c_int64, POINTER(None), RcimEngineErrorCb]
    rcim_engine_pause_download_media_message.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4497
if _libs["librust_universal_imsdk"].has("rcim_engine_download_file_with_progress", "cdecl"):
    rcim_engine_download_file_with_progress = _libs["librust_universal_imsdk"].get("rcim_engine_download_file_with_progress", "cdecl")
    rcim_engine_download_file_with_progress.argtypes = [POINTER(struct_RcimEngineSync), String, String, POINTER(POINTER(c_char)), POINTER(None), RcimDownloadMediaCb, RcimDownloadFileProgressCb]
    rcim_engine_download_file_with_progress.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4523
if _libs["librust_universal_imsdk"].has("rcim_engine_download_file_with_unique_id", "cdecl"):
    rcim_engine_download_file_with_unique_id = _libs["librust_universal_imsdk"].get("rcim_engine_download_file_with_unique_id", "cdecl")
    rcim_engine_download_file_with_unique_id.argtypes = [POINTER(struct_RcimEngineSync), String, String, String, POINTER(None), RcimDownloadMediaCb, RcimDownloadFileProgressCb]
    rcim_engine_download_file_with_unique_id.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4544
if _libs["librust_universal_imsdk"].has("rcim_engine_cancel_download_file", "cdecl"):
    rcim_engine_cancel_download_file = _libs["librust_universal_imsdk"].get("rcim_engine_cancel_download_file", "cdecl")
    rcim_engine_cancel_download_file.argtypes = [POINTER(struct_RcimEngineSync), String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_cancel_download_file.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4562
if _libs["librust_universal_imsdk"].has("rcim_engine_pause_download_file", "cdecl"):
    rcim_engine_pause_download_file = _libs["librust_universal_imsdk"].get("rcim_engine_pause_download_file", "cdecl")
    rcim_engine_pause_download_file.argtypes = [POINTER(struct_RcimEngineSync), String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_pause_download_file.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4591
if _libs["librust_universal_imsdk"].has("rcim_engine_recall_message", "cdecl"):
    rcim_engine_recall_message = _libs["librust_universal_imsdk"].get("rcim_engine_recall_message", "cdecl")
    rcim_engine_recall_message.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimMessageBox), POINTER(None), RcimRecallMessageCb]
    rcim_engine_recall_message.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4607
if _libs["librust_universal_imsdk"].has("rcim_engine_register_message_types", "cdecl"):
    rcim_engine_register_message_types = _libs["librust_universal_imsdk"].get("rcim_engine_register_message_types", "cdecl")
    rcim_engine_register_message_types.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimMessageType), c_int32]
    rcim_engine_register_message_types.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4622
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_message_by_uid", "cdecl"):
    rcim_engine_get_local_message_by_uid = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_message_by_uid", "cdecl")
    rcim_engine_get_local_message_by_uid.argtypes = [POINTER(struct_RcimEngineSync), String, POINTER(None), RcimCodeMessageCb]
    rcim_engine_get_local_message_by_uid.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4640
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_message_by_id", "cdecl"):
    rcim_engine_get_local_message_by_id = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_message_by_id", "cdecl")
    rcim_engine_get_local_message_by_id.argtypes = [POINTER(struct_RcimEngineSync), c_int64, POINTER(None), RcimCodeMessageCb]
    rcim_engine_get_local_message_by_id.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4663
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_history_messages_by_time", "cdecl"):
    rcim_engine_get_local_history_messages_by_time = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_history_messages_by_time", "cdecl")
    rcim_engine_get_local_history_messages_by_time.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(POINTER(c_char)), c_int32, c_int64, c_int32, c_int32, POINTER(None), RcimGetMessageListCb]
    rcim_engine_get_local_history_messages_by_time.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4697
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_history_messages_by_senders", "cdecl"):
    rcim_engine_get_local_history_messages_by_senders = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_history_messages_by_senders", "cdecl")
    rcim_engine_get_local_history_messages_by_senders.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(POINTER(c_char)), c_int32, POINTER(POINTER(c_char)), c_int32, c_int32, c_int64, enum_RcimOrder, POINTER(None), RcimGetMessageListCb]
    rcim_engine_get_local_history_messages_by_senders.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4729
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_history_messages_by_id", "cdecl"):
    rcim_engine_get_local_history_messages_by_id = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_history_messages_by_id", "cdecl")
    rcim_engine_get_local_history_messages_by_id.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(POINTER(c_char)), c_int32, c_int64, c_int32, c_int32, POINTER(None), RcimGetMessageListCb]
    rcim_engine_get_local_history_messages_by_id.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4760
if _libs["librust_universal_imsdk"].has("rcim_engine_get_remote_history_messages", "cdecl"):
    rcim_engine_get_remote_history_messages = _libs["librust_universal_imsdk"].get("rcim_engine_get_remote_history_messages", "cdecl")
    rcim_engine_get_remote_history_messages.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, c_int64, c_int32, enum_RcimOrder, c_bool, POINTER(None), RcimGetMessageListCb]
    rcim_engine_get_remote_history_messages.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4785
if _libs["librust_universal_imsdk"].has("rcim_engine_clean_local_history_messages", "cdecl"):
    rcim_engine_clean_local_history_messages = _libs["librust_universal_imsdk"].get("rcim_engine_clean_local_history_messages", "cdecl")
    rcim_engine_clean_local_history_messages.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, c_int64, POINTER(None), RcimEngineErrorCb]
    rcim_engine_clean_local_history_messages.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4808
if _libs["librust_universal_imsdk"].has("rcim_engine_clean_remote_history_messages", "cdecl"):
    rcim_engine_clean_remote_history_messages = _libs["librust_universal_imsdk"].get("rcim_engine_clean_remote_history_messages", "cdecl")
    rcim_engine_clean_remote_history_messages.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, c_int64, POINTER(None), RcimEngineErrorCb]
    rcim_engine_clean_remote_history_messages.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4844
if _libs["librust_universal_imsdk"].has("rcim_engine_insert_local_messages", "cdecl"):
    rcim_engine_insert_local_messages = _libs["librust_universal_imsdk"].get("rcim_engine_insert_local_messages", "cdecl")
    rcim_engine_insert_local_messages.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimMessageBox), c_int32, POINTER(None), RcimEngineErrorCb]
    rcim_engine_insert_local_messages.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4877
if _libs["librust_universal_imsdk"].has("rcim_engine_insert_local_message", "cdecl"):
    rcim_engine_insert_local_message = _libs["librust_universal_imsdk"].get("rcim_engine_insert_local_message", "cdecl")
    rcim_engine_insert_local_message.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimMessageBox), POINTER(None), RcimCodeMessageCb]
    rcim_engine_insert_local_message.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4895
if _libs["librust_universal_imsdk"].has("rcim_engine_delete_local_messages", "cdecl"):
    rcim_engine_delete_local_messages = _libs["librust_universal_imsdk"].get("rcim_engine_delete_local_messages", "cdecl")
    rcim_engine_delete_local_messages.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_delete_local_messages.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4914
if _libs["librust_universal_imsdk"].has("rcim_engine_delete_local_messages_by_ids", "cdecl"):
    rcim_engine_delete_local_messages_by_ids = _libs["librust_universal_imsdk"].get("rcim_engine_delete_local_messages_by_ids", "cdecl")
    rcim_engine_delete_local_messages_by_ids.argtypes = [POINTER(struct_RcimEngineSync), POINTER(c_int64), c_int32, POINTER(None), RcimEngineErrorCb]
    rcim_engine_delete_local_messages_by_ids.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4948
if _libs["librust_universal_imsdk"].has("rcim_engine_delete_remote_messages", "cdecl"):
    rcim_engine_delete_remote_messages = _libs["librust_universal_imsdk"].get("rcim_engine_delete_remote_messages", "cdecl")
    rcim_engine_delete_remote_messages.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(struct_RcimMessageBox), c_int32, c_bool, POINTER(None), RcimEngineErrorCb]
    rcim_engine_delete_remote_messages.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 4974
if _libs["librust_universal_imsdk"].has("rcim_engine_search_local_messages", "cdecl"):
    rcim_engine_search_local_messages = _libs["librust_universal_imsdk"].get("rcim_engine_search_local_messages", "cdecl")
    rcim_engine_search_local_messages.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, String, c_int32, c_int64, POINTER(None), RcimGetMessageListCb]
    rcim_engine_search_local_messages.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5002
if _libs["librust_universal_imsdk"].has("rcim_engine_search_local_messages_by_object_name", "cdecl"):
    rcim_engine_search_local_messages_by_object_name = _libs["librust_universal_imsdk"].get("rcim_engine_search_local_messages_by_object_name", "cdecl")
    rcim_engine_search_local_messages_by_object_name.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, String, POINTER(POINTER(c_char)), c_int32, c_int32, c_int64, POINTER(None), RcimGetMessageListCb]
    rcim_engine_search_local_messages_by_object_name.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5032
if _libs["librust_universal_imsdk"].has("rcim_engine_search_local_messages_by_time", "cdecl"):
    rcim_engine_search_local_messages_by_time = _libs["librust_universal_imsdk"].get("rcim_engine_search_local_messages_by_time", "cdecl")
    rcim_engine_search_local_messages_by_time.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, String, c_int32, c_int64, c_int64, c_int64, POINTER(None), RcimGetMessageListCb]
    rcim_engine_search_local_messages_by_time.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5060
if _libs["librust_universal_imsdk"].has("rcim_engine_search_local_messages_by_user_id", "cdecl"):
    rcim_engine_search_local_messages_by_user_id = _libs["librust_universal_imsdk"].get("rcim_engine_search_local_messages_by_user_id", "cdecl")
    rcim_engine_search_local_messages_by_user_id.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, String, c_int32, c_int64, POINTER(None), RcimGetMessageListCb]
    rcim_engine_search_local_messages_by_user_id.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5095
if _libs["librust_universal_imsdk"].has("rcim_engine_search_local_messages_by_multiple_conversations", "cdecl"):
    rcim_engine_search_local_messages_by_multiple_conversations = _libs["librust_universal_imsdk"].get("rcim_engine_search_local_messages_by_multiple_conversations", "cdecl")
    rcim_engine_search_local_messages_by_multiple_conversations.argtypes = [POINTER(struct_RcimEngineSync), POINTER(enum_RcimConversationType), c_int32, POINTER(POINTER(c_char)), c_int32, POINTER(POINTER(c_char)), c_int32, POINTER(POINTER(c_char)), c_int32, String, c_int32, c_int64, enum_RcimOrder, POINTER(None), RcimGetMessageListCb]
    rcim_engine_search_local_messages_by_multiple_conversations.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5122
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_expansion_update_listener", "cdecl"):
    rcim_engine_set_message_expansion_update_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_expansion_update_listener", "cdecl")
    rcim_engine_set_message_expansion_update_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimMessageExpansionKvUpdateLsr]
    rcim_engine_set_message_expansion_update_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5137
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_expansion_remove_listener", "cdecl"):
    rcim_engine_set_message_expansion_remove_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_expansion_remove_listener", "cdecl")
    rcim_engine_set_message_expansion_remove_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimMessageExpansionKvRemoveLsr]
    rcim_engine_set_message_expansion_remove_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5154
if _libs["librust_universal_imsdk"].has("rcim_engine_update_message_expansion", "cdecl"):
    rcim_engine_update_message_expansion = _libs["librust_universal_imsdk"].get("rcim_engine_update_message_expansion", "cdecl")
    rcim_engine_update_message_expansion.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimMessageExpansionKvInfo), c_int32, String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_update_message_expansion.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5174
if _libs["librust_universal_imsdk"].has("rcim_engine_remove_message_expansion", "cdecl"):
    rcim_engine_remove_message_expansion = _libs["librust_universal_imsdk"].get("rcim_engine_remove_message_expansion", "cdecl")
    rcim_engine_remove_message_expansion.argtypes = [POINTER(struct_RcimEngineSync), POINTER(POINTER(c_char)), c_int32, String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_remove_message_expansion.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5195
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_sent_status", "cdecl"):
    rcim_engine_set_message_sent_status = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_sent_status", "cdecl")
    rcim_engine_set_message_sent_status.argtypes = [POINTER(struct_RcimEngineSync), c_int64, enum_RcimSentStatus, POINTER(None), RcimEngineErrorCb]
    rcim_engine_set_message_sent_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5213
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_received_status", "cdecl"):
    rcim_engine_set_message_received_status = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_received_status", "cdecl")
    rcim_engine_set_message_received_status.argtypes = [POINTER(struct_RcimEngineSync), c_int64, POINTER(struct_RcimReceivedStatus), POINTER(None), RcimEngineErrorCb]
    rcim_engine_set_message_received_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5235
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_content", "cdecl"):
    rcim_engine_set_message_content = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_content", "cdecl")
    rcim_engine_set_message_content.argtypes = [POINTER(struct_RcimEngineSync), c_int64, String, String, String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_set_message_content.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5255
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_extra", "cdecl"):
    rcim_engine_set_message_extra = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_extra", "cdecl")
    rcim_engine_set_message_extra.argtypes = [POINTER(struct_RcimEngineSync), c_int64, String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_set_message_extra.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5278
if _libs["librust_universal_imsdk"].has("rcim_engine_set_push_content_show_status", "cdecl"):
    rcim_engine_set_push_content_show_status = _libs["librust_universal_imsdk"].get("rcim_engine_set_push_content_show_status", "cdecl")
    rcim_engine_set_push_content_show_status.argtypes = [POINTER(struct_RcimEngineSync), c_bool, POINTER(None), RcimEngineErrorCb]
    rcim_engine_set_push_content_show_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5293
if _libs["librust_universal_imsdk"].has("rcim_engine_get_push_content_show_status", "cdecl"):
    rcim_engine_get_push_content_show_status = _libs["librust_universal_imsdk"].get("rcim_engine_get_push_content_show_status", "cdecl")
    rcim_engine_get_push_content_show_status.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimGetBoolCb]
    rcim_engine_get_push_content_show_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5312
if _libs["librust_universal_imsdk"].has("rcim_engine_set_push_receive_status", "cdecl"):
    rcim_engine_set_push_receive_status = _libs["librust_universal_imsdk"].get("rcim_engine_set_push_receive_status", "cdecl")
    rcim_engine_set_push_receive_status.argtypes = [POINTER(struct_RcimEngineSync), c_bool, POINTER(None), RcimEngineErrorCb]
    rcim_engine_set_push_receive_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5327
if _libs["librust_universal_imsdk"].has("rcim_engine_get_push_receive_status", "cdecl"):
    rcim_engine_get_push_receive_status = _libs["librust_universal_imsdk"].get("rcim_engine_get_push_receive_status", "cdecl")
    rcim_engine_get_push_receive_status.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimGetBoolCb]
    rcim_engine_get_push_receive_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5342
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_destructing_listener", "cdecl"):
    rcim_engine_set_message_destructing_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_destructing_listener", "cdecl")
    rcim_engine_set_message_destructing_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimMessageDestructingLsr]
    rcim_engine_set_message_destructing_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5357
if _libs["librust_universal_imsdk"].has("rcim_engine_set_message_destruction_stop_listener", "cdecl"):
    rcim_engine_set_message_destruction_stop_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_message_destruction_stop_listener", "cdecl")
    rcim_engine_set_message_destruction_stop_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimMessageDestructionStopLsr]
    rcim_engine_set_message_destruction_stop_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5374
if _libs["librust_universal_imsdk"].has("rcim_engine_message_begin_destruct", "cdecl"):
    rcim_engine_message_begin_destruct = _libs["librust_universal_imsdk"].get("rcim_engine_message_begin_destruct", "cdecl")
    rcim_engine_message_begin_destruct.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimMessageBox), POINTER(None), RcimEngineErrorCb]
    rcim_engine_message_begin_destruct.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5397
if _libs["librust_universal_imsdk"].has("rcim_engine_message_stop_destruct", "cdecl"):
    rcim_engine_message_stop_destruct = _libs["librust_universal_imsdk"].get("rcim_engine_message_stop_destruct", "cdecl")
    rcim_engine_message_stop_destruct.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimMessageBox), POINTER(None), RcimEngineErrorCb]
    rcim_engine_message_stop_destruct.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5413
if _libs["librust_universal_imsdk"].has("rcim_engine_set_conversation_status_listener", "cdecl"):
    rcim_engine_set_conversation_status_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_conversation_status_listener", "cdecl")
    rcim_engine_set_conversation_status_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimConversationStatusLsr]
    rcim_engine_set_conversation_status_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5426
if _libs["librust_universal_imsdk"].has("rcim_engine_set_typing_status_listener", "cdecl"):
    rcim_engine_set_typing_status_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_typing_status_listener", "cdecl")
    rcim_engine_set_typing_status_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimTypingStatusLsr]
    rcim_engine_set_typing_status_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5442
if _libs["librust_universal_imsdk"].has("rcim_engine_send_typing_status", "cdecl"):
    rcim_engine_send_typing_status = _libs["librust_universal_imsdk"].get("rcim_engine_send_typing_status", "cdecl")
    rcim_engine_send_typing_status.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_send_typing_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5460
if _libs["librust_universal_imsdk"].has("rcim_engine_set_typing_status_interval", "cdecl"):
    rcim_engine_set_typing_status_interval = _libs["librust_universal_imsdk"].get("rcim_engine_set_typing_status_interval", "cdecl")
    rcim_engine_set_typing_status_interval.argtypes = [POINTER(struct_RcimEngineSync), c_int32, POINTER(None), RcimEngineErrorCb]
    rcim_engine_set_typing_status_interval.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5477
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_conversation", "cdecl"):
    rcim_engine_get_local_conversation = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_conversation", "cdecl")
    rcim_engine_get_local_conversation.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(None), RcimGetConversationCb]
    rcim_engine_get_local_conversation.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5498
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_conversations_by_page", "cdecl"):
    rcim_engine_get_local_conversations_by_page = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_conversations_by_page", "cdecl")
    rcim_engine_get_local_conversations_by_page.argtypes = [POINTER(struct_RcimEngineSync), POINTER(enum_RcimConversationType), c_int32, c_int64, c_int32, POINTER(None), RcimGetConversationListCb]
    rcim_engine_get_local_conversations_by_page.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5521
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_pin_conversations_by_page", "cdecl"):
    rcim_engine_get_local_pin_conversations_by_page = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_pin_conversations_by_page", "cdecl")
    rcim_engine_get_local_pin_conversations_by_page.argtypes = [POINTER(struct_RcimEngineSync), POINTER(enum_RcimConversationType), c_int32, c_int64, c_int32, c_bool, POINTER(None), RcimGetConversationListCb]
    rcim_engine_get_local_pin_conversations_by_page.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5546
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_muted_conversations_by_page", "cdecl"):
    rcim_engine_get_local_muted_conversations_by_page = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_muted_conversations_by_page", "cdecl")
    rcim_engine_get_local_muted_conversations_by_page.argtypes = [POINTER(struct_RcimEngineSync), POINTER(enum_RcimConversationType), c_int32, c_int64, c_int32, POINTER(enum_RcimPushNotificationMuteLevel), c_int32, POINTER(None), RcimGetConversationListCb]
    rcim_engine_get_local_muted_conversations_by_page.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5568
if _libs["librust_universal_imsdk"].has("rcim_engine_clear_local_conversations", "cdecl"):
    rcim_engine_clear_local_conversations = _libs["librust_universal_imsdk"].get("rcim_engine_clear_local_conversations", "cdecl")
    rcim_engine_clear_local_conversations.argtypes = [POINTER(struct_RcimEngineSync), POINTER(enum_RcimConversationType), c_int32, POINTER(None), RcimEngineErrorCb]
    rcim_engine_clear_local_conversations.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5586
if _libs["librust_universal_imsdk"].has("rcim_engine_remove_conversations", "cdecl"):
    rcim_engine_remove_conversations = _libs["librust_universal_imsdk"].get("rcim_engine_remove_conversations", "cdecl")
    rcim_engine_remove_conversations.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimConversationIdentifier), c_int32, POINTER(None), RcimEngineErrorCb]
    rcim_engine_remove_conversations.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5607
if _libs["librust_universal_imsdk"].has("rcim_engine_pin_conversations", "cdecl"):
    rcim_engine_pin_conversations = _libs["librust_universal_imsdk"].get("rcim_engine_pin_conversations", "cdecl")
    rcim_engine_pin_conversations.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimConversationIdentifier), c_int32, c_bool, c_bool, c_bool, POINTER(None), RcimEngineErrorCb]
    rcim_engine_pin_conversations.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5629
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_conversation_pin_status", "cdecl"):
    rcim_engine_get_local_conversation_pin_status = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_conversation_pin_status", "cdecl")
    rcim_engine_get_local_conversation_pin_status.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(None), RcimGetBoolCb]
    rcim_engine_get_local_conversation_pin_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5649
if _libs["librust_universal_imsdk"].has("rcim_engine_mute_conversations", "cdecl"):
    rcim_engine_mute_conversations = _libs["librust_universal_imsdk"].get("rcim_engine_mute_conversations", "cdecl")
    rcim_engine_mute_conversations.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimConversationIdentifier), c_int32, enum_RcimPushNotificationMuteLevel, POINTER(None), RcimEngineErrorCb]
    rcim_engine_mute_conversations.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5669
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_conversation_mute_level", "cdecl"):
    rcim_engine_get_local_conversation_mute_level = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_conversation_mute_level", "cdecl")
    rcim_engine_get_local_conversation_mute_level.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(None), RcimGetLocalConversationMuteLevelCb]
    rcim_engine_get_local_conversation_mute_level.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5690
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_unread_conversation", "cdecl"):
    rcim_engine_get_local_unread_conversation = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_unread_conversation", "cdecl")
    rcim_engine_get_local_unread_conversation.argtypes = [POINTER(struct_RcimEngineSync), POINTER(enum_RcimConversationType), c_int32, POINTER(None), RcimGetConversationListCb]
    rcim_engine_get_local_unread_conversation.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5712
if _libs["librust_universal_imsdk"].has("rcim_engine_search_local_conversations", "cdecl"):
    rcim_engine_search_local_conversations = _libs["librust_universal_imsdk"].get("rcim_engine_search_local_conversations", "cdecl")
    rcim_engine_search_local_conversations.argtypes = [POINTER(struct_RcimEngineSync), POINTER(enum_RcimConversationType), c_int32, String, POINTER(POINTER(c_char)), c_int32, String, POINTER(None), RcimGetConversationListCb]
    rcim_engine_search_local_conversations.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5735
if _libs["librust_universal_imsdk"].has("rcim_engine_set_no_disturbing", "cdecl"):
    rcim_engine_set_no_disturbing = _libs["librust_universal_imsdk"].get("rcim_engine_set_no_disturbing", "cdecl")
    rcim_engine_set_no_disturbing.argtypes = [POINTER(struct_RcimEngineSync), String, c_int32, enum_RcimPushNotificationMuteLevel, POINTER(None), RcimEngineErrorCb]
    rcim_engine_set_no_disturbing.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5752
if _libs["librust_universal_imsdk"].has("rcim_engine_unset_no_disturbing", "cdecl"):
    rcim_engine_unset_no_disturbing = _libs["librust_universal_imsdk"].get("rcim_engine_unset_no_disturbing", "cdecl")
    rcim_engine_unset_no_disturbing.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimEngineErrorCb]
    rcim_engine_unset_no_disturbing.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5766
if _libs["librust_universal_imsdk"].has("rcim_engine_get_no_disturbing", "cdecl"):
    rcim_engine_get_no_disturbing = _libs["librust_universal_imsdk"].get("rcim_engine_get_no_disturbing", "cdecl")
    rcim_engine_get_no_disturbing.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimGetNoDisturbingCb]
    rcim_engine_get_no_disturbing.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5784
if _libs["librust_universal_imsdk"].has("rcim_engine_save_text_message_draft", "cdecl"):
    rcim_engine_save_text_message_draft = _libs["librust_universal_imsdk"].get("rcim_engine_save_text_message_draft", "cdecl")
    rcim_engine_save_text_message_draft.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_save_text_message_draft.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5805
if _libs["librust_universal_imsdk"].has("rcim_engine_get_text_message_draft", "cdecl"):
    rcim_engine_get_text_message_draft = _libs["librust_universal_imsdk"].get("rcim_engine_get_text_message_draft", "cdecl")
    rcim_engine_get_text_message_draft.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(None), RcimGetTextMessageDraftCb]
    rcim_engine_get_text_message_draft.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5822
if _libs["librust_universal_imsdk"].has("rcim_engine_get_total_unread_count", "cdecl"):
    rcim_engine_get_total_unread_count = _libs["librust_universal_imsdk"].get("rcim_engine_get_total_unread_count", "cdecl")
    rcim_engine_get_total_unread_count.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimGetCountCb]
    rcim_engine_get_total_unread_count.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5838
if _libs["librust_universal_imsdk"].has("rcim_engine_get_unread_count_by_conversations", "cdecl"):
    rcim_engine_get_unread_count_by_conversations = _libs["librust_universal_imsdk"].get("rcim_engine_get_unread_count_by_conversations", "cdecl")
    rcim_engine_get_unread_count_by_conversations.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimConversationIdentifier), c_int32, POINTER(None), RcimGetCountCb]
    rcim_engine_get_unread_count_by_conversations.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5857
if _libs["librust_universal_imsdk"].has("rcim_engine_get_unread_count", "cdecl"):
    rcim_engine_get_unread_count = _libs["librust_universal_imsdk"].get("rcim_engine_get_unread_count", "cdecl")
    rcim_engine_get_unread_count.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(None), RcimGetCountCb]
    rcim_engine_get_unread_count.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5875
if _libs["librust_universal_imsdk"].has("rcim_engine_get_unread_count_by_conversation_types", "cdecl"):
    rcim_engine_get_unread_count_by_conversation_types = _libs["librust_universal_imsdk"].get("rcim_engine_get_unread_count_by_conversation_types", "cdecl")
    rcim_engine_get_unread_count_by_conversation_types.argtypes = [POINTER(struct_RcimEngineSync), POINTER(enum_RcimConversationType), c_int32, c_bool, POINTER(None), RcimGetCountCb]
    rcim_engine_get_unread_count_by_conversation_types.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5895
if _libs["librust_universal_imsdk"].has("rcim_engine_clear_messages_unread_status", "cdecl"):
    rcim_engine_clear_messages_unread_status = _libs["librust_universal_imsdk"].get("rcim_engine_clear_messages_unread_status", "cdecl")
    rcim_engine_clear_messages_unread_status.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_clear_messages_unread_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5916
if _libs["librust_universal_imsdk"].has("rcim_engine_clear_messages_unread_status_by_send_time", "cdecl"):
    rcim_engine_clear_messages_unread_status_by_send_time = _libs["librust_universal_imsdk"].get("rcim_engine_clear_messages_unread_status_by_send_time", "cdecl")
    rcim_engine_clear_messages_unread_status_by_send_time.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, c_int64, POINTER(None), RcimEngineErrorCb]
    rcim_engine_clear_messages_unread_status_by_send_time.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5938
if _libs["librust_universal_imsdk"].has("rcim_engine_sync_conversation_read_status", "cdecl"):
    rcim_engine_sync_conversation_read_status = _libs["librust_universal_imsdk"].get("rcim_engine_sync_conversation_read_status", "cdecl")
    rcim_engine_sync_conversation_read_status.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, c_int64, POINTER(None), RcimEngineErrorCb]
    rcim_engine_sync_conversation_read_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5957
if _libs["librust_universal_imsdk"].has("rcim_engine_set_sync_conversation_read_status_listener", "cdecl"):
    rcim_engine_set_sync_conversation_read_status_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_sync_conversation_read_status_listener", "cdecl")
    rcim_engine_set_sync_conversation_read_status_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimConversationReadStatusLsr]
    rcim_engine_set_sync_conversation_read_status_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5976
if _libs["librust_universal_imsdk"].has("rcim_engine_get_unread_mentioned_messages", "cdecl"):
    rcim_engine_get_unread_mentioned_messages = _libs["librust_universal_imsdk"].get("rcim_engine_get_unread_mentioned_messages", "cdecl")
    rcim_engine_get_unread_mentioned_messages.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, c_int32, enum_RcimOrder, POINTER(None), RcimGetMessageListCb]
    rcim_engine_get_unread_mentioned_messages.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 5998
if _libs["librust_universal_imsdk"].has("rcim_engine_get_first_unread_message", "cdecl"):
    rcim_engine_get_first_unread_message = _libs["librust_universal_imsdk"].get("rcim_engine_get_first_unread_message", "cdecl")
    rcim_engine_get_first_unread_message.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimConversationType, String, String, POINTER(None), RcimCodeMessageCb]
    rcim_engine_get_first_unread_message.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6016
if _libs["librust_universal_imsdk"].has("rcim_engine_set_chatroom_status_listener", "cdecl"):
    rcim_engine_set_chatroom_status_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_chatroom_status_listener", "cdecl")
    rcim_engine_set_chatroom_status_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimChatroomStatusLsr]
    rcim_engine_set_chatroom_status_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6033
if _libs["librust_universal_imsdk"].has("rcim_engine_set_chatroom_member_changed_listener", "cdecl"):
    rcim_engine_set_chatroom_member_changed_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_chatroom_member_changed_listener", "cdecl")
    rcim_engine_set_chatroom_member_changed_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimChatroomMemberChangedLsr]
    rcim_engine_set_chatroom_member_changed_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6048
if _libs["librust_universal_imsdk"].has("rcim_engine_set_chatroom_member_banned_listener", "cdecl"):
    rcim_engine_set_chatroom_member_banned_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_chatroom_member_banned_listener", "cdecl")
    rcim_engine_set_chatroom_member_banned_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimChatroomMemberBannedLsr]
    rcim_engine_set_chatroom_member_banned_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6063
if _libs["librust_universal_imsdk"].has("rcim_engine_set_chatroom_member_blocked_listener", "cdecl"):
    rcim_engine_set_chatroom_member_blocked_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_chatroom_member_blocked_listener", "cdecl")
    rcim_engine_set_chatroom_member_blocked_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimChatroomMemberBlockedLsr]
    rcim_engine_set_chatroom_member_blocked_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6078
if _libs["librust_universal_imsdk"].has("rcim_engine_set_chatroom_multi_client_sync_listener", "cdecl"):
    rcim_engine_set_chatroom_multi_client_sync_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_chatroom_multi_client_sync_listener", "cdecl")
    rcim_engine_set_chatroom_multi_client_sync_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimChatroomMultiClientSyncLsr]
    rcim_engine_set_chatroom_multi_client_sync_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6096
if _libs["librust_universal_imsdk"].has("rcim_engine_join_chatroom", "cdecl"):
    rcim_engine_join_chatroom = _libs["librust_universal_imsdk"].get("rcim_engine_join_chatroom", "cdecl")
    rcim_engine_join_chatroom.argtypes = [POINTER(struct_RcimEngineSync), String, c_int32, POINTER(None), RcimJoinChatroomCb]
    rcim_engine_join_chatroom.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6114
if _libs["librust_universal_imsdk"].has("rcim_engine_join_existing_chatroom", "cdecl"):
    rcim_engine_join_existing_chatroom = _libs["librust_universal_imsdk"].get("rcim_engine_join_existing_chatroom", "cdecl")
    rcim_engine_join_existing_chatroom.argtypes = [POINTER(struct_RcimEngineSync), String, c_int32, POINTER(None), RcimJoinExistingChatroomCb]
    rcim_engine_join_existing_chatroom.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6131
if _libs["librust_universal_imsdk"].has("rcim_engine_quit_chatroom", "cdecl"):
    rcim_engine_quit_chatroom = _libs["librust_universal_imsdk"].get("rcim_engine_quit_chatroom", "cdecl")
    rcim_engine_quit_chatroom.argtypes = [POINTER(struct_RcimEngineSync), String, POINTER(None), RcimEngineErrorCb]
    rcim_engine_quit_chatroom.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6149
if _libs["librust_universal_imsdk"].has("rcim_engine_get_chatroom_info", "cdecl"):
    rcim_engine_get_chatroom_info = _libs["librust_universal_imsdk"].get("rcim_engine_get_chatroom_info", "cdecl")
    rcim_engine_get_chatroom_info.argtypes = [POINTER(struct_RcimEngineSync), String, c_int32, enum_RcimOrder, POINTER(None), RcimGetChatroomInfoCb]
    rcim_engine_get_chatroom_info.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6167
if _libs["librust_universal_imsdk"].has("rcim_engine_set_chatroom_kv_sync_listener", "cdecl"):
    rcim_engine_set_chatroom_kv_sync_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_chatroom_kv_sync_listener", "cdecl")
    rcim_engine_set_chatroom_kv_sync_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimChatroomKvSyncLsr]
    rcim_engine_set_chatroom_kv_sync_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6182
if _libs["librust_universal_imsdk"].has("rcim_engine_set_chatroom_kv_changed_listener", "cdecl"):
    rcim_engine_set_chatroom_kv_changed_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_chatroom_kv_changed_listener", "cdecl")
    rcim_engine_set_chatroom_kv_changed_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimChatroomKvChangedLsr]
    rcim_engine_set_chatroom_kv_changed_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6197
if _libs["librust_universal_imsdk"].has("rcim_engine_set_chatroom_kv_delete_listener", "cdecl"):
    rcim_engine_set_chatroom_kv_delete_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_chatroom_kv_delete_listener", "cdecl")
    rcim_engine_set_chatroom_kv_delete_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimChatroomKvDeleteLsr]
    rcim_engine_set_chatroom_kv_delete_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6218
if _libs["librust_universal_imsdk"].has("rcim_engine_set_chatroom_kvs", "cdecl"):
    rcim_engine_set_chatroom_kvs = _libs["librust_universal_imsdk"].get("rcim_engine_set_chatroom_kvs", "cdecl")
    rcim_engine_set_chatroom_kvs.argtypes = [POINTER(struct_RcimEngineSync), String, POINTER(struct_RcimChatroomKvInfo), c_int32, c_bool, c_bool, POINTER(None), RcimChatroomKvCb]
    rcim_engine_set_chatroom_kvs.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6241
if _libs["librust_universal_imsdk"].has("rcim_engine_delete_chatroom_kvs", "cdecl"):
    rcim_engine_delete_chatroom_kvs = _libs["librust_universal_imsdk"].get("rcim_engine_delete_chatroom_kvs", "cdecl")
    rcim_engine_delete_chatroom_kvs.argtypes = [POINTER(struct_RcimEngineSync), String, POINTER(POINTER(c_char)), c_int32, c_bool, POINTER(None), RcimChatroomKvCb]
    rcim_engine_delete_chatroom_kvs.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6262
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_chatroom_kv_by_keys", "cdecl"):
    rcim_engine_get_local_chatroom_kv_by_keys = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_chatroom_kv_by_keys", "cdecl")
    rcim_engine_get_local_chatroom_kv_by_keys.argtypes = [POINTER(struct_RcimEngineSync), String, POINTER(POINTER(c_char)), c_int32, POINTER(None), RcimChatroomGetKvCb]
    rcim_engine_get_local_chatroom_kv_by_keys.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6280
if _libs["librust_universal_imsdk"].has("rcim_engine_get_chatroom_all_kvs", "cdecl"):
    rcim_engine_get_chatroom_all_kvs = _libs["librust_universal_imsdk"].get("rcim_engine_get_chatroom_all_kvs", "cdecl")
    rcim_engine_get_chatroom_all_kvs.argtypes = [POINTER(struct_RcimEngineSync), String, POINTER(None), RcimChatroomGetKvCb]
    rcim_engine_get_chatroom_all_kvs.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6296
if _libs["librust_universal_imsdk"].has("rcim_engine_set_log_listener", "cdecl"):
    rcim_engine_set_log_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_log_listener", "cdecl")
    rcim_engine_set_log_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimLogLsr]
    rcim_engine_set_log_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6310
if _libs["librust_universal_imsdk"].has("rcim_engine_set_log_filter", "cdecl"):
    rcim_engine_set_log_filter = _libs["librust_universal_imsdk"].get("rcim_engine_set_log_filter", "cdecl")
    rcim_engine_set_log_filter.argtypes = [POINTER(struct_RcimEngineSync), enum_RcimLogLevel]
    rcim_engine_set_log_filter.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6323
if _libs["librust_universal_imsdk"].has("rcim_engine_insert_log", "cdecl"):
    rcim_engine_insert_log = _libs["librust_universal_imsdk"].get("rcim_engine_insert_log", "cdecl")
    rcim_engine_insert_log.argtypes = [POINTER(struct_RcimEngineSync), POINTER(struct_RcimInsertLogInfo)]
    rcim_engine_insert_log.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6330
if _libs["librust_universal_imsdk"].has("rcim_dev_log_init", "cdecl"):
    rcim_dev_log_init = _libs["librust_universal_imsdk"].get("rcim_dev_log_init", "cdecl")
    rcim_dev_log_init.argtypes = [RcimDevLogLsr]
    rcim_dev_log_init.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6343
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_public_service", "cdecl"):
    rcim_engine_get_local_public_service = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_public_service", "cdecl")
    rcim_engine_get_local_public_service.argtypes = [POINTER(struct_RcimEngineSync), String, POINTER(None), RcimGetPublicServiceCb]
    rcim_engine_get_local_public_service.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6360
if _libs["librust_universal_imsdk"].has("rcim_engine_get_local_all_public_services", "cdecl"):
    rcim_engine_get_local_all_public_services = _libs["librust_universal_imsdk"].get("rcim_engine_get_local_all_public_services", "cdecl")
    rcim_engine_get_local_all_public_services.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimGetLocalPublicServiceListCb]
    rcim_engine_get_local_all_public_services.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6375
if _libs["librust_universal_imsdk"].has("rcim_engine_set_voip_call_info_listener", "cdecl"):
    rcim_engine_set_voip_call_info_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_voip_call_info_listener", "cdecl")
    rcim_engine_set_voip_call_info_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimVoipCallInfoLsr]
    rcim_engine_set_voip_call_info_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6396
if _libs["librust_universal_imsdk"].has("rcim_engine_send_rtc_signaling", "cdecl"):
    rcim_engine_send_rtc_signaling = _libs["librust_universal_imsdk"].get("rcim_engine_send_rtc_signaling", "cdecl")
    rcim_engine_send_rtc_signaling.argtypes = [POINTER(struct_RcimEngineSync), String, String, c_bool, POINTER(uint8_t), c_int32, c_int32, POINTER(c_int64), POINTER(None), RcimSendRtcSignalingCb]
    rcim_engine_send_rtc_signaling.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6418
if _libs["librust_universal_imsdk"].has("rcim_engine_cancel_rtc_signaling", "cdecl"):
    rcim_engine_cancel_rtc_signaling = _libs["librust_universal_imsdk"].get("rcim_engine_cancel_rtc_signaling", "cdecl")
    rcim_engine_cancel_rtc_signaling.argtypes = [POINTER(struct_RcimEngineSync), POINTER(c_int64), c_int32]
    rcim_engine_cancel_rtc_signaling.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6431
if _libs["librust_universal_imsdk"].has("rcim_engine_set_rtc_heartbeat_send_listener", "cdecl"):
    rcim_engine_set_rtc_heartbeat_send_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_rtc_heartbeat_send_listener", "cdecl")
    rcim_engine_set_rtc_heartbeat_send_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimRtcHeartBeatSendLsr]
    rcim_engine_set_rtc_heartbeat_send_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6444
if _libs["librust_universal_imsdk"].has("rcim_engine_set_rtc_heartbeat_send_result_listener", "cdecl"):
    rcim_engine_set_rtc_heartbeat_send_result_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_rtc_heartbeat_send_result_listener", "cdecl")
    rcim_engine_set_rtc_heartbeat_send_result_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimRtcHeartBeatResultLsr]
    rcim_engine_set_rtc_heartbeat_send_result_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6459
if _libs["librust_universal_imsdk"].has("rcim_engine_set_rtc_room_event_listener", "cdecl"):
    rcim_engine_set_rtc_room_event_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_rtc_room_event_listener", "cdecl")
    rcim_engine_set_rtc_room_event_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimRtcRoomEventLsr]
    rcim_engine_set_rtc_room_event_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6475
if _libs["librust_universal_imsdk"].has("rcim_engine_send_rtc_heartbeat", "cdecl"):
    rcim_engine_send_rtc_heartbeat = _libs["librust_universal_imsdk"].get("rcim_engine_send_rtc_heartbeat", "cdecl")
    rcim_engine_send_rtc_heartbeat.argtypes = [POINTER(struct_RcimEngineSync), POINTER(POINTER(c_char)), c_int32, c_int32]
    rcim_engine_send_rtc_heartbeat.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6493
if _libs["librust_universal_imsdk"].has("rcim_engine_rtc_set_kv_signaling", "cdecl"):
    rcim_engine_rtc_set_kv_signaling = _libs["librust_universal_imsdk"].get("rcim_engine_rtc_set_kv_signaling", "cdecl")
    rcim_engine_rtc_set_kv_signaling.argtypes = [POINTER(struct_RcimEngineSync), String, String, String, POINTER(None), RcimRtcSetKVSignalingCb]
    rcim_engine_rtc_set_kv_signaling.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6511
if _libs["librust_universal_imsdk"].has("rcim_engine_set_rtc_kv_signaling_listener", "cdecl"):
    rcim_engine_set_rtc_kv_signaling_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_rtc_kv_signaling_listener", "cdecl")
    rcim_engine_set_rtc_kv_signaling_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimRtcKvSignalingLsr]
    rcim_engine_set_rtc_kv_signaling_listener.restype = enum_RcimEngineError

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6523
if _libs["librust_universal_imsdk"].has("rcim_malloc_message_box", "cdecl"):
    rcim_malloc_message_box = _libs["librust_universal_imsdk"].get("rcim_malloc_message_box", "cdecl")
    rcim_malloc_message_box.argtypes = []
    rcim_malloc_message_box.restype = POINTER(struct_RcimMessageBox)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6535
if _libs["librust_universal_imsdk"].has("rcim_free_message_box", "cdecl"):
    rcim_free_message_box = _libs["librust_universal_imsdk"].get("rcim_free_message_box", "cdecl")
    rcim_free_message_box.argtypes = [POINTER(struct_RcimMessageBox)]
    rcim_free_message_box.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6547
if _libs["librust_universal_imsdk"].has("rcim_malloc_message_box_vec", "cdecl"):
    rcim_malloc_message_box_vec = _libs["librust_universal_imsdk"].get("rcim_malloc_message_box_vec", "cdecl")
    rcim_malloc_message_box_vec.argtypes = [c_int32]
    rcim_malloc_message_box_vec.restype = POINTER(struct_RcimMessageBox)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6560
if _libs["librust_universal_imsdk"].has("rcim_free_message_box_vec", "cdecl"):
    rcim_free_message_box_vec = _libs["librust_universal_imsdk"].get("rcim_free_message_box_vec", "cdecl")
    rcim_free_message_box_vec.argtypes = [POINTER(struct_RcimMessageBox), c_int32]
    rcim_free_message_box_vec.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6571
if _libs["librust_universal_imsdk"].has("rcim_malloc_receive_status", "cdecl"):
    rcim_malloc_receive_status = _libs["librust_universal_imsdk"].get("rcim_malloc_receive_status", "cdecl")
    rcim_malloc_receive_status.argtypes = []
    rcim_malloc_receive_status.restype = POINTER(struct_RcimReceivedStatus)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6583
if _libs["librust_universal_imsdk"].has("rcim_free_receive_status", "cdecl"):
    rcim_free_receive_status = _libs["librust_universal_imsdk"].get("rcim_free_receive_status", "cdecl")
    rcim_free_receive_status.argtypes = [POINTER(struct_RcimReceivedStatus)]
    rcim_free_receive_status.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6593
if _libs["librust_universal_imsdk"].has("rcim_malloc_push_config", "cdecl"):
    rcim_malloc_push_config = _libs["librust_universal_imsdk"].get("rcim_malloc_push_config", "cdecl")
    rcim_malloc_push_config.argtypes = []
    rcim_malloc_push_config.restype = POINTER(struct_RcimPushConfig)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6605
if _libs["librust_universal_imsdk"].has("rcim_free_push_config", "cdecl"):
    rcim_free_push_config = _libs["librust_universal_imsdk"].get("rcim_free_push_config", "cdecl")
    rcim_free_push_config.argtypes = [POINTER(struct_RcimPushConfig)]
    rcim_free_push_config.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6615
if _libs["librust_universal_imsdk"].has("rcim_malloc_ios_config", "cdecl"):
    rcim_malloc_ios_config = _libs["librust_universal_imsdk"].get("rcim_malloc_ios_config", "cdecl")
    rcim_malloc_ios_config.argtypes = []
    rcim_malloc_ios_config.restype = POINTER(struct_RcimIosConfig)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6626
if _libs["librust_universal_imsdk"].has("rcim_free_ios_config", "cdecl"):
    rcim_free_ios_config = _libs["librust_universal_imsdk"].get("rcim_free_ios_config", "cdecl")
    rcim_free_ios_config.argtypes = [POINTER(struct_RcimIosConfig)]
    rcim_free_ios_config.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6636
if _libs["librust_universal_imsdk"].has("rcim_malloc_android_config", "cdecl"):
    rcim_malloc_android_config = _libs["librust_universal_imsdk"].get("rcim_malloc_android_config", "cdecl")
    rcim_malloc_android_config.argtypes = []
    rcim_malloc_android_config.restype = POINTER(struct_RcimAndroidConfig)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6647
if _libs["librust_universal_imsdk"].has("rcim_free_android_config", "cdecl"):
    rcim_free_android_config = _libs["librust_universal_imsdk"].get("rcim_free_android_config", "cdecl")
    rcim_free_android_config.argtypes = [POINTER(struct_RcimAndroidConfig)]
    rcim_free_android_config.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6657
if _libs["librust_universal_imsdk"].has("rcim_malloc_harmony_config", "cdecl"):
    rcim_malloc_harmony_config = _libs["librust_universal_imsdk"].get("rcim_malloc_harmony_config", "cdecl")
    rcim_malloc_harmony_config.argtypes = []
    rcim_malloc_harmony_config.restype = POINTER(struct_RcimHarmonyConfig)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6668
if _libs["librust_universal_imsdk"].has("rcim_free_harmony_config", "cdecl"):
    rcim_free_harmony_config = _libs["librust_universal_imsdk"].get("rcim_free_harmony_config", "cdecl")
    rcim_free_harmony_config.argtypes = [POINTER(struct_RcimHarmonyConfig)]
    rcim_free_harmony_config.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6678
if _libs["librust_universal_imsdk"].has("rcim_malloc_msg_type", "cdecl"):
    rcim_malloc_msg_type = _libs["librust_universal_imsdk"].get("rcim_malloc_msg_type", "cdecl")
    rcim_malloc_msg_type.argtypes = []
    rcim_malloc_msg_type.restype = POINTER(struct_RcimMessageType)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6689
if _libs["librust_universal_imsdk"].has("rcim_free_msg_type", "cdecl"):
    rcim_free_msg_type = _libs["librust_universal_imsdk"].get("rcim_free_msg_type", "cdecl")
    rcim_free_msg_type.argtypes = [POINTER(struct_RcimMessageType)]
    rcim_free_msg_type.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6699
if _libs["librust_universal_imsdk"].has("rcim_malloc_conversation", "cdecl"):
    rcim_malloc_conversation = _libs["librust_universal_imsdk"].get("rcim_malloc_conversation", "cdecl")
    rcim_malloc_conversation.argtypes = []
    rcim_malloc_conversation.restype = POINTER(struct_RcimConversation)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6710
if _libs["librust_universal_imsdk"].has("rcim_free_conversation", "cdecl"):
    rcim_free_conversation = _libs["librust_universal_imsdk"].get("rcim_free_conversation", "cdecl")
    rcim_free_conversation.argtypes = [POINTER(struct_RcimConversation)]
    rcim_free_conversation.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6720
if _libs["librust_universal_imsdk"].has("rcim_malloc_conversation_identifier", "cdecl"):
    rcim_malloc_conversation_identifier = _libs["librust_universal_imsdk"].get("rcim_malloc_conversation_identifier", "cdecl")
    rcim_malloc_conversation_identifier.argtypes = []
    rcim_malloc_conversation_identifier.restype = POINTER(struct_RcimConversationIdentifier)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6731
if _libs["librust_universal_imsdk"].has("rcim_free_conversation_identifier_c", "cdecl"):
    rcim_free_conversation_identifier_c = _libs["librust_universal_imsdk"].get("rcim_free_conversation_identifier_c", "cdecl")
    rcim_free_conversation_identifier_c.argtypes = [POINTER(struct_RcimConversationIdentifier)]
    rcim_free_conversation_identifier_c.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6743
if _libs["librust_universal_imsdk"].has("rcim_malloc_conversation_identifier_vec", "cdecl"):
    rcim_malloc_conversation_identifier_vec = _libs["librust_universal_imsdk"].get("rcim_malloc_conversation_identifier_vec", "cdecl")
    rcim_malloc_conversation_identifier_vec.argtypes = [c_int32]
    rcim_malloc_conversation_identifier_vec.restype = POINTER(struct_RcimConversationIdentifier)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6755
if _libs["librust_universal_imsdk"].has("rcim_free_conversation_identifier_vec", "cdecl"):
    rcim_free_conversation_identifier_vec = _libs["librust_universal_imsdk"].get("rcim_free_conversation_identifier_vec", "cdecl")
    rcim_free_conversation_identifier_vec.argtypes = [POINTER(struct_RcimConversationIdentifier), c_int32]
    rcim_free_conversation_identifier_vec.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6766
if _libs["librust_universal_imsdk"].has("rcim_malloc_sdk_version", "cdecl"):
    rcim_malloc_sdk_version = _libs["librust_universal_imsdk"].get("rcim_malloc_sdk_version", "cdecl")
    rcim_malloc_sdk_version.argtypes = []
    rcim_malloc_sdk_version.restype = POINTER(struct_RcimSDKVersion)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6777
if _libs["librust_universal_imsdk"].has("rcim_free_sdk_version", "cdecl"):
    rcim_free_sdk_version = _libs["librust_universal_imsdk"].get("rcim_free_sdk_version", "cdecl")
    rcim_free_sdk_version.argtypes = [POINTER(struct_RcimSDKVersion)]
    rcim_free_sdk_version.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6787
if _libs["librust_universal_imsdk"].has("rcim_malloc_engine_builder_param", "cdecl"):
    rcim_malloc_engine_builder_param = _libs["librust_universal_imsdk"].get("rcim_malloc_engine_builder_param", "cdecl")
    rcim_malloc_engine_builder_param.argtypes = []
    rcim_malloc_engine_builder_param.restype = POINTER(struct_RcimEngineBuilderParam)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6798
if _libs["librust_universal_imsdk"].has("rcim_free_engine_builder_param", "cdecl"):
    rcim_free_engine_builder_param = _libs["librust_universal_imsdk"].get("rcim_free_engine_builder_param", "cdecl")
    rcim_free_engine_builder_param.argtypes = [POINTER(struct_RcimEngineBuilderParam)]
    rcim_free_engine_builder_param.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6810
if _libs["librust_universal_imsdk"].has("rcim_malloc_push_token_info_vec", "cdecl"):
    rcim_malloc_push_token_info_vec = _libs["librust_universal_imsdk"].get("rcim_malloc_push_token_info_vec", "cdecl")
    rcim_malloc_push_token_info_vec.argtypes = [c_int32]
    rcim_malloc_push_token_info_vec.restype = POINTER(struct_RcimPushTokenInfo)

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6822
if _libs["librust_universal_imsdk"].has("rcim_free_push_token_info_vec", "cdecl"):
    rcim_free_push_token_info_vec = _libs["librust_universal_imsdk"].get("rcim_free_push_token_info_vec", "cdecl")
    rcim_free_push_token_info_vec.argtypes = [POINTER(struct_RcimPushTokenInfo), c_int32]
    rcim_free_push_token_info_vec.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6834
if _libs["librust_universal_imsdk"].has("rcim_free_char", "cdecl"):
    rcim_free_char = _libs["librust_universal_imsdk"].get("rcim_free_char", "cdecl")
    rcim_free_char.argtypes = [String]
    rcim_free_char.restype = None

# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 6840
if _libs["librust_universal_imsdk"].has("rcim_engine_set_cmp_send_listener", "cdecl"):
    rcim_engine_set_cmp_send_listener = _libs["librust_universal_imsdk"].get("rcim_engine_set_cmp_send_listener", "cdecl")
    rcim_engine_set_cmp_send_listener.argtypes = [POINTER(struct_RcimEngineSync), POINTER(None), RcimCmpSendCb]
    rcim_engine_set_cmp_send_listener.restype = enum_RcimEngineError

RcimEngineBuilder = struct_RcimEngineBuilder# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1846

RcimEngineSync = struct_RcimEngineSync# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1851

RcimSDKVersion = struct_RcimSDKVersion# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1865

RcimEngineBuilderParam = struct_RcimEngineBuilderParam# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1920

RcimPushTokenInfo = struct_RcimPushTokenInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1942

RcimReceivedStatus = struct_RcimReceivedStatus# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1978

RcimReadReceiptUserInfo = struct_RcimReadReceiptUserInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 1992

RcimReadReceiptInfo = struct_RcimReadReceiptInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2008

RcimReadReceiptInfoV2 = struct_RcimReadReceiptInfoV2# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2028

RcimIosConfig = struct_RcimIosConfig# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2060

RcimAndroidConfig = struct_RcimAndroidConfig# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2146

RcimHarmonyConfig = struct_RcimHarmonyConfig# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2161

RcimPushConfig = struct_RcimPushConfig# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2213

RcimMessageBox = struct_RcimMessageBox# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2321

RcimReceivedInfo = struct_RcimReceivedInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2330

RcimRecallNotificationMessage = struct_RcimRecallNotificationMessage# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2445

RcimMessageBlockInfo = struct_RcimMessageBlockInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2499

RcimSendMessageOption = struct_RcimSendMessageOption# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2530

RcimSendReadReceiptResponseMessageData = struct_RcimSendReadReceiptResponseMessageData# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2563

RcimReadReceiptV2ReaderInfo = struct_RcimReadReceiptV2ReaderInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2632

RcimMessageType = struct_RcimMessageType# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2774

RcimMessageExpansionKvInfo = struct_RcimMessageExpansionKvInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2788

RcimConversationStatusChangeItem = struct_RcimConversationStatusChangeItem# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2882

RcimTypingStatus = struct_RcimTypingStatus# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2908

RcimConversation = struct_RcimConversation# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2964

RcimConversationIdentifier = struct_RcimConversationIdentifier# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 2994

RcimChatroomJoinedInfo = struct_RcimChatroomJoinedInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3083

RcimChatroomMemberActionInfo = struct_RcimChatroomMemberActionInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3112

RcimChatroomMemberChangeInfo = struct_RcimChatroomMemberChangeInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3134

RcimChatroomMemberBannedInfo = struct_RcimChatroomMemberBannedInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3177

RcimChatroomMemberBlockedInfo = struct_RcimChatroomMemberBlockedInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3217

RcimChatroomMultiClientSyncInfo = struct_RcimChatroomMultiClientSyncInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3252

RcimChatroomUserInfo = struct_RcimChatroomUserInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3288

RcimChatroomInfo = struct_RcimChatroomInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3314

RcimChatroomKvInfo = struct_RcimChatroomKvInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3340

RcimChatroomKeyErrorInfo = struct_RcimChatroomKeyErrorInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3374

RcimLogInfo = struct_RcimLogInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3442

RcimInsertLogInfo = struct_RcimInsertLogInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3484

RcimPublicServiceMenuItem = struct_RcimPublicServiceMenuItem# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3491

RcimPublicServiceInfo = struct_RcimPublicServiceInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3559

RcimRtcConfig = struct_RcimRtcConfig# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3597

RcimRtcKvInfo = struct_RcimRtcKvInfo# /Users/haiyin/code/python/rc-im-mcp-demo/lib/rcim_client.h: 3670

# No inserted files

# No prefix-stripping

