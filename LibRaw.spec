#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : LibRaw
Version  : 0.18.11
Release  : 9
URL      : https://www.libraw.org/data/LibRaw-0.18.11.tar.gz
Source0  : https://www.libraw.org/data/LibRaw-0.18.11.tar.gz
Summary  : Raw image decoder library (non-thread-safe)
Group    : Development/Tools
License  : CDDL-1.1 LGPL-2.1
Requires: LibRaw-bin
Requires: LibRaw-lib
Requires: LibRaw-doc
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(lcms2)
BuildRequires : qtbase-dev

%description
======================   LibRaw ==============================
== Library for reading and processing of RAW digicam images ==

%package bin
Summary: bin components for the LibRaw package.
Group: Binaries

%description bin
bin components for the LibRaw package.


%package dev
Summary: dev components for the LibRaw package.
Group: Development
Requires: LibRaw-lib
Requires: LibRaw-bin
Provides: LibRaw-devel

%description dev
dev components for the LibRaw package.


%package doc
Summary: doc components for the LibRaw package.
Group: Documentation

%description doc
doc components for the LibRaw package.


%package lib
Summary: lib components for the LibRaw package.
Group: Libraries

%description lib
lib components for the LibRaw package.


%prep
%setup -q -n LibRaw-0.18.11
pushd ..
cp -a LibRaw-0.18.11 buildavx2
popd
pushd ..
cp -a LibRaw-0.18.11 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525957315
%configure --disable-static
make

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static    --libdir=/usr/lib64/haswell
make
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=skylake-avx512"
export CXXFLAGS="$CXXFLAGS -m64 -march=skylake-avx512"
export LDFLAGS="$LDFLAGS -m64 -march=skylake-avx512"
%configure --disable-static    --libdir=/usr/lib64/haswell/avx512_1 --bindir=/usr/bin/haswell/avx512_1
make
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1525957315
rm -rf %{buildroot}
pushd ../buildavx2/
%make_install
popd
pushd ../buildavx512/
%make_install
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/4channels
/usr/bin/dcraw_emu
/usr/bin/dcraw_half
/usr/bin/half_mt
/usr/bin/haswell/avx512_1/4channels
/usr/bin/haswell/avx512_1/dcraw_emu
/usr/bin/haswell/avx512_1/dcraw_half
/usr/bin/haswell/avx512_1/half_mt
/usr/bin/haswell/avx512_1/mem_image
/usr/bin/haswell/avx512_1/multirender_test
/usr/bin/haswell/avx512_1/postprocessing_benchmark
/usr/bin/haswell/avx512_1/raw-identify
/usr/bin/haswell/avx512_1/simple_dcraw
/usr/bin/haswell/avx512_1/unprocessed_raw
/usr/bin/mem_image
/usr/bin/multirender_test
/usr/bin/postprocessing_benchmark
/usr/bin/raw-identify
/usr/bin/simple_dcraw
/usr/bin/unprocessed_raw

%files dev
%defattr(-,root,root,-)
/usr/include/libraw/libraw.h
/usr/include/libraw/libraw_alloc.h
/usr/include/libraw/libraw_const.h
/usr/include/libraw/libraw_datastream.h
/usr/include/libraw/libraw_internal.h
/usr/include/libraw/libraw_types.h
/usr/include/libraw/libraw_version.h
/usr/lib64/haswell/libraw.so
/usr/lib64/haswell/libraw_r.so
/usr/lib64/libraw.so
/usr/lib64/libraw_r.so
/usr/lib64/pkgconfig/libraw.pc
/usr/lib64/pkgconfig/libraw_r.pc

%files doc
%defattr(-,root,root,-)
/usr/share/doc/libraw/COPYRIGHT
/usr/share/doc/libraw/Changelog.txt
/usr/share/doc/libraw/LICENSE.CDDL
/usr/share/doc/libraw/LICENSE.LGPL

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libraw.so
/usr/lib64/haswell/avx512_1/libraw.so.16
/usr/lib64/haswell/avx512_1/libraw.so.16.0.0
/usr/lib64/haswell/avx512_1/libraw_r.so
/usr/lib64/haswell/avx512_1/libraw_r.so.16
/usr/lib64/haswell/avx512_1/libraw_r.so.16.0.0
/usr/lib64/haswell/libraw.so.16
/usr/lib64/haswell/libraw.so.16.0.0
/usr/lib64/haswell/libraw_r.so.16
/usr/lib64/haswell/libraw_r.so.16.0.0
/usr/lib64/libraw.so.16
/usr/lib64/libraw.so.16.0.0
/usr/lib64/libraw_r.so.16
/usr/lib64/libraw_r.so.16.0.0
