Name:           python-telepathy
Version:        0.13.13
Release:        %mkrel 1
Summary:        Python libraries for Telepathy
Group:          Development/Python
License:        LGPL
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/telepathy-python/telepathy-python-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  libxslt-proc

%description
Python libraries for use in Telepathy clients and connection managers.

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%{python_sitelib}/telepathy/
%{py_puresitedir}/telepathy_python-%version-py2.5.egg-info

#--------------------------------------------------------------------

%prep
%setup -q -n telepathy-python-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT
