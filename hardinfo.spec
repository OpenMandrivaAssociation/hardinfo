# comment out if not snapshot
%define gitdate	08.01.2020

# rel to bump
%define rel	1

Name:		hardinfo
Version:	0.6
Release:	0.%{gitdate}.%{rel}
Summary:	A system profiler for Linux
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://hardinfo.org
#Source taken from here: https://github.com/lpereira/hardinfo/
Source0:	%{name}-%{gitdate}.tar.lz
BuildRequires:	pciutils
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libsoup-2.4)
# Hardinfo (git) can be build now with GTK3 but still missing some test/benchmarks.
# Let's check in near future GTK3. Switch only if functionality will be satisfactory (angry)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
Requires:	pciutils

%description
HardInfo is a system profiler for Linux systems.
It can display information about the hardware, software, and perform
simple benchmarks.

%prep
%autosetup -p1 -n %{name}-%{gitdate}

%build
%cmake \
     -DCMAKE_INSTALL_LIBDIR=%{_lib} \
     -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install

desktop-file-install --vendor="" \
  --set-generic-name='Hardware Information' \
  --set-comment='System Information' \
  --remove-category="Application" \
  --add-category="Settings;HardwareSettings;" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/hardinfo.png
%{_mandir}/man1/hardinfo.1*
