#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : eventlet
Version  : 0.20.0
Release  : 47
URL      : https://files.pythonhosted.org/packages/8b/c3/310059af7f77d18ac92d0927fea4e84b55ed0e9ddc57ae13937bd0c44187/eventlet-0.20.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8b/c3/310059af7f77d18ac92d0927fea4e84b55ed0e9ddc57ae13937bd0c44187/eventlet-0.20.0.tar.gz
Summary  : Highly concurrent networking library
Group    : Development/Tools
License  : MIT
Requires: eventlet-python3
Requires: eventlet-license
Requires: eventlet-python
Requires: greenlet
BuildRequires : buildreq-distutils3
BuildRequires : greenlet
BuildRequires : greenlet-python
BuildRequires : nose
BuildRequires : nose-python
Patch1: 0002-Replace-enum-compat-dependency-to-enum34.patch

%description
It uses epoll or libevent for highly scalable non-blocking I/O.  Coroutines ensure that the developer uses a blocking style of programming that is similar to threading, but provide the benefits of non-blocking I/O.  The event dispatch is implicit, which means you can easily use Eventlet from the Python interpreter, or as a small part of a larger application.
        
        It's easy to get started using Eventlet, and easy to convert existing
        applications to use it.  Start off by looking at the `examples`_,
        `common design patterns`_, and the list of `basic API primitives`_.

%package license
Summary: license components for the eventlet package.
Group: Default

%description license
license components for the eventlet package.


%package python
Summary: python components for the eventlet package.
Group: Default
Requires: eventlet-python3

%description python
python components for the eventlet package.


%package python3
Summary: python3 components for the eventlet package.
Group: Default
Requires: python3-core

%description python3
python3 components for the eventlet package.


%prep
%setup -q -n eventlet-0.20.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533842840
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/eventlet
cp LICENSE %{buildroot}/usr/share/doc/eventlet/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/eventlet/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
