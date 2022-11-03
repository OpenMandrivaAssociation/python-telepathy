Name:           python-telepathy
Version:        2.3.2
Release:        1
Summary:        Python libraries for Telepathy
Group:          Development/Python
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        https://files.pythonhosted.org/packages/source/t/telepathy/telepathy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  libxslt-proc
BuildRequires:	python-setuptools

%description
Python libraries for use in Telepathy clients and connection managers.

%files
%{_bindir}/telepathy
%{python_sitelib}/telepathy*.egg-info
%{python_sitelib}/telepathy/

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n telepathy-%{version}

%build
%py_build

%install
%py_install
