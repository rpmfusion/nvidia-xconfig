%global iversion         195.36.08

Name:           nvidia-xconfig
Version:        1.0
Release:        2%{?dist}
Summary:        NVIDIA X configuration file editor

Group:          Applications/System
License:        GPLv2+
URL:            http://cgit.freedesktop.org/~aplattner/nvidia-xconfig/
Source0:        http://cgit.freedesktop.org/~aplattner/nvidia-xconfig/snapshot/nvidia-xconfig-%{iversion}.tar.bz2
Patch0:         nvidia-xconfig-1.0-default.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora} > 11 || 0%{?rhel} > 5
ExclusiveArch: i686 x86_64
%else 0%{?fedora} == 11
ExclusiveArch: i586 x86_64
%else
ExclusiveArch: i386 x86_64
%endif

BuildRequires: m4


%description
NVIDIA X configuration file editor.



%prep
%setup -q -n nvidia-xconfig-%{iversion}
%patch0 -p1 -b .default


%build
make CFLAGS="$RPM_OPT_FLAGS -IXF86Config-parser" NVDEBUG=1


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
make install ROOT=$RPM_BUILD_ROOT INSTALL="install -p"



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING
%{_sbindir}/nvidia-xconfig
%{_mandir}/man1/nvidia-xconfig.1.*

%changelog
* Sun Feb 28 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.0-2
- Update internal version to 195.36.08

* Mon Oct 26 2009 kwizart < kwizart at gmail.com > - 1.0-1
- Update internal version to 190.42

* Wed May 28 2008 kwizart < kwizart at gmail.com > - 1.0-1.1
- First Package for Fedora.

