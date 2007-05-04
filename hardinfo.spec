%define name hardinfo
%define version 0.4.2.1
%define release %mkrel 1

Summary: A system profiler for Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware 
Url: http://download.berlios.de/hardinfo/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pciutils, libsoup-devel, gtk2-devel, zlib-devel

%description
HardInfo is a system profiler for Linux systems.
It can display information about the hardware, software, and perform 
simple benchmarks.

%prep
%setup -q
%configure

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p %{buildroot}%{_menudir}

cat > %{buildroot}%{_menudir}/%{name} << EOF
?package(%{name}): \
        command="%{_bindir}/%{name}" \
        title="Hardinfo" \
        longtitle="Hardinfo (System Profiler)" \
        icon="/usr/share/hardinfo/pixmaps/logo.png" \
        needs="x11" \
        section="System/Configuration/Hardware" \
        xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Settings" \
  --add-category="HardwareSettings" \
  --add-category="X-MandrivaLinux-System-Configuration-Hardware" \
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
%{_menudir}/%{name}

%changelog
