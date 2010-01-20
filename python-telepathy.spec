Name:           python-telepathy
Version:        0.15.14
Release:        %mkrel 1
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
