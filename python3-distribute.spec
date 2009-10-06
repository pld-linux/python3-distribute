%bcond_with	tests	# enble tests
#
%define		pname	distribute
Summary:	Easily download, build, install, upgrade, and uninstall Python packages
Name:		python3-distibute
Version:	0.6.3
Release:	0.1
License:	PSF or ZPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/d/distribute/distribute-%{version}.tar.gz
# Source0-md5:	3940fd02a763f001014296cfec5e69f2
URL:		http://www.argo.es/~jcea/programacion/pybsddb.htm
BuildRequires:  python3
BuildRequires:	python3-modules
BuildRequires:	python3-devel
BuildRequires:	rpm-build-macros >= 1.523
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Distribute is a fork of the Setuptools project.

Distribute is intended to replace Setuptools as the standard method for working
with Python module distributions.
 
%prep
%setup -q -n %{pname}-%{version}

%build
python3 setup.py \
	build

%if %{with tests}
python3 setup.py test
%endif

%install
rm -rf $RPM_BUILD_ROOT
python3 -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

# shutup check-files
%py3_postclean
rm $RPM_BUILD_ROOT%{_bindir}/easy_install
rm $RPM_BUILD_ROOT%{py3_sitescriptdir}/setuptools/*.exe
rm -rf $RPM_BUILD_ROOT%{py3_sitescriptdir}/setuptools/tests
# reinstall site.py deleted by py3_postclean
cp site.py $RPM_BUILD_ROOT%{py3_sitescriptdir}/site.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc *.txt docs
%attr(755,root,root) %{_bindir}/easy_install-3.*
%{py3_sitescriptdir}/*.egg-info
%dir %{py3_sitescriptdir}/setuptools
%dir %{py3_sitescriptdir}/setuptools/command
%{py3_sitescriptdir}/pkg_resources.py[co]
%{py3_sitescriptdir}/easy_install.py[co]
%{py3_sitescriptdir}/site.py
%{py3_sitescriptdir}/site.py[co]
%{py3_sitescriptdir}/setuptools.pth
%{py3_sitescriptdir}/setuptools/*.py[co]
%{py3_sitescriptdir}/setuptools/command/*.py[co]
