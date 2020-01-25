#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Geometry-Planar
Summary:	Math::Geometry::Planar - a collection of planar geometry functions
Summary(pl.UTF-8):	Math::Geometry::Planar - zestaw funkcji do geometrii na płaszczyźnie
Name:		perl-Math-Geometry-Planar
Version:	1.17
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9b5c6bbe59e578ac14c975f6d3758666
URL:		http://search.cpan.org/dist/Math-Geometry-Planar/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Math-Geometry-Planar-GPC >= 1.04
BuildRequires:	perl-Math-Geometry-Planar-Offset >= 1.00
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-Geometry-Planar-GPC >= 1.04
# loop
#Requires:	perl-Math-Geometry-Planar-Offset >= 1.00
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a set of 2D polygon, line and line segment
operations. The module also uses the GPC module for polygon clipping
operaions.

%description -l pl.UTF-8
Ten moduł udostępnia zestaw operacji na wielokątach 2D, liniach i
odcinkach. Używa modułu GPC do obcinania wielokątów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Math/Geometry
%{perl_vendorlib}/Math/Geometry/Planar.pm
%{_mandir}/man3/*
