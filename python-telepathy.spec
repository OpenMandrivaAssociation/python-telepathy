Name:           python-telepathy
Version:        0.15.19
Release:        2
Summary:        Python libraries for Telepathy
Group:          Development/Python
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/telepathy-python/telepathy-python-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  libxslt-proc

%description
Python libraries for use in Telepathy clients and connection managers.

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%{python_sitelib}/telepathy/

#--------------------------------------------------------------------

%prep
%setup -q -n telepathy-python-%{version}


%build
%configure2_5x
# parallel build fails
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Tue Dec 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.15.19-1mdv2011.0
+ Revision: 625616
- update to new version 0.15.19

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 0.15.18-2mdv2011.0
+ Revision: 592880
- rebuild for new python 2.7

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.15.18-1mdv2011.0
+ Revision: 569672
- update to new version 0.15.18

* Sun Apr 18 2010 Frederik Himpe <fhimpe@mandriva.org> 0.15.17-1mdv2010.1
+ Revision: 536460
- update to new version 0.15.17

* Thu Jan 21 2010 Frederik Himpe <fhimpe@mandriva.org> 0.15.15-1mdv2010.1
+ Revision: 494636
- update to new version 0.15.15

* Wed Jan 20 2010 Frederik Himpe <fhimpe@mandriva.org> 0.15.14-1mdv2010.1
+ Revision: 494174
- update to new version 0.15.14

* Tue Dec 15 2009 Frederik Himpe <fhimpe@mandriva.org> 0.15.13-1mdv2010.1
+ Revision: 479069
- update to new version 0.15.13

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.15.12-1mdv2010.1
+ Revision: 462143
- Update to new version 0.5.12
- Uses autotools now

* Wed Aug 19 2009 Frederik Himpe <fhimpe@mandriva.org> 0.15.11-1mdv2010.0
+ Revision: 418066
- update to new version 0.15.11

* Thu Jul 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.15.10-1mdv2010.0
+ Revision: 404717
- update to new version 0.15.10

* Tue Jul 28 2009 Frederik Himpe <fhimpe@mandriva.org> 0.15.9-1mdv2010.0
+ Revision: 402536
- update to new version 0.15.9

* Mon Jun 15 2009 Frederik Himpe <fhimpe@mandriva.org> 0.15.8-1mdv2010.0
+ Revision: 386114
- update to new version 0.15.8

* Wed Mar 04 2009 Aleksey Lim <alsroot@mandriva.org> 0.15.7-1mdv2009.1
+ Revision: 348240
- update to new version 0.15.7

* Sat Jan 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.15.6-1mdv2009.1
+ Revision: 327962
- update to new version 0.15.6

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 0.15.3-2mdv2009.1
+ Revision: 320647
- fix file list
- update license

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.15.3-1mdv2009.1
+ Revision: 305887
- update to new version 0.15.3

* Sat Oct 18 2008 Frederik Himpe <fhimpe@mandriva.org> 0.15.2-1mdv2009.1
+ Revision: 294879
- update to new version 0.15.2

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.15.1-1mdv2009.0
+ Revision: 280567
- New version

* Sun Jun 15 2008 Funda Wang <fwang@mandriva.org> 0.15.0-1mdv2009.0
+ Revision: 219217
- update to new version 0.15.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 11 2007 Funda Wang <fwang@mandriva.org> 0.13.13-1mdv2008.0
+ Revision: 51240
- New version

* Sun Jun 10 2007 Michael Scherer <misc@mandriva.org> 0.13.12-1mdv2008.0
+ Revision: 37795
- add missing BuildRequires
- update to 0.13.12

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - new version 0.13.11
    - New version 0.13.9


* Tue Nov 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.13.2-3mdv2007.0
+ Revision: 87969
- Fix File list
-  Rebuild against new python
- Import python-telepathy

* Wed Oct 11 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.13.2-1mdv2007.1
- First Mandriva package (help from fedora one)

