#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : eventlet
Version  : 0.19.0
Release  : 30
URL      : http://pypi.debian.net/eventlet/eventlet-0.19.0.tar.gz
Source0  : http://pypi.debian.net/eventlet/eventlet-0.19.0.tar.gz
Summary  : Highly concurrent networking library
Group    : Development/Tools
License  : MIT
Requires: eventlet-python
BuildRequires : greenlet
BuildRequires : greenlet-python
BuildRequires : nose
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-Logging-speedy.patch

%description
Eventlet is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.

%package python
Summary: python components for the eventlet package.
Group: Default
Requires: greenlet-python

%description python
python components for the eventlet package.


%prep
%setup -q -n eventlet-0.19.0
%patch1 -p1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
