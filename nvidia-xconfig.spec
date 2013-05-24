%global nversion         319.23

Name:           nvidia-xconfig
Version:        1.0
Release:        28%{?dist}
Summary:        NVIDIA X configuration file editor

Group:          Applications/System
License:        GPLv2+
URL:            http://cgit.freedesktop.org/~aplattner/nvidia-xconfig/
Source0:        http://cgit.freedesktop.org/~aplattner/nvidia-xconfig/snapshot/nvidia-xconfig-%{nversion}.tar.bz2
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
Provides: %{name}-nversion = %{nversion}


%description
NVIDIA X configuration file editor.



%prep
%setup -q -n nvidia-xconfig-%{nversion}

sed -i -e 's|/usr/local|%{_prefix}|g' utils.mk


%build
make  \
  NVDEBUG=1 \
  NV_VERBOSE=1 \
  X_LDFLAGS="-L%{_libdir}" \
  CC_ONLY_CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

#We usually have it in sbin
mv $RPM_BUILD_ROOT%{_bindir}/nvidia-xconfig \
  $RPM_BUILD_ROOT%{_sbindir}
rmdir $RPM_BUILD_ROOT%{_bindir}



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING
%{_sbindir}/nvidia-xconfig
%{_mandir}/man1/nvidia-xconfig.1.*

%changelog
* Fri May 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0-28
- Update to 319.23

* Mon May 13 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0-27
- Update to 319.17

* Wed Jan 16 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0-26
- Update to 313.18

* Tue Oct 16 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0-25
- Update to 310.14

* Mon Sep 24 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0-24
- Update to 304.51

* Sat Sep 15 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0-23
- Update to 304.48

* Wed Sep 05 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0-22
- Update to 304.43

* Tue Aug 14 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0-21
- Update to 304.37

* Tue Jul 31 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0-20
- Update to 304.30

* Sat Jul 14 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0-19
- Update to 304.22

* Sun Jun 17 2012 leigh scott <leigh123linux@googlemail.com> - 1.0-18
- Update to 302.17

* Tue May 22 2012 leigh scott <leigh123linux@googlemail.com> - 1.0-17
- Update to 302.11

* Tue May 22 2012 leigh scott <leigh123linux@googlemail.com> - 1.0-16
- Update to 295.53

* Thu May 03 2012 leigh scott <leigh123linux@googlemail.com> - 1.0-15
- Update to 295.49

* Wed Apr 11 2012 leigh scott <leigh123linux@googlemail.com> - 1.0-14
- Update to 295.40
- Fix source url

* Thu Mar 22 2012 leigh scott <leigh123linux@googlemail.com> - 1.0-13
- Update to 295.33

* Mon Feb 27 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0-12
- Update to 295.20

* Wed Nov 23 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0-11
- Update to 290.10

* Thu Oct 13 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0-10
- Update internal version to 285.05.09

* Sun Jul 31 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0-9
- Update internal version to 280.11

* Sun May 01 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0-8
- Update internal version to 270.41.06

* Sat Jan 22 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0-7
- Update internal version to 260.19.36

* Thu Dec 16 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.0-6
- Update internal version to 260.19.29

* Sun Oct 10 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.0-5
- Update internal version to 260.19.06

* Mon Sep 06 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.0-4
- Update internal version to 256.53

* Sat Jul 10 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.0-3
- Update internal version to 256.35
- Provides %%{name}-nversion

* Sun Feb 28 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.0-2
- Update internal version to 195.36.08

* Mon Oct 26 2009 kwizart < kwizart at gmail.com > - 1.0-1
- Update internal version to 190.42

* Wed May 28 2008 kwizart < kwizart at gmail.com > - 1.0-1.1
- First Package for Fedora.

