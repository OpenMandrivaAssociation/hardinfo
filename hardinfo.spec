%define name hardinfo
%define version 0.4.2.3
%define release %mkrel 1

Summary: A system profiler for Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.berlios.de/hardinfo/%{name}-%{version}.tar.bz2
Patch0: multilibfix.patch  
Patch2: fixuserdsp.patch
Patch4: fix_crash.patch
Patch5: libzfix.patch
License: GPLv2+
Group: System/Kernel and hardware 
Url: http://hardinfo.berlios.de
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pciutils, libsoup-devel, gtk2-devel, zlib-devel
BuildRequires: desktop-file-utils
Requires: pciutils

%description
HardInfo is a system profiler for Linux systems.
It can display information about the hardware, software, and perform 
simple benchmarks.

%prep
%setup -q
#fix multilib build isses (upstream working on better one)
#%patch0 -p1 -b .multilib
#use correct uids
%patch2 -p1 -b .fixuserdsp
#fix double free bug
#%patch4 -p1 -b .crash
#fix libz.so detection
%patch5 -p1 -b .libzfix

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
/sbin/ldconfig
%update_menus

%postun
/sbin/ldconfig
%clean_menus

%files
%defattr(-,root,root)
%{_bindir}/hardinfo
%{_libdir}/%{name}/modules/*so
%{_datadir}/%{name}/pixmaps/*
%{_datadir}/%{name}/benchmark.conf
%{_datadir}/%{name}/benchmark.data
%{_datadir}/applications/%{name}.desktop
