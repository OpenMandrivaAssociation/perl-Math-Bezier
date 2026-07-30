%define upstream_name	 Math-Bezier
%define upstream_version 0.01
Name:		perl-%{upstream_name}
Version:	0.01
Release:	1

Summary:	Solution of Bezier Curves
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/A/AB/ABW/Math-Bezier-0.01.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements the algorithm for the solution of Bezier curves
as presented by Robert D. Miller in Graphics Gems V, "Quick and Simple
Bezier Curve Drawing". 

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/Math
%{_mandir}/*/*


