#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : LibRaw
Version  : 0.20.2
Release  : 35
URL      : https://www.libraw.org/data/LibRaw-0.20.2.tar.gz
Source0  : https://www.libraw.org/data/LibRaw-0.20.2.tar.gz
Summary  : Raw image decoder library (thread-safe)
Group    : Development/Tools
License  : CDDL-1.0 LGPL-2.1
Requires: LibRaw-bin = %{version}-%{release}
Requires: LibRaw-filemap = %{version}-%{release}
Requires: LibRaw-lib = %{version}-%{release}
Requires: LibRaw-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(zlib)

%description
================= Compile LibRaw with RawSpeed support ========================
0) RawSpeed version:
LibRaw supports 'master' version of RawSpeed library: https://github.com/darktable-org/rawspeed/tree/master

%package bin
Summary: bin components for the LibRaw package.
Group: Binaries
Requires: LibRaw-license = %{version}-%{release}
Requires: LibRaw-filemap = %{version}-%{release}

%description bin
bin components for the LibRaw package.


%package dev
Summary: dev components for the LibRaw package.
Group: Development
Requires: LibRaw-lib = %{version}-%{release}
Requires: LibRaw-bin = %{version}-%{release}
Provides: LibRaw-devel = %{version}-%{release}
Requires: LibRaw = %{version}-%{release}

%description dev
dev components for the LibRaw package.


%package doc
Summary: doc components for the LibRaw package.
Group: Documentation

%description doc
doc components for the LibRaw package.


%package filemap
Summary: filemap components for the LibRaw package.
Group: Default

%description filemap
filemap components for the LibRaw package.


%package lib
Summary: lib components for the LibRaw package.
Group: Libraries
Requires: LibRaw-license = %{version}-%{release}
Requires: LibRaw-filemap = %{version}-%{release}

%description lib
lib components for the LibRaw package.


%package license
Summary: license components for the LibRaw package.
Group: Default

%description license
license components for the LibRaw package.


%prep
%setup -q -n LibRaw-0.20.2
cd %{_builddir}/LibRaw-0.20.2
pushd ..
cp -a LibRaw-0.20.2 buildavx2
popd
pushd ..
cp -a LibRaw-0.20.2 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665094369
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%reconfigure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :
cd ../buildavx512;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1665094369
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/LibRaw
cp %{_builddir}/LibRaw-%{version}/LICENSE.CDDL %{buildroot}/usr/share/package-licenses/LibRaw/c24b9c7ef03687bf0141f85a1b7ed81459944c3c
cp %{_builddir}/LibRaw-%{version}/LICENSE.LGPL %{buildroot}/usr/share/package-licenses/LibRaw/39a21f33cadea18adcc23bf808d7d5ea6419c8b1
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/bin/rawtextdump
/usr/bin/simple_dcraw
/usr/bin/unprocessed_raw
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/libraw/libraw.h
/usr/include/libraw/libraw_alloc.h
/usr/include/libraw/libraw_const.h
/usr/include/libraw/libraw_datastream.h
/usr/include/libraw/libraw_internal.h
/usr/include/libraw/libraw_types.h
/usr/include/libraw/libraw_version.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libraw.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libraw_r.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libraw.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libraw_r.so
/usr/lib64/libraw.so
/usr/lib64/libraw_r.so
/usr/lib64/pkgconfig/libraw.pc
/usr/lib64/pkgconfig/libraw_r.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/libraw/COPYRIGHT
/usr/share/doc/libraw/Changelog.txt
/usr/share/doc/libraw/LICENSE.CDDL
/usr/share/doc/libraw/LICENSE.LGPL

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-LibRaw

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libraw.so.20
/usr/lib64/glibc-hwcaps/x86-64-v3/libraw.so.20.0.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libraw_r.so.20
/usr/lib64/glibc-hwcaps/x86-64-v3/libraw_r.so.20.0.0
/usr/lib64/glibc-hwcaps/x86-64-v4/libraw.so.20
/usr/lib64/glibc-hwcaps/x86-64-v4/libraw.so.20.0.0
/usr/lib64/glibc-hwcaps/x86-64-v4/libraw_r.so.20
/usr/lib64/glibc-hwcaps/x86-64-v4/libraw_r.so.20.0.0
/usr/lib64/libraw.so.20
/usr/lib64/libraw.so.20.0.0
/usr/lib64/libraw_r.so.20
/usr/lib64/libraw_r.so.20.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/LibRaw/39a21f33cadea18adcc23bf808d7d5ea6419c8b1
/usr/share/package-licenses/LibRaw/c24b9c7ef03687bf0141f85a1b7ed81459944c3c
