Name:           python-telepathy
Version:        0.15.3
Release:        %mkrel 2
Summary:        Python libraries for Telepathy
Group:          Development/Python
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/telepathy-python/telepathy-python-%{version}.tar.bz2
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
%{py_puresitedir}/telepathy_python-%version-py%pyver.egg-info

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
