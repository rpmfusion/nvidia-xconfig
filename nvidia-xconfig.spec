Name:           nvidia-xconfig
Version:        396.54
Release:        1%{?dist}
Summary:        NVIDIA X configuration file editor

Group:          Applications/System
License:        GPLv2+
URL:            https://download.nvidia.com/XFree86/nvidia-xconfig
Source0:        %{url}/nvidia-xconfig-%{version}.tar.bz2
Patch0:         nvidia-xconfig-1.0-default.patch

ExclusiveArch: x86_64

BuildRequires: hostname
BuildRequires: m4


%description
NVIDIA X configuration file editor.



%prep
%setup -q

sed -i -e 's|/usr/local|%{_prefix}|g' utils.mk


%build
make  \
  NVDEBUG=1 \
  NV_VERBOSE=1 \
  STRIP_CMD=true NV_KEEP_UNSTRIPPED_BINARIES=1 \
  X_LDFLAGS="-L%{_libdir}" \
  CC_ONLY_CFLAGS="%{optflags}"
(cd _out/Linux_*/ ; cp %{name}.unstripped %{name} ; cd -)


%install
mkdir -p %{buildroot}%{_sbindir}
%make_install INSTALL="install -p"


%files
%license COPYING
%{_bindir}/nvidia-xconfig
%{_mandir}/man1/nvidia-xconfig.1.*


%changelog
* Wed Aug 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 396.54-1
- Update to 396.54

* Sat Aug 04 2018 Leigh Scott <leigh123linux@googlemail.com> - 396.51-1
- Update to 396.51

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 396.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 396.45-1
- Update to 396.45

* Fri May 04 2018 Leigh Scott <leigh123linux@googlemail.com> - 396.24-1
- Update to 396.24

* Thu Mar 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 390.48-1
- Update to 390.48

* Tue Mar 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 390.42-1
- Update to 390.42

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 390.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 390.25-1
- Update to 390.25

* Thu Jan 11 2018 Leigh Scott <leigh123linux@googlemail.com> - 390.12-1
- Update to 390.12

* Sat Dec 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 387.34-1
- Update to 387.34

* Mon Oct 30 2017 Nicolas Chauvet <kwizart@gmail.com> - 387.22-1
- Update to 387.22

* Tue Sep 26 2017 Leigh Scott <leigh123linux@googlemail.com> - 384.90-1
- Update to 384.90

* Thu Aug 03 2017 Nicolas Chauvet <kwizart@gmail.com> - 384.59-1
- Update to 384.59

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 319.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 21 2013 Nicolas Chauvet <kwizart@gmail.com> - 319.32-1
- Build an empty package to workaround yum issue with obsoletes

* Thu Jun 27 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0-29
- Update to 319.32

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

