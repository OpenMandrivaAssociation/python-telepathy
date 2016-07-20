Name:           python2-telepathy
Version:        0.15.19
Release:        3
Summary:        Python libraries for Telepathy
Group:          Development/Python
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/telepathy-python/telepathy-python-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  libxslt-proc
%rename	python-telepathy

%description
Python libraries for use in Telepathy clients and connection managers.

%files
%doc COPYING AUTHORS README
%{python2_sitelib}/telepathy/

#--------------------------------------------------------------------

%prep
%setup -q -n telepathy-python-%{version}


%build
export PYTHON=python2
%configure2_5x
# parallel build fails
make

%install
%makeinstall_std

