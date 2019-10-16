#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SPIRV-Headers
Version  : 1.5.1.corrected
Release  : 6
URL      : https://github.com/KhronosGroup/SPIRV-Headers/archive/1.5.1.corrected/SPIRV-Headers-1.5.1.corrected.tar.gz
Source0  : https://github.com/KhronosGroup/SPIRV-Headers/archive/1.5.1.corrected/SPIRV-Headers-1.5.1.corrected.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: SPIRV-Headers-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
# SPIR-V Headers
This repository contains machine-readable files for the
[SPIR-V Registry](https://www.khronos.org/registry/spir-v/).
This includes:

%package dev
Summary: dev components for the SPIRV-Headers package.
Group: Development
Provides: SPIRV-Headers-devel = %{version}-%{release}
Requires: SPIRV-Headers = %{version}-%{release}

%description dev
dev components for the SPIRV-Headers package.


%package license
Summary: license components for the SPIRV-Headers package.
Group: Default

%description license
license components for the SPIRV-Headers package.


%prep
%setup -q -n SPIRV-Headers-1.5.1.corrected

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571239986
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1571239986
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SPIRV-Headers
cp LICENSE %{buildroot}/usr/share/package-licenses/SPIRV-Headers/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/spirv/1.0/GLSL.std.450.h
/usr/include/spirv/1.0/OpenCL.std.h
/usr/include/spirv/1.0/extinst.glsl.std.450.grammar.json
/usr/include/spirv/1.0/extinst.opencl.std.100.grammar.json
/usr/include/spirv/1.0/spirv.core.grammar.json
/usr/include/spirv/1.0/spirv.cs
/usr/include/spirv/1.0/spirv.h
/usr/include/spirv/1.0/spirv.hpp
/usr/include/spirv/1.0/spirv.hpp11
/usr/include/spirv/1.0/spirv.json
/usr/include/spirv/1.0/spirv.lua
/usr/include/spirv/1.0/spirv.py
/usr/include/spirv/1.1/GLSL.std.450.h
/usr/include/spirv/1.1/OpenCL.std.h
/usr/include/spirv/1.1/extinst.glsl.std.450.grammar.json
/usr/include/spirv/1.1/extinst.opencl.std.100.grammar.json
/usr/include/spirv/1.1/spirv.core.grammar.json
/usr/include/spirv/1.1/spirv.cs
/usr/include/spirv/1.1/spirv.h
/usr/include/spirv/1.1/spirv.hpp
/usr/include/spirv/1.1/spirv.hpp11
/usr/include/spirv/1.1/spirv.json
/usr/include/spirv/1.1/spirv.lua
/usr/include/spirv/1.1/spirv.py
/usr/include/spirv/1.2/GLSL.std.450.h
/usr/include/spirv/1.2/OpenCL.std.h
/usr/include/spirv/1.2/extinst.glsl.std.450.grammar.json
/usr/include/spirv/1.2/extinst.opencl.std.100.grammar.json
/usr/include/spirv/1.2/spirv.core.grammar.json
/usr/include/spirv/1.2/spirv.cs
/usr/include/spirv/1.2/spirv.h
/usr/include/spirv/1.2/spirv.hpp
/usr/include/spirv/1.2/spirv.hpp11
/usr/include/spirv/1.2/spirv.json
/usr/include/spirv/1.2/spirv.lua
/usr/include/spirv/1.2/spirv.py
/usr/include/spirv/spir-v.xml
/usr/include/spirv/unified1/GLSL.std.450.h
/usr/include/spirv/unified1/OpenCL.std.h
/usr/include/spirv/unified1/extinst.glsl.std.450.grammar.json
/usr/include/spirv/unified1/extinst.opencl.std.100.grammar.json
/usr/include/spirv/unified1/spirv.core.grammar.json
/usr/include/spirv/unified1/spirv.cs
/usr/include/spirv/unified1/spirv.h
/usr/include/spirv/unified1/spirv.hpp
/usr/include/spirv/unified1/spirv.hpp11
/usr/include/spirv/unified1/spirv.json
/usr/include/spirv/unified1/spirv.lua
/usr/include/spirv/unified1/spirv.py
/usr/include/spirv/unified1/spv.d
/usr/lib64/cmake/SPIRV-Headers/SPIRV-HeadersConfig.cmake
/usr/lib64/cmake/SPIRV-Headers/SPIRV-HeadersConfigVersion.cmake
/usr/lib64/cmake/SPIRV-Headers/SPIRV-HeadersTargets.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SPIRV-Headers/LICENSE
