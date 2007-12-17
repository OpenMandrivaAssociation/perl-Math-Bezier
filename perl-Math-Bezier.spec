%define module	Math-Bezier
%define name	perl-%{module}
%define version 0.01
%define release %mkrel 9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Solution of Bezier Curves
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp.perl.org/pub/CPAN/modules/by-module/Math/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch

%description
This module implements the algorithm for the solution of Bezier curves
as presented by Robert D. Miller in Graphics Gems V, "Quick and Simple
Bezier Curve Drawing". 

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Math
%{_mandir}/*/*

