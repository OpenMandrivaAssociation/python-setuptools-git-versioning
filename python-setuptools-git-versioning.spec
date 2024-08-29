%global	module setuptools-git-versioning

Summary:	Use git repo data for building a version number according PEP-440
Name:		python-%{module}
Version:	2.0.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://setuptools-git-versioning.readthedocs.io
Source0:	https://pypi.io/packages/source/s/%{module}/%{module}-%{version}.tar.gz
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(toml)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
Use git repo data (latest tag, current commit hash, etc) for building
a version number according PEP 440.

%files
%doc README.rst
%license LICENSE
%{_bindir}/%{module}
%{py_puresitedir}/setuptools_git_versioning.py
%{py_puresitedir}/setuptools_git_versioning-*.*-info/

#------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}

rm -rf setuptools_git_versioning.egg-info

%build
%py_build

%install
%py_install
