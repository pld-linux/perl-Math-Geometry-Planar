#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Geometry-Planar
Summary:	Math::Geometry::Planar - A collection of planar geometry functions
Summary(pl):	Math::Geometry::Planar - zestaw funkcji do geometrii na p³aszczy¼nie
Name:		perl-Math-Geometry-Planar
Version:	1.09
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Math-Geometry-GPC >= 1.03
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-Geometry-GPC >= 1.03
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a set of 2D polygon, line and line segment
operations. The module also uses the GPC module for polygon clipping
operaions.

%description -l pl
Ten modu³ udostêpnia zestaw operacji na wielok±tach 2D, liniach i
odcinkach. U¿ywa modu³u GPC do obcinania wielok±tów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

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
