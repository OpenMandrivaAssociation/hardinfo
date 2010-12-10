%define name hardinfo
%define version 0.5.1
%define release %mkrel 2

Summary: A system profiler for Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.berlios.de/hardinfo/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: System/Kernel and hardware 
Url: http://hardinfo.berlios.de
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pciutils, libsoup-2.2-devel, gtk2-devel, zlib-devel
BuildRequires: desktop-file-utils
Requires: pciutils

%description
HardInfo is a system profiler for Linux systems.
It can display information about the hardware, software, and perform 
simple benchmarks.

%prep
%setup -q

%build
#export LIBDIR=%{_libdir}
%configure2_5x
#perl -pi -e "s|/usr/lib/hardinfo/|%{_libdir}/hardinfo/|g" Makefile
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Settings" \
  --add-category="HardwareSettings" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%name.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files
%defattr(-,root,root)
%{_bindir}/hardinfo
%{_libdir}/%{name}/modules/*so
%{_datadir}/%{name}/pixmaps/*
%{_datadir}/%{name}/benchmark.conf
%{_datadir}/%{name}/benchmark.data
%{_datadir}/applications/%{name}.desktop
