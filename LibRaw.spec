#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : LibRaw
Version  : 0.18.2
Release  : 2
URL      : http://www.libraw.org/data/LibRaw-0.18.2.tar.gz
Source0  : http://www.libraw.org/data/LibRaw-0.18.2.tar.gz
Summary  : Raw image decoder library (non-thread-safe)
Group    : Development/Tools
License  : CDDL-1.1 LGPL-2.1
Requires: LibRaw-bin
Requires: LibRaw-lib
Requires: LibRaw-data
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(lcms2)

%description
======================   LibRaw ==============================
== Library for reading and processing of RAW digicam images ==

%package bin
Summary: bin components for the LibRaw package.
Group: Binaries
Requires: LibRaw-data

%description bin
bin components for the LibRaw package.


%package data
Summary: data components for the LibRaw package.
Group: Data

%description data
data components for the LibRaw package.


%package dev
Summary: dev components for the LibRaw package.
Group: Development
Requires: LibRaw-lib
Requires: LibRaw-bin
Requires: LibRaw-data
Provides: LibRaw-devel

%description dev
dev components for the LibRaw package.


%package lib
Summary: lib components for the LibRaw package.
Group: Libraries
Requires: LibRaw-data

%description lib
lib components for the LibRaw package.


%prep
%setup -q -n LibRaw-0.18.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491995166
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491995166
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/4channels
/usr/bin/dcraw_emu
/usr/bin/dcraw_half
/usr/bin/half_mt
/usr/bin/mem_image
/usr/bin/multirender_test
/usr/bin/postprocessing_benchmark
/usr/bin/raw-identify
/usr/bin/simple_dcraw
/usr/bin/unprocessed_raw

%files data
%defattr(-,root,root,-)
/usr/share/doc/libraw/COPYRIGHT
/usr/share/doc/libraw/Changelog.txt
/usr/share/doc/libraw/LICENSE.CDDL
/usr/share/doc/libraw/LICENSE.LGPL

%files dev
%defattr(-,root,root,-)
/usr/include/libraw/libraw.h
/usr/include/libraw/libraw_alloc.h
/usr/include/libraw/libraw_const.h
/usr/include/libraw/libraw_datastream.h
/usr/include/libraw/libraw_internal.h
/usr/include/libraw/libraw_types.h
/usr/include/libraw/libraw_version.h
/usr/lib64/libraw.so
/usr/lib64/libraw_r.so
/usr/lib64/pkgconfig/libraw.pc
/usr/lib64/pkgconfig/libraw_r.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libraw.so.16
/usr/lib64/libraw.so.16.0.0
/usr/lib64/libraw_r.so.16
/usr/lib64/libraw_r.so.16.0.0
